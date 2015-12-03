What kind of debugging tools ship with Hitch?
=============================================

Hitch takes the approach that, as a testing framework, it should not only make it easy
to write and run tests, it should make it easy to find bugs by including first class
debugging tools.

The IPython REPL
================

Hitch ships with IPython and integrates with it deeply. When you use the step 'pause'
it is launched, at which point you have access to a wealth of tools to inspect
the environment your app is running in, change the time in your app,
run steps and much, much more::

    In [1]: self.services.time_travel(days=30)

    In [2]: self.services['Django'].manage("help").run()
    
    In [3]: self.click("button-id")

While useful, this only gives you a bird's eye view and control over your application.
In order to debug you will want to dig deeper.

As well as giving you access to the hitch environment via IPython, you can also
connect directly to embedded IPython kernels and run a REPL in your code's
environment *no matter what language your code is running in*::

    - Click and don't wait for page load: button-id
    - Connect to kernel: Django


Log Catting and Tailing
=======================

The first port of call when debugging any kind of application is to look in the logs.

By default, all services run under the Hitch service framework are asynchronously logged
together, so while a test is running you can always see what the services you are
running together are saying::

    [             Django] Performing system checks...
    [             Django] System check identified no issues (0 silenced).
    [             Django] November 30, 2015 - 16:03:15
    [             Django] Django version 1.8.7, using settings 'config.settings.local'
    [             Django] Starting development server at http://127.0.0.1:8000/
    [             Django] Quit the server with CONTROL-C.
    [              Hitch] Django Loaded.
    [              Hitch] READY in 5.4 seconds.
    [         Err Django] [30/Nov/2015 16:03:33] "GET / HTTP/1.1" 200 34140
    [         Err Django] [30/Nov/2015 16:03:33] "GET /static/css/bootstrap.min.css HTTP/1.1" 200 122887



While your test is paused and you're in IPython you can also directly inspect the logs of particular services::

    In [1]: self.services['Django'].logs
    [             Django] Performing system checks...
    [             Django] System check identified no issues (0 silenced).
    [             Django] November 30, 2015 - 16:03:15
    [             Django] Django version 1.8.7, using settings 'config.settings.local'
    [             Django] Starting development server at http://127.0.0.1:8000/
    [             Django] Quit the server with CONTROL-C.
    [         Err Django] [30/Nov/2015 16:03:33] "GET / HTTP/1.1" 200 34140
    [         Err Django] [30/Nov/2015 16:03:33] "GET /static/css/bootstrap.min.css HTTP/1.1" 200 122887
