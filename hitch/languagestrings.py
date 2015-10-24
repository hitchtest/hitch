

SPECIFY_PYTHON_TO_CREATE_VIRTUALENV_WITH = """\
Create hitch virtualenv using specific python version
(e.g. /usr/bin/python3). Defaults to using python3 on the system path."""

SPECIFY_VIRTUALENV_TO_CREATE_HITCH_WITH = """\
Create hitch virtualenv using specific virtualenv
(e.g. /usr/bin/virtualenv). Defaults to using virtualenv on the system path."""

YOU_MUST_HAVE_VIRTUALENV_INSTALLED = """\
You must have virtualenv installed to use hitch.

Suggestions:

#1 Install via your system's package manager:
  - On Ubuntu/Debian : sudo apt-get install python-virtualenv
  - On Fedora        : sudo yum install python-virtualenv
  - On Arch          : sudo pacman -Sy python-virtualenv
  - On Mac OS X      : pip install --upgrade virtualenv

#2 Install via pip, e.g.:
  - sudo pip3 install --upgrade virtualenv
"""

YOU_MUST_HAVE_PYTHON3_INSTALLED = """\
To use Hitch, you must have python 3 installed.

To install:
  - On Ubuntu/Debian : sudo apt-get install python3
  - On Fedora        : sudo yum install python3
  - On Arch          : sudo pacman -Sy python3
  - On Mac OS X      : brew install python3

If your python3 is *not* on the system path with the name 'python3',
you can specify the location of its virtualenv executable like so:

hitch init --virtualenv=/path/to/python3/bin/virtualenv

Or specify the location of the python3 interpreter, e.g.

hitch init --python=/path/to/python3/bin/python3
"""

YOU_MUST_HAVE_VERSION_ABOVE_PYTHON33 = """\
Hitch must have python 3.3 or higher installed to run.
Your app can run with earlier versions of python, but the
testing environment cannot.

Suggestions:

#1 You may need to run a sytem upgrade or upgrade your OS.

#2 If you have python 3.3+ installed but it is not accessible
on the system path with the command 'python3', you can run:

hitch init --virtualenv=/path/to/python3/bin/virtualenv

OR

hitch init --python=/path/to/python3/bin/python3
"""

ERROR_INITIALIZING_HITCH = """\
\nError initializing hitch. Problem checklist:\n
* Was there a problem with your internet?
* Was there a python package being installed that couldn't compile?\n

Try searching for any errors printed above or raising an issue at:
http://github.com/hitchtest/hitch/issues/
"""

HITCH_DIRECTORY_MOVED = """\
The hitch directory '{0}' was moved.
"Run 'hitch clean' then run 'hitch init' in this directory:
==> {1}
"""

HITCH_NOT_INITIALIZED = """\
Hitch has not been initialized in this directory, or any of the directories beneath it:\n"""

SOMETHING_CORRUPTED = """\
WARNING: Hitch directory was corrupted. Run 'hitch clean' and hitch init again.\n
"""

UPDATING_REQUIREMENTS = """\
Updating installed packages to bring them in alignment with the contents of hitchreqs.txt\n"""
