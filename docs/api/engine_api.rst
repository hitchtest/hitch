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


For a test like this:

.. code-block:: yaml

    - name: Example scenario
      scenario:
        - Do something
        - Do something else


Step Translation
----------------

Test steps and their arguments are fed to the engine directly as method calls
and arguments. All step names and arguments are first changed into underscore_case.

For example, putting this as a test step:

.. code-block:: yaml

  - Do something

Would be equivalent to calling this in your engine:

.. code-block:: python

  self.do_something()

This, on the other hand (note the semicolon):

.. code-block:: yaml

  - Do something else: value 1

Would be translated into:

.. code-block:: python

  self.do_something_else("value 1")

You can include as many arguments as you like in steps like so:

.. code-block:: yaml

  - Do complicated thing:
      Variable 1: Value 1
      Variable 2: 2

If the equivalent were written in python it would look like this:

.. code-block:: python

  self.do_complicated_thing(variable_1="Value 1", variable_2="2")

Your steps can also contain arguments that contain lists:

.. code-block:: yaml

  - Do another complicated thing:
      Variable 1: value 1
      Variable 2:
        - List item 1
        - List item 2

The python equivalent of that would look like this:

.. code-block:: python

  self.do_another_complicated_thing(variable_1="value 1", variable_2=["list item 1", "list item 2",])

They can contain dicts (or associative arrays) as well:

.. code-block:: yaml

  - A 3rd complicated thing:
      Variable 1: value 1
      Variable 2:
        Dict item 1: val 1
        Dict item 2: val 2

Which in python would be equivalent to this:

.. code-block:: python

  self.a_3rd_complicated_thing(variable_1="value 1", variable_2={'Dict item 1': 'val 1', 'Dict item 2': 'val 2'})


Careful with semicolons and braces like { and }
-----------------------------------------------

Since the tests are written in YAML with optional Jinja2, braces and
semicolons have special meanings and must be escaped if you want
to use them.


Preconditions
-------------

self.preconditions is a dictionary representation of the YAML snippet in the test being run.
What goes in this snippet is up to you. Anything that is valid YAML is allowed.

Example:

.. code-block:: yaml

    preconditions:
      db_fixtures:
        - fixture1.sql
      python_version: 2.7.3

This will mean your preconditions variable will be::

    In [1]: self.preconditions
    Out[1]: {'db_fixtures': ['fixture1.sql'], 'python_version': '2.7.3'}

You can access any properties you set here using python's get method (which
you can also use to program in a sensible default)::

    In [1]: self.preconditions.get('db_fixtures', [])
    Out[1]: ['fixture1.sql']

If no preconditions are set, self.preconditions will be an empty dict::

    In [1]: self.preconditions
    Out[1]: {}

Note that while preconditions can contain lists, you can't set preconditions
to be a list.

Tags
----

Tests can also have tags, which let you single out individual tests to run
or to run groups of tests together. Example:

.. code-block:: yaml

  - name: Test with tags
    tags:
      - registration
      - email
      - firefox
    scenario:
      - Step 1
      - Step 2

You can use these tags to run related sets of tests together like so::

  $ hitch test . --tags registration

Or, if you want to be more specific, you can list the tags, separated by a comma::

  $ hitch test . --tags registration,email,firefox


Description
-----------

You can also include comments in the description property. This where you can
put comments in your tests to help explain to people what your test is doing
and why.

It is ignored by the engine.

.. code-block:: yaml

  - name: Test with long description
    description: |
      This test has a long history behind it. First there was a feature, then
      ther was another bug BUG-431, which it was tweaked to accomodate.

      It registers, recieves an email and checks the email arrived.
    scenario:
      - Step 1
      - Step 2: with parameter
      - Step 3:
          var 1: 1
          var 2: 2
          var 3: 3
      - Last step


Stacktrace
----------

self.stacktrace is an object representation of the stack trace that occurs after a failure
occurs in your test. It is set to None if no error has occurred while running the test.

You can use it to pretty-print a representation of the last error that occurred::

    In [1]: print(self.stacktrace.to_template())
    [ prints colorized, pretty printed version of the stacktrace ]

You can also use it to *dive into* the specific engine code where the exception occurred,
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
