"""Command line interface to hitch."""
from click import command, group, argument, option
from subprocess import call, check_output, PIPE
from os import path, makedirs
from sys import stderr, exit
import hitchdir
import shutil
import signal

@group()
def cli():
    """Hitch bootstrapper and test runner."""
    pass

@command()
def init():
    """Initialize hitch in this directory."""
    if call(["which", "virtualenv"], stdout=PIPE):
        stderr.write("You must have python-virtualenv installed to use hitch.\n")
        stderr.flush()
        exit(1)

    if hitchdir.hitch_exists():
        stderr.write("Hitch has already been initialized in this directory.\n")
        stderr.flush()
        exit(1)

    makedirs(".hitch")
    pip = path.abspath(path.join(".hitch", "virtualenv", "bin", "pip"))

    call(["virtualenv", ".hitch/virtualenv", "--no-site-packages"])
    call([pip, "install", "-U", "pip"])

    if path.exists("hitchreqs.txt"):
        call([pip, "install", "-r", "hitchreqs.txt"])
    else:
        call([pip, "install", "hitch"])
        call([pip, "install", "hitchserve"])

        pip_freeze = check_output([pip, "freeze"])

        with open("hitchreqs.txt", "w") as hitchreqs_handle:
            hitchreqs_handle.write(pip_freeze)


@command()
@argument('filename')
@option('-r', '--repeat', default=1, help='Number of times to run the test. Report % success and failure.')
@option('-s', '--settings', default=None, help="Load settings from file.")
@option('-e', '--extra', default=None, help="""Load extra vars on command line as JSON (e.g. --extra '{"postgres_version": "3.5.5"}'""")
def test(filename, repeat, settings, extra):
    """Run test"""
    if filename.endswith(".yml") and path.exists(filename):
        python = path.join(hitchdir.get_hitch_directory(), "virtualenv", "bin", "test")
        command = [python, path.abspath(filename), '-r', str(repeat), ]
        if settings is not None:
            command = command + ['--settings', settings, ]
        if extra is not None:
            command = command + ['--extra', extra, ]
        return_code = call(command)
        exit(return_code)
    else:
        stderr.write("I didn't understand {}\n".format(filename))
        stderr.flush()
        exit(1)


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
    """Clean out all hitch data and set up from scratch."""
    run_checks()
    shutil.rmtree(".hitch")
    up()


def run():
    """Run hitch bootstrap CLI"""
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    signal.signal(signal.SIGTERM, signal.SIG_IGN)

    cli.add_command(init)
    cli.add_command(install)
    cli.add_command(uninstall)
    cli.add_command(test)
    cli.add_command(clean)
    cli.add_command(freeze)
    cli()

if __name__ == '__main__':
    run()
