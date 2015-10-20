Settings
========

:doc:`/glossary/hitch_settings` are a set of configuration variables used by
your tests that potentially change test behavior.

Settings are for behaviors for all of your tests that you may want to change
on a case by case basis or a per-environment basis. They are available via:

* self.settings in :doc:`/glossary/engine.py` and the :doc:`/glossary/ipython` console.
* All jinja2 templates

With a few exceptions, what these settings mean and what they do is left up to you.


Changing settings via the from command line
-------------------------------------------

You can set settings via the command line by specifying them
in a snippet of JSON. For example::

  $ hitch test sometests.test --extra '{"failfast":false}'

This will override the default behavior from "stop on on first failure and report" to
"run all tests and report failures at the end".

This variable is accessible in engine.py and via the IPython shell via self.settings, e.g.::

  In [1]: self.settings
  Out[1]:
  {'failfast': False,
   'engine_folder': '/home/user/django-remindme/django-remindme-tests',}

Or::

  In [1]: self.settings.get("failfast")
  Out[1]: False


Per-environment settings
------------------------

Some settings you may want to apply consistently to a certain environment or use case. For example:

* TDD (test driven development environment) - browser is configured to be shown to the developer on all tests.
* CI (continuous integration environment) - browser is configured to run headless on all tests.

Rather than typing all of them in to the command line in JSON, these settings can be set in a YAML file.

Here's an example 'ci.settings' file you might use for a continuous integration environment:

.. code-block:: yaml

  python_version: 2.7.3
  xvfb: true
  failfast: false
  pause_on_failure: false
  pause_on_success: false

You can use the settings from this file by running::

    $ hitch test sometests.test --settings ci.settings

Here, self.settings would be::

  {'engine_folder': '/home/user/django-remindme/django-remindme-tests',
   'failfast': False,
   'pause_on_failure': False,
   'python_version': '2.7.3',
   'xvfb': False,
   'quiet': False}


Override priority
-----------------

If any settings are set in a settings file *and* on the command line, the command line
setting will take precedence. E.g.::

    $ hitch test sometests.test --settings ci.settings --extra '{"failfast":True}'

self.settings::

  {'engine_folder': '/home/user/django-remindme/django-remindme-tests',
   'failfast': True,
   'pause_on_failure': False,
   'python_version': '2.7.3',
   'xvfb': False,
   'quiet': False}


Global settings
---------------

Some settings you will want to apply to all test runs unless specified otherwise.

These settings can be put in a YAML file called 'all.settings' which is read implicitly
if it exists. For example::

.. code-block:: yaml

    python_versions:
      - 2.7.3
      - 2.7.10
      - 3.4.3
      - 3.5.0

This specifies a default list of python versions to test with. However, it can
be overridden via a specified settings file or with the --extra switch on the command
line.

For example::

    $ hitch test sometests.test --extra '{"python_versions":["2.7.3", "3.5.0"]}'


Getting settings in engine.py
-----------------------------

To use the settings in engine.py you need to access the settings
dict. This can be done like so::

    self.settings["python_versions"]

This will either fail if 'python_versions' is not set or return the
setting as a python variable (e.g. a list in this case).

Sometimes failure is what you want.

Alternatively, if you want a default to be used in case no setting
is set, you can access the setting this way instead::

    self.settings.get("python_versions", [])

This will *not* cause the test to fail if python_versions is not set.
Instead it will just return an empty list.


Special settings
----------------

The following are special settings which change the way hitch behaves regardless of what is in engine.py:

* failfast -- this causes all test runs to stop on the first test that fails. Useful for TDD.
* colorless -- this stops color codes from being output in stacktraces - for systems like Jenkins that cannot interpret them correctly.
* quiet -- this conceals output produced by the test. It can be used to make long test logs less unwieldy.
* show_hitch_stacktrace -- by default the stacktrace displayed on errors conceals lines in hitch. This is for debugging exceptions in hitch itself.
