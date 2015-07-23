Hitch Engine API
================

Each test must specify an engine that drives it, along with a unique name and scenario:

.. code-block:: yaml

  - name: Stub
    engine: engine.py:YourProjectTestExecutionEngine
    scenario:
      - Pause

The engine property specifies the filename that contains the execution engine, followed
by a colon, followed by the class name of the execution engine.

The Hitch Engine is the python code, written by the user, which drives a test. It has four
special methods:

.. code-block:: python

    import hitchtest

    class YourProjectTestExecutionEngine(hitchtest.ExecutionEngine):
        def set_up(self):
            pass

        def on_success(self):
            pass

        def on_failure(self):
            pass

        def tear_down(self):
            pass

When a test (any test) is run, set_up is always run first.

Next, methods corresponding to the steps specified in tests are called (see below).

If all of the steps complete successfully without exceptions, the on_success
method is called, followed by the tear_down method.

If any of the steps fails, the on_failure method is called, followed by the tear_down.

Test Steps
----------

Test steps and their properties are fed to the engine directly as method calls
and arguments. All step names and properties are first changed into underscore_case.

Example 2 (without variables):

.. code-block:: yaml

  - Step 1

Is translated into the following method call:

.. code-block:: python

  self.step_1()

Example 2 (with a single variable):

.. code-block:: yaml

  - Step 2: value 1

Is translated into the following method call:

.. code-block:: python

  self.step_2("value 1")

Example 3 (with more than one variable):

.. code-block:: yaml

  - Step 3:
      Variable 1: Value 1
      Variable 2: 2

Is translated into the following method call:

.. code-block:: python

  self.step_3(variable_1="Value 1", variable_2="2")

Example 4 (with a variable that contains a list):

.. code-block:: yaml

  - Step 4:
      Variable 1: value 1
      Variable 2:
        - List item 1
        - List item 2

Is translated into the following method call:

.. code-block:: python

  self.step_4(variable_1="value 1", variable_2=["list item 1", "list item 2",])

Example 5 (with a variable that contains a dict):

.. code-block:: yaml

  - Step 5:
      Variable 1: value 1
      Variable 2:
        Dict item 1: val 1
        Dict item 2: val 2

Is translated into the following method call:

.. code-block:: python

  self.step_5(variable_1="value 1", variable_2={'Dict item 1': 'val 1', 'Dict item 2': 'val 2'})


Settings
--------

self.settings is a dictionary representation of what is in settings.yml and specified by --extra
on the command line. This is where you can put project and environment specific test settings.

Example settings.yml:

.. code-block:: yaml

  python_version: 2.7.3
  pause_on_failure: true

Example command used to run test::

  $ hitch test stub.test --extra '{'custom_var':'1'}'

Example output of settings during test::

  In [1]: self.settings
  Out[1]:
  {'custom_var': 1,
   'engine_folder': '/home/user/django-remindme/django-remindme-tests',
   'pause_on_failure': True,
   'python_version': '2.7.3',
   'quiet': False}



Preconditions
-------------

self.preconditions is a dictionary representation of the YAML snippet in the test being run.
What goes in this variable is up to you. Anything that is valid YAML is allowed.

Example:

.. code-block:: yaml

    preconditions:
      db_fixtures:
        - fixture1.sql
      python_version: 2.7.3

Will be translated into::

    In [1]: self.preconditions
    Out[1]: {'db_fixtures': ['fixture1.sql'], 'python_version': '2.7.3'}


Stacktrace
----------

self.stacktrace is an object representation of the stack trace that occurred
after an exception occurred. It is set to None if no error has occurred while
running the test.

You can use it to pretty print a representation of the last error that occurred::

    In [1]: print(self.stacktrace.to_template())
    [ prints colorized, pretty printed version of the stacktrace ]

You can also use it to dive into the specific code where the exception occurred,
so that you can check the contents of variables at that point or even re-run the code::

    In [1]: self.stacktrace[0].ipython()
    Entering /home/user/django-remindme/django-remindme-tests/engine.py at line 122

    In [1]: on
    Out[1]: 'register'
