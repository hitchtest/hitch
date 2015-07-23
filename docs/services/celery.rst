Celery
======

.. note::

    This documentation applies to hitchpython version 0.1

Install the hitch python package::

    $ hitch install hitchpython

To use, define the service after initializing the ServiceBundle object but before starting it.

.. code-block:: python

        # Service definition in engine's setUp:
        self.services['Celery'] = hitchcelery.CeleryService(
            version="3.1.17",                                       # Mandatory
            python="{}/venv/bin/python".format(PROJECT_DIRECTORY),  # Mandatory
            app="remindme",                                         # Mandatory
            beat=False,                                             # Optional (default: False)
            concurrency=2,                                          # Optional (default: 2)
            loglevel="INFO",                                        # Optional (default: INFO)
            broker=None,                                            # Optional (default: None)
            needs=[ self.services['Redis'], ]                       # Optional (default: no prerequisites)
        )


Once it is running, you can interact with the service::

    In [1]: self.services['Celery'].help().run()
    [ Prints help ]

    In [1]: self.services['Celery'].status().run()
    [ Prints celery queue status ]

    In [1]: self.services['Celery'].control(*args).run()
    [ Run specific celery control commands ]

    In [1]: self.services['Celery'].inspect(*args).run()
    [ Run specific celery inspect commands ]
