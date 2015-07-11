Generic Service API
===================

All of the services listed are created using the generic service API. This API lets
you start, monitor and stop any kind of process during a test.

Basic Usage
-----------

To use, define the service after initializing the ServiceBundle object but before starting it:

.. code-block:: python

        self.services['MyService'] = hitchserve.Service(
            command=["command", "arg1", "arg2, "arg3"],                 # Mandatory - command to run the service
            log_line_ready_checker=lambda line: line == "READY",        # Mandatory - function used to ascertain readiness of the service
            directory="/directory/to/run/command/in",                   # Optional
            no_libfaketime=False,                                       # Optional (if set to True, the service is run without libfaketime)
            env_vars={'A':1, 'B':2},                                    # Optional (dictionary of environment variables to feed to the service)
            needs=[self.services['Django']],                            # Optional (services to start and wait for before starting this one)
        )

.. warning::

    Libfaketime sometimes causes buggy and unpredictable behavior in some programs.
    If you see problems when running a service, you may need to switch it off with 'no_libfaketime=True'.

    Problems have been reported specifically with node.js and Java apps.

Logs
----

Most services output information about what they are doing. In UNIX, there are two
'pipes' known as stdout and stderr where processes can log normal information
and errors.

During normal operation in a test, both of these are logged to the screen, alongside
the name of the service. E.g.::

    [             Django] Performing system checks...
    [             Django] System check identified no issues (0 silenced).
    [             Django] July 11, 2015 - 10:36:58
    [             Django] Django version 1.8, using settings 'remindme.settings'
    [             Django] Starting development server at http://127.0.0.1:18080/
    [             Django] Quit the server with CONTROL-C.
    [         Err Django] [11/Jul/2015 10:36:59]"GET / HTTP/1.1" 500 99545
    [         Err Django] [11/Jul/2015 10:36:59]"GET /favicon.ico HTTP/1.1" 404 2416
    [         Err Django] [11/Jul/2015 10:36:59]"GET /favicon.ico HTTP/1.1" 404 2416

While a test is paused and interactive mode is switched off, you can still access
these logs via the log object::

    In [1]: self.service['Django'].logs
    [ Prints all of the logs ]

You can see the stdout and stderr individually, too::

    In [2]: self.service['Django'].logs.out
    [ Prints all of the logs ]

    In [1]: self.service['Django'].logs.err
    [ Prints all of the logs ]
