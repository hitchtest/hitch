Hitch Engine API
================

The Hitch Engine is a python class which is tasked with executing your tests
and responding to successes and failures.

The basic Hitch Engine looks something like this:

.. code-block:: python

    import hitchtest

    class ExecutionEngine(hitchtest.ExecutionEngine):
        def set_up(self):
            # set up code

        def do_something(self):
            # code run when test says "Do something"

        def do_something_else(self, with_what):
            # code run run when test says "Do something else"

        def tear_down(self):
            # code that always runs at the end


Step Translation
----------------

Test steps and their properties are fed to the engine directly as method calls
and arguments. All step names and properties are first changed into underscore_case.

Example 2 (without variables):

.. code-block:: yaml

  - Do something

Is translated into the following method call:

.. code-block:: python

  self.do_something()

Example 2 (with a single variable):

.. code-block:: yaml

  - Do something else: value 1

Is translated into the following method call:

.. code-block:: python

  self.do_something_else("value 1")

Example 3 (with more than one variable):

.. code-block:: yaml

  - Do complicated thing:
      Variable 1: Value 1
      Variable 2: 2

Is translated into the following method call:

.. code-block:: python

  self.do_complicated_thing(variable_1="Value 1", variable_2="2")

Example 4 (with a variable that contains a list):

.. code-block:: yaml

  - Do another complicated thing:
      Variable 1: value 1
      Variable 2:
        - List item 1
        - List item 2

Is translated into the following method call:

.. code-block:: python

  self.do_another_complicated_thing(variable_1="value 1", variable_2=["list item 1", "list item 2",])

Example 5 (with a variable that contains a dict):

.. code-block:: yaml

  - A 3rd complicated thing:
      Variable 1: value 1
      Variable 2:
        Dict item 1: val 1
        Dict item 2: val 2

Is translated into the following method call:

.. code-block:: python

  self.a_3rd_complicated_thing(variable_1="value 1", variable_2={'Dict item 1': 'val 1', 'Dict item 2': 'val 2'})


Careful with semicolons and braces like { and }
-----------------------------------------------

Since the tests are written in YAML with optional Jinja2, braces and
semicolons have special meanings.


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

This will mean your preconditions variable is::

    In [1]: self.preconditions
    Out[1]: {'db_fixtures': ['fixture1.sql'], 'python_version': '2.7.3'}

If no preconditions are set, it will set to be an empty dict::

    In [1]: self.preconditions
    Out[1]: {}

You can access any properties you set here using python's get method, which
you can also use to program in a sensible default::

    In [1]: self.preconditions.get('db_fixtures', [])
    Out[1]: ['fixture1.sql']

Note that while preconditions can contain lists, you can't set preconditions
to be a list.

Tags
----

Tests can also have tags, which let you single out individual tests to run
or to run individual tests together:

  - name: Test with tags
    tags:
      - registration
      - email
      - firefox
    scenario:
      - Step 1
      - Step 2

You can use these to run related sets of tests together like so::

  $ hitch test . --tags registration

Or, if you want to be more specific, you can list the tags, separated by a comma::

  $ hitch test . --tags registration,email,firefox


Description
-----------

You can also include comments in the description property. This is to help people
understand what the test is doing and why.

It is ignored by the engine.

.. code-block:: yaml

  - name: Test with long description
    description: |
      This test has a long history behind it. First there was a feature, then
      ther was another bug BUG-431, which it was tweaked to accomodate.

      It registers, recieves an email and checks the email arrived.
    scenario:
      - Step 1
      - Step 2
      db_fixtures:
        - fixture1.sql


Stacktrace
----------

self.stacktrace is an object representation of the stack trace that occurred
after an exception occurred. It is set to None if no error has occurred while
running the test.

You can use it to pretty-print a representation of the last error that occurred::

    In [1]: print(self.stacktrace.to_template())
    [ prints colorized, pretty printed version of the stacktrace ]

You can also use it to *dive into* the specific code where the exception occurred,
so that you can check the contents of variables at that point or even re-run the code::

    In [1]: self.stacktrace[0].ipython()
    Entering /home/user/django-remindme/django-remindme-tests/engine.py at line 122

    In [1]: on
    Out[1]: 'register'


Settings
--------

Test settings are also available in the test engine, e.g.::

    In [1]: self.settings
    Out[1]:
    {'engine_folder': '/home/user/django-remindme/django-remindme-tests',
     'pause_on_failure': True,
     'python_version': '2.7.3',
     'xvfb': False,
     'quiet': False}

To read more about setting settings see :doc:`settings`.
