2: Creating test settings and test preconditions
================================================

Note: it's recommended that you gain a familiarity with :doc:`/glossary/YAML`.

.. note::

    :doc:`/faq/why_yaml`

Now that you have a skeleton test, but you need to be able to configure
it properly to be able to get it to do useful things in your tests.

Settings
--------

First, create a file called settings.yml and put in this one line::

  python_version: 2.7.9

This is a basic YAML file.

This file is read automatically by your tests and the values can be
inserted directly into your test by your engine, like so::

  In [1]: self.settings['python_version']
  Out[1]: '2.7.9'

Since it is YAML, this file can store lists, dicts, lists of dicts
and dicts of lists, strings and numbers.

What goes in it and how it is structured is entirely up to you.

It's the best place to put settings that will be used by
all of your tests.

Preconditions
-------------

Now take a look at your test::

  - name: Stub
    engine: engine.py:YourProjectTestExecutionEngine
    scenario:
      - Pause

You can add a preconditions value::

  - name: Stub
    preconditions:
      precondition1: value1
      precondition2: 100
    engine: engine.py:YourProjectTestExecutionEngine
    scenario:
      - Pause

These values are available to you when you run the test::

   In [1]: self.preconditions
   Out[1]: {'precondition1': 'value1', 'precondition2': 100}

What goes in here is basically settings used for *individual*
tests. The exact contents and structure are left up to you.

It could be databse fixtures filenames, specific versions
of software or even different configurations of services.

Again, like the settings file, this is just YAML, so your
preconditions can be nothing at all, a dict, a list and
contain strings, numbers and other dicts and lists.
