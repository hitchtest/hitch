

SPECIFY_PYTHON_TO_CREATE_VIRTUALENV_WITH = """\
Create hitch virtualenv using specific python version
(e.g. /usr/bin/python3). Defaults to using python3 on the system path."""

SPECIFY_VIRTUALENV_TO_CREATE_HITCH_WITH = """\
Create hitch virtualenv using specific virtualenv
(e.g. /usr/bin/virtualenv). Defaults to using virtualenv on the system path."""

YOU_MUST_HAVE_VIRTUALENV_INSTALLED = """\
You must have virtualenv installed to use hitch.
"""

YOU_MUST_HAVE_PYTHON3_INSTALLED = """\
To use Hitch, you must have python 3 installed on your system
and available. If your python3 is not on the system path with
the name python3, specify its exact location using --python.
"""

YOU_MUST_HAVE_VERSION_ABOVE_PYTHON33 = """\
Hitch must have python 3.3 or higher installed to run.
Your app can run with earlier versions of python, but the tests can't.
"""

HITCH_ALREADY_INITIALIZED = """\
Hitch has already been initialized in this directory or a directory above it.
If you wish to re-initialize hitch in this directory, run 'hitch clean' first.
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
