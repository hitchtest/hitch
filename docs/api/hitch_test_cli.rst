Hitch Test Command Line Interface
=================================

.. note::

    This documentation applies to the latest version of hitchtest: version 0.6.5 and the latest version of hitch: version: 0.4.4

To run a specific .test file::

  $ hitch test stub.test

To run *all* of the tests in a directory (and its subdirectories)::

  $ hitch test .

You can also specify multiple files and directories to test::

  $ hitch test apptests/ apitests/

Display Test YAML
-----------------

You may want to just display the YAML output of your test files,
especially if they contain jinja2 and you want to debug the output::

  $ hitch test simple_reminder.test --yaml

.. code-block:: yaml

    # /home/colm/hitch/django-remindme/django-remindme-tests/simple_reminder.test
    - engine: engine.py:DjangoReminderTestExecutionEngine
      name: Sign up, create reminder and wait for email reminder to arrive in python 2.7.10
      preconditions:
        python_version: "2.7.10"
      scenario:
        - Load website
        - Click: register
        - Fill form:
            id_username: django
            id_email: django@reinhardt.com
            id_password1: jazzguitar
            id_password2: jazzguitar
        - Click submit
        - Click: create
        - Fill form:
            id_description: Remind me about upcoming gig.
            id_when: 30 days
        - Click: create
        - Wait for email:
            Containing: Confirm E-mail Address
        - Confirm emails sent: 1
        - Time travel:
            Days: 30
        - Wait for email:
            Containing: Remind me about upcoming gig.



    - engine: engine.py:DjangoReminderTestExecutionEngine
        name: Sign up, create reminder and wait for email reminder to arrive in python 3.4.3
        preconditions:
          python_version: "3.4.3"
        scenario:
          - Load website
          - Click: register
          - Fill form:
              id_username: django
              id_email: django@reinhardt.com
              id_password1: jazzguitar
              id_password2: jazzguitar
          - Click submit
          - Click: create
          - Fill form:
              id_description: Remind me about upcoming gig.
              id_when: 30 days
          - Click: create
          - Wait for email:
              Containing: Confirm E-mail Address
          - Confirm emails sent: 1
          - Time travel:
              Days: 30
          - Wait for email:
              Containing: Remind me about upcoming gig.


Settings
--------

To use a different settings file from 'settings.yml' (the default), you must
specify it on the command line using --settings::

  $ hitch test . --settings alternative.yml

To add custom variables to your settings via the command line, use the --extra switch with JSON::

  $ hitch test . --settings alternative.yml --extra '{'specific_var':5}'


Quiet
-----

To run your tests quietly (no unnecessary text output), you can use the --quiet switch::

  $ hitch test . --quiet
