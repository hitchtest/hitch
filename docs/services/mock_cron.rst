Mock Cron Service
=================

The mock cron service is a service that will run a specified command periodically.

It can be used to mimic the effect of a real cron in a live environment.

To install::

    $ hitch install hitchcron

To use, define the service after initializing the ServiceBundle object but before starting it:

.. code-block:: python

        import hitchcron

        self.services['Cron'] = hitchcron.CronService(
            run=['command', 'arg1', 'arg2', 'arg3'],    # List containing command + args
            every=1,                                    # Run every 1 seconds
        )

