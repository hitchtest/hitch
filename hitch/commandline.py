"""High level command line interface to hitch."""
from subprocess import call, check_output, PIPE, CalledProcessError
from click import command, group, argument, option
from sys import stderr, exit, modules, argv
from os import path, makedirs, listdir
import hitchdir
import shutil
import signal
import copy


@group()
def cli():
    pass

@command()
def init():
    """Initialize hitch in this directory."""
    if call(["which", "virtualenv"], stdout=PIPE):
        stderr.write("You must have python-virtualenv installed to use hitch.\n")
        stderr.flush()
        exit(1)

    if call(["which", "python3"], stdout=PIPE):
        stderr.write("To use Hitch, you must have python 3 installed and available on the system path with the name 'python3'.\n")
        stderr.flush()
        exit(1)

    python3 = check_output(["which", "python3"]).replace("\n", "")

    if hitchdir.hitch_exists():
        stderr.write("Hitch has already been initialized in this directory.\n")
        stderr.flush()
        exit(1)

    makedirs(".hitch")
    pip = path.abspath(path.join(".hitch", "virtualenv", "bin", "pip"))

    call(["virtualenv", ".hitch/virtualenv", "--no-site-packages", "--distribute", "-p", python3])
    call([pip, "install", "-U", "pip"])

    if path.exists("hitchreqs.txt"):
        call([pip, "install", "-r", "hitchreqs.txt"])
    else:
        call([pip, "install", "hitchtest"])

        pip_freeze = check_output([pip, "freeze"])

        with open("hitchreqs.txt", "w") as hitchreqs_handle:
            hitchreqs_handle.write(pip_freeze)

def update_requirements():
    """Check hitchreqs.txt match what's installed via pip freeze. If not, update."""
    pip = path.join(hitchdir.get_hitch_directory_or_fail(), "virtualenv", "bin", "pip")
    hitchreqs_filename = path.join(hitchdir.get_hitch_directory_or_fail(), "..", "hitchreqs.txt")
    pip_freeze = check_output([pip, "freeze"]).split('\n')
    hitchreqs_handle = ""
    with open(hitchreqs_filename, "r") as hitchreqs_handle:
        hitchreqs = hitchreqs_handle.read().split('\n')

    if not sorted(pip_freeze) == sorted(hitchreqs):
        call([pip, "install", "-r", "hitchreqs.txt"])

    pip_freeze = check_output([pip, "freeze"])

    with open("hitchreqs.txt", "w") as hitchreqs_handle:
        hitchreqs_handle.write(pip_freeze)


@command(context_settings={'help_option_names':[],'ignore_unknown_options':True}, help="dd")
@argument('arguments', nargs=-1)
def runpackage(arguments):
    # Generic method to run any installed app in the virtualenv whose name starts with hitch*
    update_requirements()
    binfile = path.join(hitchdir.get_hitch_directory(), "virtualenv", "bin", "hitch{}".format(argv[1]))
    command = [binfile, ] + argv[2:]
    return_code = call(command)
    exit(return_code)

@command()
@argument('package', required=True)
def uninstall(package):
    """Uninstall hitch package."""
    pip = path.join(hitchdir.get_hitch_directory_or_fail(), "virtualenv", "bin", "pip")

    call([pip, "uninstall", package] )
    pip_freeze = check_output([pip, "freeze"])

    with open("hitchreqs.txt", "w") as hitchreqs_handle:
        hitchreqs_handle.write(pip_freeze)

@command()
@argument('package', required=True)
def install(package):
    """Install hitch package."""
    pip = path.join(hitchdir.get_hitch_directory_or_fail(), "virtualenv", "bin", "pip")

    call([pip, "install", package, "-U", ])
    pip_freeze = check_output([pip, "freeze"])

    with open("hitchreqs.txt", "w") as hitchreqs_handle:
        hitchreqs_handle.write(pip_freeze)

@command()
def freeze():
    """List install hitch packages."""
    pip = path.join(hitchdir.get_hitch_directory_or_fail(), "virtualenv", "bin", "pip")
    call([pip, "freeze", ])

@command()
def clean():
    """Remove the hitch directory entirely."""
    hitch_directory = hitchdir.get_hitch_directory_or_fail()
    shutil.rmtree(".hitch")


def run():
    """Run hitch bootstrap CLI"""
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGTERM, signal.SIG_IGN)

    if hitchdir.hitch_exists():
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
                ], stderr=PIPE)
            except CalledProcessError:
                description = ""
            cmd.help = description
            cmd.short_help = description
            cli.add_command(cmd)


        cli.add_command(install)
        cli.add_command(uninstall)
        cli.add_command(clean)
        cli.add_command(freeze)
        cli.help = "Hitch test runner for:\n\n  {}.".format(hitchdir.get_hitch_directory())
    else:
        cli.add_command(init)
        cli.help = "Hitch bootstrapper - '.hitch' directory not detected here."
    cli()

if __name__ == '__main__':
    run()
