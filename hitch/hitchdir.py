import os
from sys import stderr, exit

DOTDIR = ".hitch"

def _check_for_directory():
    checkdirectory = os.getcwd()
    directories_checked = []
    hitch_directory = None

    while not os.path.ismount(checkdirectory):
        directories_checked.append(checkdirectory)
        if os.path.exists(os.path.join(checkdirectory, DOTDIR)):
            hitch_directory = os.path.join(checkdirectory, DOTDIR)
            break
        else:
            checkdirectory = os.path.abspath(os.path.join(checkdirectory, os.pardir))

    return hitch_directory, directories_checked

def hitch_exists_here():
    return os.path.exists(DOTDIR)

def hitch_exists():
    directory, _ = _check_for_directory()
    return directory is not None

def get_hitch_directory_or_fail():
    directory, directories_checked = _check_for_directory()
    if not directory:
        stderr.write("Hitch has not been initialized in this directory, or any of the directories beneath it:\n")
        stderr.write('\n'.join(directories_checked))
        stderr.flush()
        exit(1)
    return directory

def get_hitch_directory():
    """Get the full path of the hitch directory."""
    directory, _ = _check_for_directory()
    return directory
