What does the init script do?
=============================

The init script is a one step method of setting up a hitch environment and running
all the tests in a directory. It is intended to be a low friction way of getting a
development and testing environment up and running.

If you'd prefer instead to perform the steps manually, you can use this as a guide.


1. Installs python, pip, virtualenv, python-dev, automake and libtool (requires sudo)
-------------------------------------------------------------------------------------

On Ubuntu/Debian::

  $ sudo apt-get install -y python python3 python-dev python-setuptools python-virtualenv python3-dev automake libtool

On Fedora/Red Hat/CentOS::

  $ yum -y install python python-devel python-setuptools python-virtualenv python-pip python3 python3-devel automake libtool gcc-c++

On Arch::

  $ pacman -Sy python python-setuptools python-virtualenv python automake libtool

On Mac OS X::

  $ brew install python python3 libtool automake cmake

  $ pip install --upgrade pip setuptools virtualenv


2. Install or upgrades the hitch bootstrap script (may require sudo)
--------------------------------------------------------------------

On the Mac it will run::

  $ pip install --upgrade hitch

Or on Linux::

  $ sudo pip install --upgrade hitch

This is a small python script with zero dependencies.

See also:

* :doc:`/faq/what_does_the_hitch_bootstrap_script_do`


3. Runs "hitch clean" and "hitch init" in the current directory (does not require sudo)
---------------------------------------------------------------------------------------

If no hitch environment is already installed then this command does nothing. If a .hitch
directory *is* found, it will remove it::

  $ hitch clean

This creates a .hitch directory in the current directory, where all of the
packages required to run tests will be installed in a python virtualenv::

  $ hitch init


* :doc:`/faq/what_does_hitch_init_do`


4. Run "hitch test ." if tests are found (may require sudo)
-----------------------------------------------------------

If there are tests in the directory where the init script is run, hitch will run all
of them.

During the course of running the tests, the test may attempt to use sudo to install
necessary packages. It will always print the exact command it is trying to run
(e.g. sudo apt-get install xvfb).

If the packages are already installed, hitch will not attempt to install them.

See also:

* :doc:`why_does_my_test_require_me_to_sudo_and_install_packages`

During the course of running the tests it will also attempt to download and compile
certain pieces of software (e.g. postgres). The software will be installed in the
"~/.hitchpkg" directory. Doing this does not require root and it will not interfere
at all with other software you may have installed.

See also:

* :doc:`why_is_my_test_downloading_and_compiling_software`
* :doc:`why_does_the_first_test_run_take_so_long`

All software installed there can be easily removed by deleting the "~/.hitchpkg"
directory or running the command "hitch cleanpkg". If a test does not detect its
presence it will download and compile it again.

See also:

* :doc:`how_do_i_uninstall_hitch_completely`
