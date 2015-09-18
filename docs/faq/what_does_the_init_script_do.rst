What does the init script do?
=============================

The init script is an easy one step means to set up a hitch environment and run
all the tests in a directory (if there are any). It largely automates the process
of setting up an integration testing / development environment on your Linux
machine or Mac.

The script does the following:


1. Checks for the existence of python, pip and virtualenv on your system
------------------------------------------------------------------------

If they are installed it continues. If they are not, it tries to install them using
the system's package manager (apt-get, yum or pacman).


2. Install the hitch bootstrap script
-------------------------------------

The hitch bootstrap script is a very simple app used to initialize a testing
environment, clean the environment and trigger test runs. It short and has no
other python package dependencies.

It does not require root, but it does need to be on the user's path so it can
be run from any directory.

If pipsi is found, the init script will attempt::

  $ pipsi install --upgrade hitch

If not found, on, the Mac::

  $ pip install --upgrade hitch

Or on Linux::

  $ sudo pip install --upgrade hitch


3. Run hitch init
-----------------

"Hitch init" installs a virtualenv in the current directory using python 3 to run your tests.
It is *not* the virtualenv used to run your code. It is purely for running tests. If you
are using hitch to test a python app, the tests you run in this environment will
set up a separate virtual environment to run your application's code in using the
version(s) of python specified in your test.

Hitch init will install all of the packages listed in the file "hitchreqs.txt". These
are the python packages required to run your testing code only - not your application code.
E.g. the tests used to test django require the "hitchpython" package, but not the "Django"
package.


4. Run "hitch test ." if tests are found
----------------------------------------

If there are tests in the directory where the init script is run, hitch will run all
of them.

See also:

* :doc:`why_does_the_first_test_run_take_so_long`
* :doc:`why_is_my_test_downloading_and_compiling_software`
* :doc:`why_does_my_test_require_me_to_sudo_and_install_packages`
