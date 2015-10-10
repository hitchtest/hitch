What does the init script do?
=============================

.. note::

    This script tries to respect your existing environment as much as possible and
    avoids the use of sudo except where necessary to install packages via your
    system's package manager.

The init script is a one step method of setting up a hitch environment and running
all the tests in a directory. It is intended to be a low friction way of:

* Getting a CI or test driven development environment up and running.
* Rebuilding an environment from scratch that may have been broken.

If you'd prefer instead to perform the steps manually, you can use this document
as a guide.

Note that the first three steps take about 5 minutes and the last step can take
roughly 15 minutes (or longer, sometimes).


1. Installs python, pip, virtualenv, python-dev, automake and libtool (may require sudo)
----------------------------------------------------------------------------------------

Takes approximately: 1 minute

These packages are required for hitch to initialize.

On Ubuntu/Debian::

  $ sudo apt-get install -y python python3 python-dev python-setuptools python-virtualenv python3-dev automake libtool

On Fedora/Red Hat/CentOS::

  $ sudo yum -y install python python-devel python-setuptools python-virtualenv python-pip python3 python3-devel automake libtool gcc-c++

On Arch::

  $ sudo pacman -Sy python python-setuptools python-virtualenv python automake libtool

On Mac OS X::

  $ brew install python python3 libtool automake cmake

  $ pip install --upgrade pip setuptools virtualenv


2. Install or upgrades the hitch bootstrap script (may require sudo)
--------------------------------------------------------------------

Takes approximately: 5 seconds

This is a small python script with no dependencies that bootstraps your testing
environment and lets you trigger test runs. It installs a single command ('hitch')
on your system's path.

On the Mac the init script will run::

  $ pip install --upgrade hitch

On Linux::

  $ sudo pip install --upgrade hitch

See also:

* :doc:`/faq/what_does_the_hitch_bootstrap_script_do`


3. Runs "hitch clean", "hitch cleanpkg" and "hitch init" in the current directory (may require sudo)
----------------------------------------------------------------------------------------------------

Takes approximately: 2 minutes

If no ".hitch" directory is already installed then this command does nothing. If a .hitch
directory *is* found, it will remove it::

  $ hitch clean

If no "~/.hitchpkg" directory is found, this will also do nothing. If you already used hitch
before you may have packages downloaded into this directory, in which case it will destroy it
so it can be rebuilt::

  $ hitch cleanpkg

This builds a .hitch directory in the current directory and installs any more required
system packages via unixpackage. This asks to install system packages specified in
hitch plugins and packages specified in the system.packages file::

  $ hitch init


* :doc:`/faq/what_does_hitch_init_do`


4. Run "hitch test ." to run all tests (does not require sudo)
--------------------------------------------------------------

Takes approximately: 15 minutes (subsequent test runs will be quicker)

If there are tests in the directory where the init script is run, it will run all
of them.

During the course of running the tests it will attempt to download and compile
certain pieces of software (e.g. postgres). The software will be installed in the
"~/.hitchpkg" directory. This does not require sudo and it will not interfere
with software you may already have installed.

See also:

* :doc:`why_is_my_test_downloading_and_compiling_software`
* :doc:`why_does_the_first_test_run_take_so_long`

All software installed there can easily be removed by deleting the "~/.hitchpkg"
directory or running the command "hitch cleanpkg".

See also:

* :doc:`how_do_i_uninstall_hitch_completely`
