"""High level command line interface to hitch."""
from subprocess import call, PIPE, STDOUT, CalledProcessError, Popen
from hitch.click import command, group, argument, option
from sys import stderr, exit, modules, argv
from os import path, makedirs, listdir, kill
from functools import partial
from hitch import hitchdir
import shutil
import signal
import copy

def check_output(command, stdout=PIPE, stderr=PIPE):
    """Re-implemented subprocess.check_output since it is not available < python 2.7."""
    return Popen(command, stdout=stdout, stderr=stderr).communicate()[0]

@group()
def cli():
    pass

@command()
@option(
    '-p', '--python', default=None,
    help="""Create hitch virtualenv using specific python version"""
         """ (e.g. /usr/bin/python3). Defaults to using python3 on the system path."""
)
@option(
    '-v', '--virtualenv', default=None,
    help="""Create hitch virtualenv using specific virtualenv"""
         """ (e.g. /usr/bin/virtualenv). Defaults to using virtualenv on the system path."""
)
def init(python, virtualenv):
    """Initialize hitch in this directory."""
    if virtualenv is None:
        if call(["which", "virtualenv"], stdout=PIPE, stderr=PIPE):
            stderr.write("You must have virtualenv installed to use hitch.\n")
            stderr.flush()
            exit(1)
        virtualenv = check_output(["which", "virtualenv"]).decode('utf8').replace("\n", "")
    else:
        if path.exists(virtualenv):
            if python is None:
                python = path.join(path.dirname(virtualenv), "python")
        else:
            stderr.write("{} not found.\n".format(virtualenv))

    if python is None:
        if call(["which", "python3"], stdout=PIPE, stderr=PIPE):
            stderr.write(
                "To use Hitch, you must have python 3 installed on your system "
                "and available. If your python3 is not on the system path with "
                "the name python3, specify its exact location using --python.\n"
            )
            stderr.flush()
            exit(1)
        python3 = check_output(["which", "python3"]).decode('utf8').replace("\n", "")
    else:
        if path.exists(python):
            python3 = python
        else:
            stderr.write("{} not found.\n".format(python))
            exit(1)

    str_version = check_output([python3, "-V"], stderr=STDOUT).decode('utf8').replace('\n', '')
    tuple_version = tuple([int(v) for v in str_version.replace('Python ', '').split('.')])

    if tuple_version < (3, 3):
        stderr.write(
            "The hitch environment must have python >=3.3 installed to be built.\n Your "
            "app can run with earlier versions of python, but the testing environment can't.\n"
        )
        exit(1)

    if hitchdir.hitch_exists():
        stderr.write("Hitch has already been initialized in this directory or a directory above it.\n")
        stderr.write("If you wish to re-initialize hitch in this directory, run 'hitch clean' in the")
        stderr.write("directory containing the .hitch directory and run hitch init here again.\n")
        stderr.flush()
        exit(1)

    makedirs(".hitch")
    pip = path.abspath(path.join(".hitch", "virtualenv", "bin", "pip"))

    call([virtualenv, ".hitch/virtualenv", "--no-site-packages", "--distribute", "-p", python3])
    call([pip, "install", "-U", "pip"])

    if path.exists("hitchreqs.txt"):
        call([pip, "install", "-r", "hitchreqs.txt"])
    else:
        call([pip, "install", "hitchtest"])

        pip_freeze = check_output([pip, "freeze"]).decode('utf8')

        with open("hitchreqs.txt", "w") as hitchreqs_handle:
            hitchreqs_handle.write(pip_freeze)

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
    update_requirements()
    binfile = path.join(hitchdir.get_hitch_directory(), "virtualenv", "bin", "hitch{}".format(argv[1]))
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
    pip = get_pip()

    call([pip, "uninstall", package] )
    pip_freeze = check_output([pip, "freeze"]).decode('utf8')

    with open("hitchreqs.txt", "w") as hitchreqs_handle:
        hitchreqs_handle.write(pip_freeze)

@command()
@argument('package', required=True)
def install(package):
    """Install hitch package."""
    pip = get_pip()

    call([pip, "install", package, "-U", ])
    pip_freeze = check_output([pip, "freeze"]).decode('utf8')

    with open("hitchreqs.txt", "w") as hitchreqs_handle:
        hitchreqs_handle.write(pip_freeze)

@command()
def upgrade():
    """Upgrade all installed hitch packages."""
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

@command()
def freeze():
    """List installed hitch packages."""
    pip = path.join(hitchdir.get_hitch_directory_or_fail(), "virtualenv", "bin", "pip")
    call([pip, "freeze", ])

@command()
def clean():
    """Remove the hitch directory entirely."""
    if hitchdir.hitch_exists():
        hitch_directory = hitchdir.get_hitch_directory_or_fail()
        shutil.rmtree(hitch_directory)
    else:
        stderr.write("No hitch directory found. Doing nothing.\n")
        stderr.flush()

def run():
    """Run hitch bootstrap CLI"""
    def stop_everything(sig, frame):
        """Exit hitch."""
        exit(1)

    signal.signal(signal.SIGINT, stop_everything)
    signal.signal(signal.SIGTERM, stop_everything)
    signal.signal(signal.SIGHUP, stop_everything)
    signal.signal(signal.SIGQUIT, stop_everything)

    if hitchdir.hitch_exists():
        if not path.exists(path.join(hitchdir.get_hitch_directory(), "virtualenv", "bin")):
            stderr.write("Hitch was initialized in this directory (or one above it), but something.\n")
            stderr.write("was corrupted. Try running 'hitch clean' and then run 'hitch init' again.")
            stderr.flush()
            exit(1)

        # Get packages from bin folder that are hitch related
        python_bin = path.join(hitchdir.get_hitch_directory(), "virtualenv", "bin", "python")
        packages = [
            package.replace("hitch", "") for package in listdir(
                path.join(hitchdir.get_hitch_directory(), "virtualenv", "bin")
            )
            if package.startswith("hitch") and package != "hitch"
        ]

        # Add packages that start with hitch* to the list of commands available
        for package in packages:
            cmd = copy.deepcopy(runpackage)
            cmd.name = package
            try:
                description = check_output([
                    python_bin, '-c',
                    'import sys;sys.stdout.write(__import__("hitch{}").commandline.cli.help)'.format(
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
        cli.add_command(clean)
        cli.add_command(freeze)
        cli.add_command(init)
        cli.help = "Hitch test runner for:\n\n  {0}.".format(hitchdir.get_hitch_directory())
    else:
        cli.add_command(init)
        cli.add_command(clean)
        cli.help = "Hitch bootstrapper - '.hitch' directory not detected here."
    cli()

if __name__ == '__main__':
    run()
