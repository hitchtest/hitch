HitchCron
=========

.. note::

    This documentation applies to the latest version of hitchcron.

HitchCron is a :doc:`/glossary/hitch_plugin` created to make testing applications that rely upon a cron or cron-like service.

It contains:

* A :doc:`/glossary/service` that runs during the whole test that runs a command periodically (typically every second).



Installation
------------

To install::

    $ hitch install hitchcron


Set up Cron
-----------

To use, define the service after initializing the ServiceBundle object but before starting it:

.. code-block:: python

    import hitchcron

    self.services['Cron'] = hitchcron.CronService(
        run=['command', 'arg1', 'arg2', 'arg3'],    # Mandatory - list containing command + args
        every=1,                                    # Optional (Default: run every 1 seconds)
    )

