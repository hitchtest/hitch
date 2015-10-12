Generic Service API
===================

.. note::

    This documentation applies to the latest version of hitchserve.

All of the services listed are run using the generic service API. This API lets
you start, monitor and stop any kind of process during a test.

Basic Usage
-----------

To use, define the service after initializing the ServiceBundle object but before starting it:

.. code-block:: python

        self.services['MyService'] = hitchserve.Service(
            command=["command", "arg1", "arg2", "arg3"],                # Mandatory - command to run the service
            log_line_ready_checker=lambda line: line == "READY",        # Mandatory - function used to ascertain readiness of the service
            directory="/directory/to/run/command/in",                   # Optional
            no_libfaketime=False,                                       # Optional (if set to True, the service is run without libfaketime)
            env_vars={'A':1, 'B':2},                                    # Optional (dictionary of environment variables to feed to the service)
            needs=[self.services['Django']],                            # Optional (services to start and wait for before starting this one)
        )

.. warning::

    Libfaketime sometimes causes buggy and unpredictable behavior in some programs (e.g. node.js and Java).
    If you see problems when running a service, you may need to switch it off with 'no_libfaketime=True'.


Logs
----

Most services output information about what they are doing. In UNIX, there are two
'pipes' known as stdout and stderr where processes can log regular information
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

    In [3]: self.service['Django'].logs.err
    [ Prints all of the logs ]

You can tail the logs too::

    In [4]: self.service['Django'].logs.tail.follow(lines_back=2)
    [ Prints logs from two lines before the command starts. ]
    [ Continues logging in real time until you hit ctrl-C ]

Hitch also lets you grab a list of log lines encoded as JSON and return them
as a list of dicts/lists. For example::

    In [5]: self.service['HitchSMTP'].logs.json()
    Out[5]:
    [{'contenttype': 'text/plain',
    'date': 'Tue, 14 Jul 2015 05:59:44 -0000',
    'header_from': 'webmaster@localhost',
    'header_from_email': None,
    'header_from_name': None,
    'header_to': 'django@reinhardt.com',
    'header_to_email': None,
    'header_to_name': None,
    'links': ['http://127.0.0.1:18080/accounts/confirm-email/oro7rarxl8poqk9moe6jru5do6uoqijlllpcllmuqfaotqpvrdw3wlezsfvdtto4/'],
    'multipart': False,
    'payload': 'User django at 127.0.0.1:18080 has given this as an email address.\n\nTo confirm this is correct, go to http://127.0.0.1:18080/accounts/confirm-email/oro7rarxl8poqk9moe6jru5do6uoqijlllpcllmuqfaotqpvrdw3wlezsfvdtto4/',
    'sent_from': 'webmaster@localhost',
    'sent_to': ['django@reinhardt.com'],
    'subject': '[127.0.0.1:18080] Confirm E-mail Address'},
    {'contenttype': 'text/plain',
    'date': 'Thu, 13 Aug 2015 13:59:47 -0000',
    'header_from': 'noreply@localhost',
    'header_from_email': None,
    'header_from_name': None,
    'header_to': '<django@reinhardt.com>',
    'header_to_email': 'django@reinhardt.com',
    'header_to_name': '',
    'links': [],
    'multipart': False,
    'payload': 'Remind me about upcoming gig.',
    'sent_from': 'noreply@localhost',
    'sent_to': ['django@reinhardt.com'],
    'subject': 'Reminder'}]

This is a useful feature for verifying interactions with mock services went according to plan.

You can also tail the logs until a specific condition is met in a JSON line, for instance::

    In [5]: self.services['HitchSMTP'].logs.out.tail.until_json(
                lambda email: containing in email['payload'] or containing in email['subject'],
                timeout=15,
                lines_back=1,
            )
    [ returns full dict representation of JSON snippet representing email once it has been received ]


Time Travel
-----------

Some test scenarios require you to move forward through time. Hitch provides a high level way of
making your code *think* that the time is by hijacking the standard UNIX time API and lying via it.

The service bundle object has a special command which can be used to mock the forward (or even backward)
passage of time.

To move forward relatively you can use the following API::

    In [1]: self.services.time_travel(days=1)
    Time traveling to 23 hours from now

    In [2]: self.services.time_travel(hours=25)
    Time traveling to 2 days from now

    In [3]: self.services.time_travel(minutes=60)
    Time traveling to 2 days from now

    In [4]: self.services.time_travel(seconds=60)
    Time traveling to 2 days from now

    In [5]: from datetime import timedelta

    In [6]: self.services.time_travel(timedelta=timedelta(hours=1))
    Time traveling to 2 days from now

You can get the current (mocked) time via::

    In [7]: self.services.now()
    Out[7]: datetime.datetime(2015, 7, 19, 16, 21, 33, 703669)

To move to an absolute time use::

    In [8]: from datetime import datetime

    In [9]: self.services.time_travel(datetime=datetime.now())
    Time traveling to now

This feature has been tested and works with Postgres and Python code run as a service, but has been
tried with and will not yet work with node.JS code, Java code or Firefox.

Note that it will not work if no_libfaketime is set to True.

Service Process API
-------------------

To see a service's process ID::

    In [1]: self.services['HitchSMTP'].pid
    Out[1]: 43215

To interact with or inspect the service's process::

    In [1]: self.services['HitchSMTP'].process.<TAB>
    self.services['HitchSMTP'].process.as_dict           self.services['HitchSMTP'].process.is_running        self.services['HitchSMTP'].process.pid
    self.services['HitchSMTP'].process.children          self.services['HitchSMTP'].process.kill              self.services['HitchSMTP'].process.ppid
    self.services['HitchSMTP'].process.cmdline           self.services['HitchSMTP'].process.memory_info       self.services['HitchSMTP'].process.resume
    self.services['HitchSMTP'].process.connections       self.services['HitchSMTP'].process.memory_info_ex    self.services['HitchSMTP'].process.rlimit
    self.services['HitchSMTP'].process.cpu_affinity      self.services['HitchSMTP'].process.memory_maps       self.services['HitchSMTP'].process.send_signal
    self.services['HitchSMTP'].process.cpu_percent       self.services['HitchSMTP'].process.memory_percent    self.services['HitchSMTP'].process.status
    self.services['HitchSMTP'].process.cpu_times         self.services['HitchSMTP'].process.name              self.services['HitchSMTP'].process.suspend
    self.services['HitchSMTP'].process.create_time       self.services['HitchSMTP'].process.nice              self.services['HitchSMTP'].process.terminal
    self.services['HitchSMTP'].process.cwd               self.services['HitchSMTP'].process.num_ctx_switches  self.services['HitchSMTP'].process.terminate
    self.services['HitchSMTP'].process.exe               self.services['HitchSMTP'].process.num_fds           self.services['HitchSMTP'].process.threads
    self.services['HitchSMTP'].process.gids              self.services['HitchSMTP'].process.num_threads       self.services['HitchSMTP'].process.uids
    self.services['HitchSMTP'].process.io_counters       self.services['HitchSMTP'].process.open_files        self.services['HitchSMTP'].process.username
    self.services['HitchSMTP'].process.ionice            self.services['HitchSMTP'].process.parent            self.services['HitchSMTP'].process.wait

The psutil Process class API can be used to inspect the CPU usage of the process, memory usage, list open files and much much more.

The full API docs for psutil's Process class are here: https://pythonhosted.org/psutil/#process-class


Service Sub-commands
--------------------

Many services have special commands which are run during their operation.
For example, Django has the manage command, Redis has redis-cli and
Postgresql has psql.

Hitch provides an API to let you run these commands in the same environment
as the service you are running. This means that they will inherit the same
environment variables and system time::

    In [1]: self.services['Django'].manage("help").run()


Running Arbitrary Code Before and After Starting a Service
----------------------------------------------------------

Some services can just be started and stopped, but others require special
code to be run before and after. A good example of this is postgresql,
which requires initdb be run before starting the database service, and CREATE
USER / CREATE DATABASE to be run after.

If your service has special requirements like this, you can subclass the
hitchserve Service object:

.. code-block:: python

    from hitchserve import Service
    import signal


    class MyService(Service):
        def __init__(self, **kwargs):
            kwargs['log_line_ready_checker'] = lambda line: "line in logs that signals readiness" in line
            kwargs['command'] = ["start_service_command", "arg1", "arg2", "arg3", ]
            super(MyService, self).__init__(**kwargs)

        def setup(self):
            """This is where you run all of the code you want run before starting the service."""
            pass

        def poststart(self):
            """This is where you put all of the code you want run after the service is ready."""
            pass
