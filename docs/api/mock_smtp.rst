Mock SMTP Service
=================

The mock SMTP service is an SMTP server that you can use to test that your
applications have sent an email at the right time with the right contents.

To install::

    $ hitch install hitchsmtp

To run, define the service after initializing the ServiceBundle object but before starting it:

.. code-block:: python

        import hitchsmtp

        # Service definition in your test execution engine's setUp
        self.services['HitchSMTP'] = hitchsmtp.HitchSMTPService(
            port=10025                                                 # Optional (default: 10025)
        )

To show a list of all sent emails during a test::

    In [1]: self.services['HitchSMTP'].logs.json()
    [ list of dicts of email contents and properties ]

To wait for an email and then check that it contained the right contents during the test::

    In [2]: email = self.services['HitchSMTP'].logs.out.tail.until_json(
        lambda email: "register: in email['payload'] or "register" in email['Subject'],
        timeout=5,
        lines_back=1,
    )

    In [3]: email
    [ dict of email contents and properties ]
