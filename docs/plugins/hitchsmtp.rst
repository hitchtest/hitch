HitchSMTP
=========

.. note::

    This documentation applies to the latest version of hitchsmtp.

HitchSMTP is a :doc:`/glossary/hitch_plugin` created to make testing applications that send emails easier.

It contains:

* A :doc:`/glossary/service` to run a mock SMTP server that your application can be configured to send emails to.

Installation
------------

To install::

    $ hitch install hitchsmtp

Set up HitchSMTP
----------------

To use, define the service after initializing the :doc:`/api/service_bundle`:

.. code-block:: python

    import hitchsmtp

    self.services['HitchSMTP'] = hitchsmtp.HitchSMTPService(
        port=10025                                                 # Optional (default: 10025)
    )

Once it is running, you can access the emails which arrived via the logs::

    In [1]: self.services['HitchSMTP'].logs.json()
    [ list of dicts of email contents and properties ]

You can also wait for emails to arrive by waiting for the logs::

    In [2]: email = self.services['HitchSMTP'].logs.out.tail.until_json(
        lambda email: "register: in email['payload'] or "register" in email['Subject'],
        timeout=5,
        lines_back=1,
    )

    In [3]: email
    [ dict of email contents and properties ]
