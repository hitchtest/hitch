"""High level command line interface to hitch."""
from subprocess import call, PIPE, STDOUT, Popen
from hitch.click import command, group, argument, option
from os import path, makedirs, listdir, kill, remove
from sys import stderr, exit, modules, argv
from functools import partial
from hitch import hitchdir, languagestrings
import shutil
import signal
import copy


class CalledProcessError(Exception):
    """Re-implemented CalledProcessError, since it is not available < python 2.7."""
    pass


def check_output(command, stdout=PIPE, stderr=PIPE):
    """Re-implemented subprocess.check_output since it is not available < python 2.7."""
    return Popen(command, stdout=stdout, stderr=stderr).communicate()[0]


def check_call(command, shell=False):
    """Re-implemented subprocess.check_call since it is not available < python 2.7."""
    process = Popen(command, shell=shell)
    process.communicate()
    if process.returncode != 0:
        raise CalledProcessError
    return


def stop_everything(sig, frame):
    """Exit hitch."""
    exit(1)


def installpackages():
    """Install packages with hitchsystem."""
    hitchsystem = path.abspath(path.join(".hitch", "virtualenv", "bin", "hitchsystem"))
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    check_call([hitchsystem, "installpackages", ])
    signal.signal(signal.SIGINT, stop_everything)


@group()
def cli():
    pass

@command()
@option(
    '-p', '--python', default=None,
    help=languagestrings.SPECIFY_PYTHON_TO_CREATE_VIRTUALENV_WITH
)
@option(
    '-v', '--virtualenv', default=None,
    help=languagestrings.SPECIFY_VIRTUALENV_TO_CREATE_HITCH_WITH
)
def init(python, virtualenv):
    """Initialize hitch in this directory."""
    if virtualenv is None:
        if call(["which", "virtualenv"], stdout=PIPE, stderr=PIPE) != 0:
            stderr.write(languagestrings.YOU_MUST_HAVE_VIRTUALENV_INSTALLED)
            stderr.flush()
            exit(1)
        virtualenv = check_output(["which", "virtualenv"]).decode('utf8').replace("\n", "")
    else:
        if path.exists(virtualenv):
            if python is None:
                python = path.join(path.dirname(virtualenv), "python")
        else:
            stderr.write("{0} not found.\n".format(virtualenv))

    if python is None:
        if call(["which", "python3"], stdout=PIPE, stderr=PIPE) != 0:
            stderr.write(languagestrings.YOU_MUST_HAVE_PYTHON3_INSTALLED)
            stderr.flush()
            exit(1)
        python3 = check_output(["which", "python3"]).decode('utf8').replace("\n", "")
    else:
        if path.exists(python):
            python3 = python
        else:
            stderr.write("{0} not found.\n".format(python))
            exit(1)

    python_version = check_output([python3, "-V"], stderr=STDOUT).decode('utf8')
    replacements = ('Python ', ''), ('\n', '')
    str_version = reduce(lambda a, kv: a.replace(*kv), replacements, python_version)
    tuple_version = tuple([int(x) for x in str_version.split('.')[:2]])

    if tuple_version < (3, 3):
        stderr.write(languagestrings.YOU_MUST_HAVE_VERSION_ABOVE_PYTHON33)
        exit(1)

    if hitchdir.hitch_exists():
        stderr.write(languagestrings.HITCH_ALREADY_INITIALIZED)
        stderr.flush()
        exit(0)

    makedirs(".hitch")

    # Store absolute directory in .hitch directory to guard against the directory being moved
    hitch_dir = path.abspath(".hitch")
    with open(path.join(hitch_dir, "absdir"), "w") as absdir_handle:
        absdir_handle.write(hitch_dir)

    pip = path.abspath(path.join(".hitch", "virtualenv", "bin", "pip"))

    try:
        check_call([
            virtualenv, ".hitch/virtualenv", "--no-site-packages", "--distribute", "-p", python3
        ])
        check_call([pip, "install", "-U", "pip"])
        check_call([pip, "install", "unixpackage", "hitchsystem"])

        installpackages()

        if path.exists("hitchreqs.txt"):
            check_call([pip, "install", "-r", "hitchreqs.txt"])
        else:
            check_call([pip, "install", "hitchtest"])

            pip_freeze = check_output([pip, "freeze"]).decode('utf8')

            with open("hitchreqs.txt", "w") as hitchreqs_handle:
                hitchreqs_handle.write(pip_freeze)

        installpackages()
    except CalledProcessError:
        stderr.write(languagestrings.ERROR_INITIALIZING_HITCH)
        hitchdir.remove_hitch_directory_if_exists()
        exit(1)



def update_requirements():
    """Check hitchreqs.txt match what's installed via pip freeze. If not, update."""
    pip = path.join(hitchdir.get_hitch_directory_or_fail(), "virtualenv", "bin", "pip")
    hitchreqs_filename = path.join(hitchdir.get_hitch_directory_or_fail(), "..", "hitchreqs.txt")
    pip_freeze = check_output([pip, "freeze"]).decode('utf8').split('\n')
    hitchreqs_handle = ""
    with open(hitchreqs_filename, "r") as hitchreqs_handle:
        hitchreqs = hitchreqs_handle.read().split('\n')

    if not sorted(pip_freeze) == sorted(hitchreqs):
        call([pip, "install", "-r", "hitchreqs.txt"])

    pip_freeze = check_output([pip, "freeze"]).decode('utf8')

    with open("hitchreqs.txt", "w") as hitchreqs_handle:
        hitchreqs_handle.write(pip_freeze)


def get_pip():
    """Get the file path to the hitch pip."""
    return path.join(hitchdir.get_hitch_directory_or_fail(), "virtualenv", "bin", "pip")


@command(context_settings={'help_option_names':[],'ignore_unknown_options':True}, help="dd")
@argument('arguments', nargs=-1)
def runpackage(arguments):
    # Generic method to run any installed app in the virtualenv whose name starts with hitch*
    hitchdir.check_hitch_directory_integrity()
    update_requirements()
    binfile = path.join(hitchdir.get_hitch_directory(), "virtualenv", "bin", "hitch{0}".format(argv[1]))
    command = [binfile, ] + argv[2:]

    # When receiving an exit signal, just forward it to process child.
    def forward_signal_to_child(pid, signum, frame):
        kill(pid, signum)

    process = Popen(command)
    signal.signal(signal.SIGINT, partial(forward_signal_to_child, process.pid))
    signal.signal(signal.SIGTERM, partial(forward_signal_to_child, process.pid))
    signal.signal(signal.SIGHUP, partial(forward_signal_to_child, process.pid))
    signal.signal(signal.SIGQUIT, partial(forward_signal_to_child, process.pid))
    return_code = process.wait()
    exit(return_code)

@command()
@argument('package', required=True)
def uninstall(package):
    """Uninstall hitch package."""
    hitchdir.check_hitch_directory_integrity()
    pip = get_pip()

    call([pip, "uninstall", package] )
    pip_freeze = check_output([pip, "freeze"]).decode('utf8')

    with open("hitchreqs.txt", "w") as hitchreqs_handle:
        hitchreqs_handle.write(pip_freeze)

@command()
@argument('package', required=True)
def install(package):
    """Install hitch package."""
    hitchdir.check_hitch_directory_integrity()
    pip = get_pip()

    call([pip, "install", package, "-U", ])
    pip_freeze = check_output([pip, "freeze"]).decode('utf8')

    with open("hitchreqs.txt", "w") as hitchreqs_handle:
        hitchreqs_handle.write(pip_freeze)

    installpackages()


@command()
def upgrade():
    """Upgrade all installed hitch packages."""
    hitchdir.check_hitch_directory_integrity()
    pip = get_pip()
    package_list = [
        p for p in check_output([pip, "freeze"]).decode('utf8').split('\n')
            if p != "" and "==" in p
    ]
    version_fixed_package_list = [p.split("==")[0] for p in package_list]

    for package in version_fixed_package_list:
        call([pip, "install", package, "-U", ])

    pip_freeze = check_output([pip, "freeze"]).decode('utf8')

    with open("hitchreqs.txt", "w") as hitchreqs_handle:
        hitchreqs_handle.write(pip_freeze)

    installpackages()


@command()
def freeze():
    """List installed hitch packages."""
    hitchdir.check_hitch_directory_integrity()
    pip = path.join(hitchdir.get_hitch_directory_or_fail(), "virtualenv", "bin", "pip")
    call([pip, "freeze", ])


@command()
def clean():
    """Remove the hitch directory entirely."""
    if hitchdir.hitch_exists():
        hitchdir.remove_hitch_directory_if_exists()
    else:
        stderr.write("No hitch directory found. Doing nothing.\n")
        stderr.flush()


@command()
@option(
    '-p', '--packages', default=None, help=(
        "Specify precise packages to remove - "
        "e.g. postgresql, postgresql-9.3.9, python, python2.6.8"
    )
)
def cleanpkg(packages):
    """Remove installed packages from the .hitchpkg directory."""
    hitchpkg = path.join(path.expanduser("~"), ".hitchpkg")

    if path.exists(hitchpkg):
        if packages is None:
            shutil.rmtree(hitchpkg)
        else:
            for file_or_dir in listdir(hitchpkg):
                if file_or_dir.startswith(packages):
                    if path.isdir(path.join(hitchpkg, file_or_dir)):
                        shutil.rmtree(path.join(hitchpkg, file_or_dir))
                    else:
                        remove(path.join(hitchpkg, file_or_dir))


def run():
    """Run hitch bootstrap CLI"""
    signal.signal(signal.SIGINT, stop_everything)
    signal.signal(signal.SIGTERM, stop_everything)
    signal.signal(signal.SIGHUP, stop_everything)
    signal.signal(signal.SIGQUIT, stop_everything)

    if hitchdir.hitch_exists():
        # Get packages from bin folder that are hitch related
        python_bin = path.join(hitchdir.get_hitch_directory(), "virtualenv", "bin", "python")
        if path.exists(python_bin):
            packages = [
                package.replace("hitch", "") for package in listdir(
                    path.join(hitchdir.get_hitch_directory(), "virtualenv", "bin")
                )
                if package.startswith("hitch") and package != "hitch"
            ]

            # Add commands that start with "hitch" to the list of commands available (e.g. hitchtest, hitchsmtp)
            for package in packages:
                cmd = copy.deepcopy(runpackage)
                cmd.name = package
                try:
                    description = check_output([
                        python_bin, '-c',
                        'import sys;sys.stdout.write(__import__("hitch{0}").commandline.cli.help)'.format(
                            package
                        )
                    ]).decode('utf8')
                except CalledProcessError:
                    description = ""
                cmd.help = description
                cmd.short_help = description
                cli.add_command(cmd)

            cli.add_command(install)
            cli.add_command(uninstall)
            cli.add_command(upgrade)
            cli.add_command(freeze)
        else:
            stderr.write(languagestrings.SOMETHING_CORRUPTED)

        cli.add_command(clean)
        cli.add_command(cleanpkg)
        cli.add_command(init)
        cli.help = "Hitch test runner for:\n\n  {0}.".format(hitchdir.get_hitch_directory())
    else:
        cli.add_command(init)
        cli.add_command(clean)
        cli.add_command(cleanpkg)
        cli.help = "Hitch bootstrapper - '.hitch' directory not detected here."
    cli()

if __name__ == '__main__':
    run()
