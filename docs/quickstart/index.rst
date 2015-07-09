Hitch Quickstart
================

This is a basic introduction to getting your first test up and running.

Prerequisites
-------------

To begin, the minimum you need to have python3 and virtualenv installed on your system.

On Ubuntu::

  $ sudo apt-get install python3 python-virtualenv

On a Mac::

  $ brew install python3

  $ pip install -U setuptools pip virtualenv

Install
-------

The first thing that you need to install after this is the hitch bootstrap
script::

  $ pip install hitch

or::

  $ sudo pip install hitch


See :doc:`faq/why_install_hitch_on_the_system_path`.


Create your test directory
--------------------------

First create a directory inside your project to put your tests in. For example::

  $ mkdir tests
  $ cd tests

Inside this, directory, run the following command to initialize hitch.

  $ hitch init

This will create a file called hitchreqs.txt, which contains a list of
pypi requirements to use in the hitch virtualenv. These are the packages
required to run your *testing* code - there is no need to add packages
here which your application needs to run. It will run in its own segregated
virtualenv.

The .hitch directory contains all the necessary generated files
required to run your tests, including the testing virtualenv.

This directory should be gitignored. If you delete it, you can regenerate
it just by running hitch init again.

Create your first test and engine
---------------------------------

To run your first test, you need an engine. An engine file simply contains
a class with a lot of methods that your tests can invoke.

Create an engine called 'engine.py' like so::

    import hitchtest
    from os import path

    PROJECT_DIRECTORY = path.abspath(path.join(path.dirname(__file__), '..'))

    class YourProjectTestExecutionEngine(hitchtest.ExecutionEngine):
        def set_up(self):
            pass

        def pause(self):
            hitchtest.ipython_embed()

        def tear_down(self):
            pass

And a test called 'stub.test', written in YAML, like so::

  - name: Stub
    engine: engine.py:YourProjectTestExecutionEngine
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


Contents:

.. toctree::
   :glob:
   :maxdepth: 2

   *
