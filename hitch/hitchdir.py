from os.path import exists, join, ismount, abspath, pardir
from hitch import languagestrings
from sys import stderr, exit
import shutil
import os


DOTDIR = ".hitch"


def _check_for_directory():
    checkdirectory = os.getcwd()
    directories_checked = []
    hitch_directory = None

    while not ismount(checkdirectory):
        directories_checked.append(checkdirectory)
        if exists(join(checkdirectory, DOTDIR)):
            hitch_directory = join(checkdirectory, DOTDIR)
            break
        else:
            checkdirectory = abspath(join(checkdirectory, os.pardir))

    return hitch_directory, directories_checked

def hitch_exists_here():
    return exists(DOTDIR)

def hitch_exists():
    directory, _ = _check_for_directory()
    return directory is not None

def get_hitch_directory_or_fail():
    directory, directories_checked = _check_for_directory()
    if not directory:
        stderr.write(languagestrings.HITCH_NOT_INITIALIZED)
        stderr.write('\n'.join(directories_checked))
        stderr.flush()
        exit(1)
    return directory

def remove_hitch_directory_if_exists():
    directory, _ = _check_for_directory()
    if directory is not None:
        shutil.rmtree(directory)

def check_hitch_directory_integrity():
    directory, _ = _check_for_directory()
    if exists(join(directory, "absdir")):
        with open(join(directory, "absdir"), "r") as absdir_handle:
            absdir = absdir_handle.read()
        if directory != absdir:
            stderr.write(languagestrings.HITCH_DIRECTORY_MOVED.format(
                directory, abspath(join(directory, os.pardir))
            ))
            stderr.flush()
            exit(1)
    if not exists(join(get_hitch_directory(), "virtualenv", "bin")):
        stderr.write(languagestrings.SOMETHING_CORRUPTED)
        stderr.flush()
        exit(1)

def get_hitch_directory():
    """Get the full path of the hitch directory."""
    directory, _ = _check_for_directory()
    return directory
