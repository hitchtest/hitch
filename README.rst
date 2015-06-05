Hitch
======

Hitch is a loosely-coupled UNIX based testing framework built upon python's
unittest that helps you write simple, easy to read and easy to debug
tests for *any* software (not just web apps!).

It is divided into five components, all of which can be used individually,
together, or not at all. Those are:

* HitchTest     - simple declarative test description language based on YAML and jinja2.

* HitchServe    - simple service orchestration to allow for writing functional tests.
** HitchSMTP     - Mock SMTP server - to test email sending in your functional tests.
** HitchHTTP     - Mock HTTP server - mainly to test your application's use of REST APIs.
** HitchCron     - Mock cron server - to test applications require cron-like behavior.
** HitchSelenium - Simple wrapper around selenium to mock browser usage.
** HitchPostgres - Simple wrapper around Postgres.
** HitchSelenium - Simple wrapper around Selenium.
** HitchRedis    - Simple wrapper around Redis.
** HitchDjango    - Simple wrapper around Django.
** HitchCelery    - Simple wrapper around Celery.

Hitch was initially built to test Django applications, but it can be used to
write python tests for any application at all, *written in almost any
language* (PHP, Java, etc.). It is particularly well suited to testing
software that is built upon many interacting services.

Hitch also has an API to let you easily integrate services your applications
use which it does not have code for.

Hitch also makes it easy to write your own mock services - similar to SMTP or
HTTP, if, for example, your application must interact with an outside service
that speaks a different protocol, or speaks HTTP or SMTP but uses more complex
scripted interactions than HitchSMTP or HitchHTTP provide.

Hitch is currently in ALPHA. There may be bugs lurking and APIs may
change. However, since few people are using it I will be quick to provide
support and more open to feature requests during this period. It has been
tested on Ubuntu the most, but should work on any flavor of *nix, including
Mac OS X.


Getting Started
===============

There is currently one tutorial for Hitch:

* Getting started testing with Hitch and Django, Celery, Cron, Redis and Postgresql (INCOMPLETE)

If you want a tutorial for your stack, drop me a line.



Hitch Design
=============

Hitch was built to accommodate tests that follow the following principles,
as well as to follow them itself where applicable:

* Loose coupling
* Fail fast
* DRY
* FIRST principles of good tests:
** Fast
** Isolated
** Repeatable
** Self-verifying
** Timely

