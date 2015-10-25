Getting started quickly with Hitch
==================================

This is a basic introduction to getting your first hitch test up and running.

Install prerequisites
---------------------

You should have a reasonably up to date Ubuntu, Debian, Arch, Fedora or Mac.

On Ubuntu/Debian::

    $ sudo apt-get install python3 python-pip python-virtualenv
    $ sudo pip install --upgrade hitch

On Mac OS X::

    $ brew install python python3
    $ pip install --upgrade hitch virtualenv

On Arch::

    $ sudo pacman -Sy python python-virtualenv
    $ sudo pip install --upgrade hitch

On Fedora/RHEL/CentOS::

    $ sudo yum install python3 python-virtualenv python-pip python3
    $ sudo pip install --upgrade hitch

.. note::

    The 'hitch' package (the bootstrapper) is a small python package with no dependencies.


Create your test directory
--------------------------

Create a directory inside the root of your project to put your tests in. For example::

  ~/yourproject$ mkdir tests
  ~/yourproject$ cd tests
  ~/yourproject/tests$

If you already have a tests directory you can call it something else.


Create the hitch environment
----------------------------

To initialize a hitch environment, run hitch init in your tests directory::

  ~/yourproject/tests$ hitch init

This will:

* Install any necessary system packages required to run hitch.
* Create a .hitch directory, create a python 3 virtualenv in it and install all the necessary packages to run hitch tests there.
* Ask you some basic questions about the project which you are testing.
* Create a skeleton hitch project template for you to use based upon the answers.

The skeleton template will include all of the following:

* :doc:`/glossary/hitchreqs.txt`
* :doc:`/glossary/engine.py`
* tdd.settings (:doc:`/glossary/hitch_settings`)
* ci.settings
* all.settings
* :doc:`/glossary/stub.test`
* README.rst

You might want to take a look around these files. They all try to be self-explanatory.


Running your first test
-----------------------

You can now run the stub test. Try running it in test driven development mode::

  $ hitch test stub.test --settings tdd.settings

The first time you run this command it *may take a while* (up to 25 minutes depending upon what you answered).

.. note::

    :doc:`/faq/why_does_the_first_test_run_take_so_long`

This might be a good time to take a break.

While you're at it, subscribe to the `hitch subreddit <https://reddit.com/r/hitchtest>`_ and
`twitter feed <https://twitter.com/testhitch>`_ for updates and news.



Back?
-----

.. note::

    If the stub test failed, please `raise an issue <https://github.com/hitchtest/hitch/issues/new>`_.

Once the test run is done setting up, if there were no problems, you should see this::

    Python 3.4.3 (default, Jul 28 2015, 18:20:59)
    Type "copyright", "credits" or "license" for more information.

    IPython 4.0.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.


    SUCCESS

    In [1]:

This is the interactive prompt that appears during the pause step. This is an :doc:`/glossary/ipython`
prompt that can be used to interact with your app, inspect logs and try out test
steps.

The components you selected during the set up should also be running. For example, if you
chose postgres, the latest version of postgres will have been installed in the ~/.hitchpkg
directory and it will be running and accessible.

To exit, simply hit ctrl-D.

This will shut everything down and then quit.

You're now ready to start writing new tests.

Happy testing!

.. note::

    Was there anything that went wrong or was confusing? Please tell us! Help with :doc:`/misc/clarifying_documentation`.


Further reading
---------------

* :doc:`/howto/web_applications`
* :doc:`/howto/command_line_applications`

Advanced topics
---------------

* :doc:`/howto/test_driven_development`
* :doc:`/howto/parameterize_test_cases`
* :doc:`/howto/external_apis`
* :doc:`/howto/continuous_integration`

Plugin Documentation
--------------------

.. toctree::
   :glob:
   :maxdepth: 1

   /plugins/*


.. note::

    Need tutorials for any other topics? `Please raise a ticket <https://github.com/hitchtest/hitch/issues/new>`_.
