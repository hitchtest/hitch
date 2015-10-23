Hitch
=====

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/hitchtest/hitch
   :target: https://gitter.im/hitchtest/hitch?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

Hitch is a UNIX-based testing framework for writing integration tests with an emphasis on:

* Test realism
* Test readability
* Loose coupling
* Minimizing or eliminating brittle tests
* Tests that fail fast and fail clearly

Available plugins
-----------------

Hitch comes with a variety of plugins to aid you to realistically testing various
kinds of software, components and scenarios, including:

* Python code (including Django and Celery)
* Postgresql
* Redis
* Web apps (using selenium)
* Command line apps (using pexpect)
* Cron
* MySQL
* RabbitMQ
* Elastic Search

Read more here: https://hitchtest.readthedocs.org/en/latest/plugins/

Getting started
---------------

See the quickstart tutorial on how to get started testing an existing project:

https://hitchtest.readthedocs.org/en/latest/quickstart/index.html

Also check out https://github.com/pydanny/cookiecutter-django if you want to start a
new Django project and need something to test it with.

Status
------

Hitch is currently in beta.

It is tested on Mac OS X Yosemite, Ubuntu, Debian, Fedora and Arch Linux. It does not currently work on Windows.

See : https://hitchtest.readthedocs.org/en/latest/misc/tested_on.html for details about how the framework itself is tested.


Contents of this project
------------------------

This project contains:

* The code for the bootstrapper script
* Documentation for the whole project (hosted at readthedocs: https://hitchtest.readthedocs.org/en/latest/)

To see the code for other components, see: https://github.com/hitchtest/
