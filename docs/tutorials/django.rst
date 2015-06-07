Getting started functional testing with Hitch and with Django, Celery, Redis, Cron and Postgresql
=================================================================================================

Django-RemindMe is a simple Django app which lets users sign up, create email reminders
for themselves and have those emails delivered to them at a later date. It makes use
of Django, Celery, Redis, Cron, Postgresql and sends emails.

Applications like these are naturally not so easy to write automated tests for -
particularly not loosely coupled automated tests. Hitch aims to solve this problem.

This is a tutorial that will guide you through the steps you need to
to create a test harness and write a simple test for this Django app.

This tutorial assumes a rudimentary level of Python and Django knowledge and access
to a UNIX machine of some sort (Linux, Mac, Linux VM of some sort, etc.).

If you are very familiar with Python and/or Django, I recommended that you
just check out the django-remindme repository and then check out the
django-remindme-tests repository inside it and take a look around that.



Preparation
-----------

You need several prerequisite packages installed before you can begin here:

On Ubuntu::

    $ sudo apt-get install python python-virtualenv python-pip postgresql redis-server git firefox node-less libtool automake


On a Mac (make sure firefox is installed first)::

    $ brew install python redis postgresql git libtool automake npm

    $ npm install -g less

    $ pip install -U setuptools pip virtualenv

Then, find a new directory and check out the code. You can do that by::

    $ git clone git@github.com:hitchtest/django-remindme.git

Or::

    $ git clone https://github.com/hitchtest/django-remindme.git

Finally, you must install hitch, which you can do by running::

    $ sudo pip install hitch

Or, if you'd prefer not to use root, you can install it through pipsi_::

    $ pipsi install hitch


Create your hitch environment
-----------------------------

Go to the django-remindme directory and create a tests directory::

    $ mkdir tests

Inside the tests directory, run this command::

    $ hitch init

This creates a directory called .hitch in your project folder.
This self-contained directory contains all of the code required to
run hitch tests, including something called a virtualenv_, containing
python packages required to run tests.

This directory can be regenerated from scratch and should be gitignored.

Hitch init will also create a file called hitchreqs.txt in your project
directory containing a list of all packages installed in the hitch
environment. This should be stored in your repo as it can be used to
regenerate your hitch environment from scratch.


Test setup #1: Create the skeleton engine and test
--------------------------------------------------

Before you can write a line of test code for your harness, you first
need to write some simple code to run your code. This is known as the
execution engine. In hitch, this takes the form of a very basic
python unit test case, looking like this:

.. code-block:: python

    import unittest
    import IPython

    # Get directory above this file
    PROJECT_DIRECTORY = path.join(path.dirname(__file__), '..')

    class RemindMeExecutionEngine(unittest.TestCase):
        def setUp(self):
            pass

        def pause()
            IPython.embed()

        def tearDown(self):
            pass

You can save this file in the tests directory. It must be in the same
directory as your .hitch folder.

In the same directory, you need to create a stub test case (call it stub.yml), like so::

    - engine: engine.RemindMeExecutionEngine
      scenario:
        - Pause

You can run this, by running the following command::

    $ hitch test tests/template.yml

All this test and engine does is start an IPython prompt currently,
but it serves as a base which we can use to build more.

Test setup #2: Install a virtualenv using your test
------------------------------------------------

The first thing your engine needs to do is to create a virtualenv
for your django application. This is an isolated folder that
contains all of the python packages that your Django app
needs to run. The list of packages are stored in requirements.txt in
the project folder.

So, after running the test, try running these commands::

    In [1]: from os import path, chdir

    In [2]: from subprocess import call

    In [3]: chdir(PROJECT_DIRECTORY)

    In [4]: call(["virtualenv", "venv", "--no-site-packages"])

    In [5]: call(["./venv/bin/pip", "install", "-r", "requirements.txt"])

This sets up a local environment so that your application can now run.
You can now copy and paste these lines back into your setUp by typing
this and copying and pasting back the result::

    In [6]: %history

Unfortunately, this code still has a problem. If you run it a second time it will
fail because the virtualenv is already created. To solve this, you must
check for its existence first and only create it if it isn't there, like so:

.. code-block:: python

    from os import path, chdir
    import unittest
    import IPython

    # Get directory above this file
    PROJECT_DIRECTORY = path.join(path.dirname(__file__), '..')

    class RemindMeExecutionEngine(unittest.TestCase):
        def setUp(self):
            chdir(PROJECT_DIRECTORY)
            if not path.exists(path.join(PROJECT_DIRECTORY, "venv")):
                subprocess.call(["virtualenv", "venv", "--no-site-packages"])
            subprocess.call(["./venv/bin/pip", "install", "-r", "requirements.txt"])

        def pause():
            IPython.embed()

        def tearDown(self):
            pass


Test setup #3: Lock in your current environment and start the Service Bundle
----------------------------------------------------------------------------

Now that you have a virtualenv set up, you can start running things, namely the
above six services. First, though, you must write some code to ensure that
the environment your test is running on is suitable to run your tests, and
to fail fast if it isn't.

To do service based functional tests, you must have a hitch
component installed called "hitchserve" installed::

    $ hitch install hitchserve

These will all be installed in the .hitch directory, and the file hitchreqs.txt will
be updated to account for all of the packages and dependencies required.

Now, you can run the stub again and start using hitch serve::

    $ hitch test tests/stub.yml

Now, when you are presented with a prompt, you can run a command which prints out
the environment details of your machine::

    In [1]: import hitchserve

    In [2]: import hitchenvironment

    In [3]: hitchenvironment.class_definition()
    hitchenvironment.Environment("linux2", 64, True)        # Yours may look different to this

What this means is that the machine I ran this on runs linux, is 64 bit and currently
has access to the Internet. You can assign this to a variable like so, and change requires_internet
to False (since Django-RemindMe tests won't require internet to run)::

    In [4]: environment = hitchenvironment.Environment("linux2", 64, False)

And create an empty ServiceBundle like so::

    In [5]: self.services = hitchserve.ServiceBundle(project_directory=PROJECT_DIRECTORY, environment=environment)

You can then start it like so::

    In [6]: self.services.startup(interactive=True)

But, it wont do anything yet.

You can stop it again by running the shutdown command::

    In [7]: self.services.shutdown()

Now, you can copy and paste all the code that you just ran (using %history) into your engine.py. It should look something like this now:

.. code-block:: python

    from os import path, chdir
    import unittest
    import IPython
    import hitchserve

    # Get directory above this file
    PROJECT_DIRECTORY = path.join(path.dirname(__file__), '..')

    class RemindMeExecutionEngine(unittest.TestCase):
        def setUp(self):
            chdir(PROJECT_DIRECTORY)
            if not path.exists(path.join(PROJECT_DIRECTORY, "venv")):
                subprocess.call(["virtualenv", "venv", "--no-site-packages"])
            subprocess.call(["./venv/bin/pip", "install", "-r", "requirements.txt"])

            environment = hitchserve.environment.Environment("linux2", 64, False)
            self.services = hitchserve.ServiceBundle(project_directory=PROJECT_DIRECTORY, environment=environment)

            self.services.startup(interactive=True)

        def pause():
            IPython.embed()

        def tearDown(self):
            self.services.shutdown()


Test Setup #4: Add your first service to the ServiceBundle
----------------------------------------------------------

We'll start with Redis, since it's a pretty simple service with few dependencies.

Run this command to install the (very simple) hitchredis plugin::

    $ hitch install hitchredis

Also run redis-server to check that it's there and get its version, e.g.::

    $ redis-server --version
    Redis server v=2.8.4 sha=00000000:0 malloc=jemalloc-3.4.1 bits=64 build=a44a05d76f06a5d9

Then you'll need to insert another IPython.embed() before self.services.startup, so that you can interactively
add your first service.

.. code-block:: python

    self.services = hitchserve.ServiceBundle(project_directory=PROJECT_DIRECTORY, environment=environment)
    IPython.embed()
    self.services.startup(interactive=True)

Then run the test again. During the first prompt, you will have access to self.services before it is started, so you
can start telling it *what* to run::

    In [1]: import hitchredis

    In [2]: self.services['Redis'] = hitchredis.RedisService(version="2.8.4")

That's it. Now you can hit ctrl-D and HitchServe will start it. You should see a new IPython prompt appear::

    Python 2.7.6 (default, Mar 22 2014, 22:59:56)
    Type "copyright", "credits" or "license" for more information.

    IPython 3.1.0 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

Which you can now use to interact with redis, using its CLI::

    In [1]: self.services['Redis'].cli().run()
    127.0.0.1:16379>

Now you can copy and paste the service definition back to your engine.

Test Setup #5: Start Postgres too
---------------------------------

To install::

    $ hitch install hitchpostgres

Postgres is a little more complicated, but not much. You have to tell Hitch where it's installed,
what users and databases you want created when you run it::

    In [1]: import hitchpostgres

    In [2]: postgres_installation = hitchpostgres.PostgresInstallation("/usr/lib/postgresql/9.3/bin/")

    In [3]: postgres_user = hitchpostgres.PostgresUser("remindme", "password")

    In [4]: postgres_database = hitchpostgres.PostgresDatabase("remindme", postgres_user)

    In [5]: self.services['Postgres'] = hitchpostgres.PostgresService(version="9.3.6", postgres_installation=postgres_installation, users=[postgres_user,], databases=[postgres_database,])

And hit ctrl-D and you should see it start, and then you can interact with the root template database::

    In [1]: self.services['Postgres'].psql().run()
    psql (9.3.6)
    Type "help" for help.

    template1=#

Or (hit ctrl-D), you can interact with the database you just created::

    In [2]: self.services['Postgres'].databases[0].psql().run()
    psql (9.3.6)
    Type "help" for help.

    remindme=#


Test Setup #6: Start Django and Celery
--------------------------------------

To install::

    $ hitch install hitchdjango

Django is a little special in that it requires Postgres to start up, and you must specify which python is used to run it,
and you must specify which settings file to use::

    In [1]: import hitchdjango

    In [2]: self.services['Django'] = hitchdjango.DjangoService(
                version="1.8",
                python="{}/venv/bin/python".format(PROJECT_DIRECTORY),
                settings="remindme.settings",
                needs=[self.services['Postgres'], ]
            )

Once started, you can interact with it via manage commands::

    In [1]: self.services['Django'].manage("help")

And you can get the URL required to load it::

    In [1]: self.services['Django'].url()
    http://127.0.0.1:18080/

And, to install Celery::

    $ hitch install hitchcelery

Celery is defined much like Django::

    In [1]: import hitchcelery

    In [2]: self.services['Celery'] = hitchcelery.CeleryService(
                version="3.1.17",
                python="{}/venv/bin/python".format(PROJECT_DIRECTORY),
                app="remindme",
                needs=[
                    self.services['Redis'], self.services['Postgres'],
                ]
            )


Test Setup #7: Mock Cron and Mock SMTP
--------------------------------------

We have two more pieces which our app needs in order to run correctly:

* A way to mock the effect of the cron service which will run a check periodically if any reminders need to be sent.
* A way to mock an external SMTP gateway which will be used to send emails.

The first can be done with hitchcron::

    $ hitch install hitchcron

    In [1]: import hitchcron

    In [2]: self.services['Cron'] = hitchcron.CronService(
                run=self.services['Django'].manage("trigger").command,
                every=1,
                needs=[ self.services['Django'], self.services['Celery'], ],
            )

This will start a service which will run Django's trigger command every 1 second.

The second can be done with hitchsmtp::

    $ hitch install hitchsmtp

    In [1]: import hitchsmtp

    In [2]: self.services['HitchSMTP'] = hitchsmtp.HitchSMTPService()


Test Setup #8: Start your browsers!
-----------------------------------

Now that we have everything ready to run the app, we need one more thing to test it
- a browser we can programmatically interact with.

Fortunately, we have one of these too::

    $ hitch install hitchselenium

    In [1]: import hitchselenium

    In [2]: self.services['Firefox'] = hitchselenium.SeleniumService()

This will start the browser, but to interact with it, we need a selenium driver::

    In [3]: self.driver = self.services['Firefox'].driver

(Now copy & paste this back)

Et, voila::

    In [1]: self.driver.get(self.serices['Django'].url())

    In [2]: self.driver.find_element_by_id("register").click()


Writing your test
-----------------

Now we have a running application that we can start up and shut down at will, but
we still want some automated steps to test it. Currently we have a test that looks
like this::

    - engine: engine.RemindMeExecutionEngine
      scenario:
        - Pause

Doesn't do much, right?

Still, note that the only step followed is a method in our engine::

    def pause():
        IPython.embed()

Why not add a step::

    - engine: engine.RemindMeExecutionEngine
      scenario:
        - Load website
        - Pause

This will fail, currently, because there is no method called load_website.

How do we make this happen? Easy, add another method::

    def load_website(self):
        self.driver.get(self.serices['Django'].url())


Conclusion
----------

That's the end of our first Hitch tutorial. There's much more you can do
with hitch. To see more, just check out the Django-RemindMe-Tests project into
the django-remindme root folder.

* engine.py
* simple_reminder.yml
* settings.yml
