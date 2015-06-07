Hitch
=====

Hitch is a loosely-coupled, isolated by design testing framework built upon python's
unittest that lets you write simple, easy to read and easy to debug tests for *any*
software (not just web apps and not just python apps).

Using Hitch you can very easily create and run tests like this::

  - engine: engine.DjangoReminderTestExecutionEngine
    description: Sign up, create reminder and wait for email reminder to arrive.
    scenario:
      - Load website
      - Click: Register
      - Fill form:
          Username: django
          Email: django@reinhardt.com
          Password1: jazzguitar
          Password2: jazzguitar
      - Click: Create
      - Create reminder:
          Description: Remind me about upcoming gig.
          Days from now: 30
      - Wait for email:
          Containing: Confirm E-mail Address
      - Confirm emails sent: 1
      - Time travel:
          Days: 30
      - Wait for email:
          Containing: Remind me about upcoming gig.

...where each step is a 1-4 line method in the test execution engine, written in python, defined by you (e.g. def wait_for_email).

The engine for this partcular test is only 150 lines long and takes care of all of the following:

* Creating/setting up a virtualenv - the application's build step (test setup).
* Starting all 4 services required to run this app - Django, Celery, Redis, Postgres (test setup).
* Starting the two mock services required to test this app - Selenium browser (firefox) and the Mock SMTP server (test setup).
* A method to run all of the above steps (execution).
* Stopping all of the services (teardown).

Example project the test was written for: http://github.com/hitchtest/django-remindme

Example test script, execution engine and settings for the project: http://github.com/hitchtest/django-remindme-tests


Unique Features of Hitch
========================

* Very loosely coupled - changing the framework to accomodate your specific requirements should be easy compared to other more inflexible and tightly coupled testing frameworks that make assumptions about your environment.
* Enforces clean separation of concerns - the tests are written with a clean, non-turing complete test description language, helping keep test interaction code and scenario descriptions separate. The engine that runs them is written in python.
* Simple test description language - it is possible to make your tests readable and even writable by non-programmers without sacrificing power.
* ...that does not reinvent the wheel - the test description language is very basic, and built using YAML + Jinja2. If you have used ansible or salt, you will appreciate the simplicity and ease of this approach.
* Highly optimized - the service orchestration portion starts and tracks services in parallel, making use of epoll/kqueue to do so. Say goodbye to sleeps. Say hello to much faster functional tests!
* Mock the passage of time - during your test you can pass a new time to your applications during scenarios that are time sensitive. Hitch uses a C library called libfaketime_ to invisibly feed a new UNIX system time to your services without changing your system time. Note that some types of code may not work well with this library due to the way that they read system time (e.g. node.js, Java).
* Highly isolated - hitch creates its own virtual environment, so that the libraries and code you use to run your tests can be kept separate from the code your application needs and uses (assuming the application you are testing is even written in python).
* Easily extensible - writing code to run your custom services is very easy and quick. The framework abstracts the parallelism away from you.
* Easy to add mock services - let's say your application needs to talk a weird protocol to an external service. You can write a very simple mock service that receives a message in that protocol and logs it to JSON. The testing framework can pick up and parse that JSON and you can add a step in your test to parse it and verify that your application interacted with that service correctly. HitchSMTP_ is built based upon this principle.
* Integrated debugging tools - all service logs are aggregated into one easy to read log. Pausing and launching into IPython (with more powerful tab completion than default IPython) at any point in your tests is simple.


Getting Started
===============

You can install the hitch bootstrapping script with::

  $ sudo pip install hitch

Or::

  $ pipsi_ install hitch (if you do not want to use root)

This is a very simple script (with one dependency: click), which creates its own
virtualenv that you can use to install all the other components.

There is currently one tutorial for Hitch:

* Getting started testing with Hitch and Django, Celery, Cron, Redis and Postgresql


Components
==========

It currently has ten components, all of which can be used individually,
together, or not at all. Those are:

* HitchTest_         - simple declarative test description language based on YAML and jinja2.
* HitchServe_        - simple service orchestration to let you easily write functional tests for service based applications.
* HitchEnvironment_  - plugin to let you define the environment your tests will run on.
* HitchSMTP_         - Mock SMTP server - to test email sending in your functional tests.
* HitchCron_         - Mock cron server - to test applications require cron-like behavior.
* HitchSelenium_     - Simple wrapper around selenium to let you mock browser usage.
* HitchPostgres_     - Simple wrapper around Postgres.
* HitchSelenium_     - Simple wrapper around Selenium.
* HitchRedis_        - Simple wrapper around Redis.
* HitchDjango_       - Simple wrapper around Django.
* HitchCelery_       - Simple wrapper around Celery.

More coming soon.

Status
======

Hitch is currently in ALPHA. There may be bugs lurking and APIs may
change. However, since few people are using it I will be quick to provide
support and more open to feature requests during this period. It has been
tested on Ubuntu and Mac OS X. Currently, hitchserve will not run on Windows.



.. _HitchTest: https://github.com/hitchtest/hitchtest
.. _HitchServe: https://github.com/hitchtest/hitchserve
.. _HitchEnvironment: https://github.com/hitchtest/hitchenvironment
.. _HitchSMTP: https://github.com/hitchtest/hitchsmtp
.. _HitchCron: https://github.com/hitchtest/hitchcron
.. _HitchSelenium: https://github.com/hitchtest/hitchselenium
.. _HitchRedis: https://github.com/hitchtest/hitchredis
.. _HitchDjango: https://github.com/hitchtest/hitchdjango
.. _HitchPostgres: https://github.com/hitchtest/hitchpostgres
.. _HitchCelery: https://github.com/hitchtest/hitchcelery
.. _pipsi: https://github.com/mitsuhiko/pipsi

