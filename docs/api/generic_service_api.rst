Generic Service API
===================

.. note::

    This documentation applies to the latest version of hitchserve.

All of the services listed are run using the generic service API. This API lets
you start, monitor and stop any kind of process during a test.

Defining a Service Bundle
-------------------------

To run one or more services together during your tests, you must first define a
:doc:`/glossary/service_bundle` which will run them all together.

The definition of your service bundle should go in your :doc:`/glossary/test_setup` in the
:doc:`/glossary/execution_engine`:

.. code-block:: python

    # Create a service bundle
    self.services = hitchserve.ServiceBundle(
        project_directory=PROJECT_DIRECTORY,        # Default directory all of your services are started in
        startup_timeout=15.0,                       # How long to wait for all of the services to startup
        shutdown_timeout=5.0,                       # How long to wait for all of the services to shutdown before killing
    )

Once your service bundle is defined, you can start defining services.

Defining a Service to Run
--------------------------

Next, your code needs to define services to run with your service bundle. You define
generic services like this:

.. code-block:: python

        self.services['MyService'] = hitchserve.Service(
            command=["command", "arg1", "arg2", "arg3"],         # Mandatory - command to run the service
            log_line_ready_checker=lambda line: line == "READY", # Mandatory - function used to ascertain readiness of the service
            directory="/directory/to/run/command/in",            # Optional
            no_libfaketime=False,                                # Optional (if set to True, the service is run without libfaketime)
            env_vars={'A':1, 'B':2},                             # Optional (dictionary of environment variables to feed to the service)
            needs=[self.services['Django']],                     # Optional (services to start and wait for before starting this one)
        )




Starting a service bundle
-------------------------

Once all of your services are defined, they still aren't started. To start your services
you must call the startup method:

.. code-block:: python

    self.services.startup(interactive=False)


.. note::

    interactive=False should be the default for all tests. However, if you want to run this
    command in an :doc:`/glossary/ipython` console, use interactive=True.

    interactive=False will take over the console and start printing logs as they arrive.
    interactive=True will not take over the console.


Interacting with a Service Bundle: Switching to Interactive Mode
----------------------------------------------------------------

If you want your service bundle to stop logging to the screen (e.g. so you can launch
IPython), you can start the interactive mode.

.. code-block:: python

        self.services.start_interactive_mode()
        # Do interactive stuff here
        self.services.stop_interactive_mode()

If you just want to print a log message during your test alongside all of the
other logs, however, you can just use:

.. code-block:: python

        self.services.log("Your message here")
        self.services.warn("A bad thing just happened")

.. warning::

    Avoid using the print("") command to log messages. It will cause an error.


Interacting with a Service Bundle: Logs
---------------------------------------

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


This will hopefully tell you most of what you need to know about why your services
are reporting errors.

While a test is paused and interactive mode is switched off, you can access
these logs via the log object::

    In [1]: self.service['Django'].logs
    [ Prints all of the logs ]

You can see the stdout and stderr individually, too::

    In [2]: self.service['Django'].logs.out
    [ Prints all of the logs ]

    In [3]: self.service['Django'].logs.err
    [ Prints all of the logs ]

As with the UNIX console, you can also tail your logs. This is a useful debugging
tool::

    In [4]: self.service['Django'].logs.tail.follow(lines_back=2)
    [ Prints logs from two lines before the command starts. ]
    [ Continues logging in real time until you hit ctrl-C ]


Interacting with a Service Bundle: JSON Logs
--------------------------------------------

If you have a service which outputs JSON, hitch can read the logs and parse
the JSON automatically. This is *extremely* useful for writing test steps that
listen to a :doc:`/glossary/mock_service`.

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


Interacting with a Service Bundle: Time Travel
----------------------------------------------

Many bugs and test scenarios often cannot be realistically replicated without
jumping through time.

The example application - a reminders app - is one example. To test that a reminder
is really sent after 30 days, the application must *think* that 30 days have actually
passed.

You can mimic these scenarios for services run using your service bundle by
calling the time_travel API, which can be used like so::

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

If you forgot where you are, you can get the current (mocked) time via::

    In [7]: self.services.now()
    Out[7]: datetime.datetime(2015, 7, 19, 16, 21, 33, 703669)

To move to an absolute time::

    In [8]: from datetime import datetime

    In [9]: self.services.time_travel(datetime=datetime.now())
    Time traveling to now


Note that if no_libfaketime is set to True for a service, it will not pick up on the new time.

.. warning::

    This feature relies upon a C library called libfaketime.

    Libfaketime sometimes causes buggy and unpredictable behavior in some programs (e.g. node.js and Java)
    on some platforms.

    If you see problems when running a service, you may need to switch it off with 'no_libfaketime=True'.

    Some programs will also work fine (e.g. firefox), but they will not pick up on the time being fed
    to them.

    Libfaketime works well with python and postgresql.


Interacting with a Service Bundle: Connecting to a service's IPython Kernel
---------------------------------------------------------------------------

IPython kernels are a great way of debugging your code. They give you access
to a REPL which you can use to inspect variables and run commands to see their
effect.

With python code, you can invoke a kernel by putting the following line of
code in your application:

.. code-block:: python

    import IPython ; IPython.embed_kernel()

Hitch provides a convenience function which you can use to listen to a service's
logs and detect the presence of a recently embedded kernel and then connect
directly to it and launch an interpreter in interactive mode.

.. code-block:: python

    def connect_to_kernel(self, service_name):
        self.services.connect_to_ipykernel(service_name)

This is a step that can be called just by adding ::

    - Connect to kernel: Celery

Note that if you are connecting to a kernel after clicking a button in a web
app, be sure to replace 'click' with the following step::

    - Click and dont wait for page load: button-id

The regular click step will wait for the next page to load before continuing,
which will never happen because your app paused on loading it due to the embed_kernel.


Interacting with a Service Bundle: The Process API
--------------------------------------------------

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

The psutil Process class API can be used to inspect the CPU usage of the service, its memory usage, list open files and much much more.

The full API docs for psutil's Process class are here: https://pythonhosted.org/psutil/#process-class


Interacting with a Service Bundle: Service Sub-commands
-------------------------------------------------------

Many services have special commands which are run during their operation.
For example, Django has the manage command, Redis has redis-cli and
Postgresql has psql.

Hitch provides an API to let you run these commands in the same environment
as the service you are running. This means that they will inherit the same
environment variables and time::

    In [1]: self.services['Django'].manage("help").run()


Running Arbitrary Code Before and After Starting a Service
----------------------------------------------------------

Some services can just be started and stopped, but others require special
code to be run before and after. A good example of this is postgresql,
which requires initdb be run before starting the database service, and CREATE
USER / CREATE DATABASE to be run after.

If your service has special requirements like this, you can subclass the
hitchserve Service object and override the setup and poststart
methods:

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
