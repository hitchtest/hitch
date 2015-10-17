Getting started quickly with Hitch
==================================

This is a basic introduction to getting your first hitch test up and running.

Create your test directory
--------------------------

Create a directory inside the root of your project to put your tests in. For example::

  ~/yourproject$ mkdir tests
  ~/yourproject$ cd tests
  ~/yourproject/tests$

If you already have a tests directory you can call it something else.


Create the hitch environment
----------------------------

If you have hitch installed already, run the following command::

  ~/yourproject/tests$ hitch init

If you don't, run the init script by copying and pasting the following line::

  ~/yourproject/tests$ curl -sSL https://hitchtest.com/init.sh > init.sh ; chmod +x init.sh ; ./init.sh

.. note::

    This can be used as a guide to instal hitch instead: :doc:`/faq/what_does_the_init_script_do`

Once the installation has completed, it will ask you a few basic questions about your project,
mostly requiring a yes or no answer and will then generate a skeleton project template for you.

Apart from installing all of the required packages and creating a .hitch directory,
the following files are created in your tests directory:

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

The first time you run this command it may take a while (up to 25 minutes depending upon what you configured).

Time for coffee?

While you're at it, check out the hitch subreddit and subscribe to the twitter feed!

.. note::

    :doc:`/faq/why_does_the_first_test_run_take_so_long`


Back?
-----

Once the test run is done setting up and running things, if there were no problems, you should see this::

    Python 3.4.3 (default, Jul 28 2015, 18:20:59)
    Type "copyright", "credits" or "license" for more information.

    IPython 4.0.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.


    SUCCESS

    In [1]:

This is the interactive prompt that appears during the pause step. This is an :doc:`glossary/ipython`
prompt that can be used to interact with your app, inspect logs and try out test
steps.

The components you selected during the set up should also be running. For example, if you
chose postgres, postgres will be running.

To exit, simply hit ctrl-D.

This will shut everything down and then quit.

You're now ready to start writing new tests.

Happy testing!

.. note::

    Was there anything that confused you? Please tell us! Help with :doc:`misc/clarifying_documentation`.


Further reading
---------------

* :doc:`/howto/web_applications`
* :doc:`/howto/command_line_applications`

Advanced topics
---------------

* :doc:`/howto/test_driven_development`
* :doc:`/howto/parameterize_test_cases`
* :doc:`/howto/continuous_integration`

.. note::

    Need tutorials for any other topics? `Please raise a ticket <https://github.com/hitchtest/hitch/issues/new>`_.
