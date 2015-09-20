1: Creating a skeleton test
===========================

This is a basic introduction to getting your first skeleton test up and running.

Create your test directory
--------------------------

Next, create a directory inside your project to put your tests in. For example::

  $ mkdir tests
  $ cd tests

Inside this, directory, run the following command to download, install and
initialize hitch in this directory::

  $ curl -sSL https://hitchtest.com/init.sh > init.sh ; chmod +x init.sh ; ./init.sh

See also:

* :doc:`/faq/what_does_the_init_script_do`

Create your first test and engine
---------------------------------

To run your first test, you need an engine file. An engine file simply contains
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


Then, create test called 'stub.test', written in YAML, like so:

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
