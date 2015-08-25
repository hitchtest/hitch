1: Creating a skeleton test
===========================

This is a basic introduction to getting your first skeleton test up and running.

Prerequisites
-------------

To begin, make sure you have a reasonably up to date system (no more than two years old) and
install the following packages:

.. note::

    Your application can still be tested using python 2. Read on to find out more.

On Ubuntu::

  $ sudo apt-get install python3 python-virtualenv python-dev python-pip build-essential

On Red Hat/Fedora::

  $ sudo yum install python3 python-setuptools python-devel python-pip python-virtualenv automake libtool patch gcc

On Arch::

  $ sudo pacman -S python3 python-setuptools python-pip python-virtualenv base-devel

On a Mac::

  $ brew install python3

  $ pip install -U setuptools pip virtualenv


Make sure that you have the correct version(s) of python 3 installed::

  $ python3 -V
  Python 3.4.3

It should be python 3.3 or above.

Install
-------

The first thing that you need to install after this is the hitch bootstrap
script::

  $ pip install -U hitch

or::

  $ sudo pip install -U hitch

You can install this in a virtualenv if you wish, but it's more
convenient to install it with your system python.

.. note::

    :doc:`/faq/why_install_hitch_on_the_system_path`


Create your test directory
--------------------------

Next, create a directory inside your project to put your tests in. For example::

  $ mkdir tests
  $ cd tests

Inside this, directory, run the following command to initialize hitch::

  $ hitch init

This will create a file called hitchreqs.txt, which contains a list of
pypi requirements to use in the hitch virtualenv. These are the packages
required to run your *testing* code - there is no need to add packages
here which your application needs to run. It will run in its own segregated
virtualenv.

The .hitch directory contains all the necessary generated files
required to run your tests, including the testing virtualenv.

The .hitch directory should be gitignored. If you delete it, you can
regenerate it just by running hitch init again.

Create your first test and engine
---------------------------------

To run your first test, you need an engine. An engine file simply contains
a class with a lot of methods that your tests can invoke.

Create an engine called 'engine.py' like so::

    import hitchtest
    from os import path

    PROJECT_DIRECTORY = path.abspath(path.join(path.dirname(__file__), '..'))

    class ExecutionEngine(hitchtest.ExecutionEngine):
        def set_up(self):
            pass

        def pause(self):
            hitchtest.ipython_embed()

        def tear_down(self):
            pass

And a test called 'stub.test', written in YAML, like so:

.. code-block:: yaml

  - name: Stub
    scenario:
      - Pause

You can run this test by running the command inside your tests directory::

  $ hitch test stub.test

And voila, you should see an IPython prompt.

It runs "set_up", followed by "pause" (as specified in the scenario), which
enters IPython and finally runs "tear_down".

You can exit the IPython prompt by typing ctrl-D.

Now that you have the skeleton of a test, you can continue building the
other necessary parts of your testing infrastructure.
