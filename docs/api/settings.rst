Settings
========

In your execution engine, self.settings is a dictionary representation of settings
used to run your test.

These settings are mostly read from your all.settings file - a YAML file.

Example all.settings:

.. code-block:: yaml

  python_version: 2.7.3
  xvfb: false
  pause_on_failure: true

Example output of settings during test::

  In [1]: self.settings
  Out[1]:
  {'engine_folder': '/home/user/django-remindme/django-remindme-tests',
   'pause_on_failure': True,
   'python_version': '2.7.3',
   'xvfb': False,
   'quiet': False}


Override or add settings from command line
------------------------------------------

You can override or add settings via the command line by specifying them
in a snippet of JSON. For example:

Example command used to run test::

  $ hitch test stub.test --extra '{"custom_var":1, "xvfb":true}'

Example output of settings during test::

  In [1]: self.settings
  Out[1]:
  {'custom_var': 1,
   'engine_folder': '/home/user/django-remindme/django-remindme-tests',
   'pause_on_failure': True,
   'python_version': '2.7.3',
   'xvfb': True,
   'quiet': False}


Override or add settings from other settings files
--------------------------------------------------

You can also store additional settings for different environments or use
cases in additional YAML files.

For example - a jenkins.settings might contain:

.. code-block:: yaml

  xvfb: true
  pause_on_failure: false

To use::

  $ hitch test . --settings jenkins.settings

The settings dict will then contain::

  {'engine_folder': '/home/user/django-remindme/django-remindme-tests',
   'pause_on_failure': False,
   'python_version': '2.7.3',
   'xvfb': True,
   'quiet': False}


Override Priority
-----------------

The following priority override applies to all settings:

* Any properties set on the command line with JSON by --extra are always used first.
* Any properties set in a YAML settings file specified by --settings are used next.
* Any properties in the YAML file named "all.settings" are used next.

Note that the following settings cannot be set by you. They will always be set by hitch:

* engine_folder - this is set by hitch to always be the absolute path containing the .hitch directory.

Special settings
----------------

The following are special settings which change the way hitch behaves regardless of what is in engine.py:

* failfast -- this causes all test runs to stop on the first test that fails. Useful for TDD.
* colorless -- this stops color codes from being output in stacktraces - for systems like Jenkins that cannot interpret them correctly.
* quiet -- this conceals all output produced by the test. It can be used to make long test logs less unwieldy to view.
* show_hitch_stacktrace -- by default the stacktrace displayed on errors conceals lines in hitch. This is only for use when debugging hitch itself.
