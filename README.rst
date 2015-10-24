Hitch
=====

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/hitchtest/hitch
   :target: https://gitter.im/hitchtest/hitch?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge

Hitch is a UNIX-based testing framework for writing integration tests with an emphasis on:

* Minimizing and eliminating `brittle tests <https://hitchtest.readthedocs.org/en/latest/glossary/brittle_tests.html>`_
* `Test readability <https://hitchtest.readthedocs.org/en/latest/glossary/test_readability.html>`_
* `Loose coupling <https://hitchtest.readthedocs.org/en/latest/glossary/loose_coupling.html>`_
* `Test realism <https://hitchtest.readthedocs.org/en/latest/glossary/test_realism.html>`_
* Tests that `fail fast <https://hitchtest.readthedocs.org/en/latest/glossary/fail_fast.html>`_ and `fail clearly <https://hitchtest.readthedocs.org/en/latest/glossary/fail_clearly.html>`_

Available plugins
-----------------

Hitch comes with a variety of plugins to aid you to realistically testing various
kinds of software, components and scenarios, including:

* `Python <https://hitchtest.readthedocs.org/en/latest/plugins/hitchpython.html>`_ (includes Django and Celery service definitions)
* `Postgresql <https://hitchtest.readthedocs.org/en/latest/plugins/hitchpostgres.html>`_
* `Redis <https://hitchtest.readthedocs.org/en/latest/plugins/hitchredis.html>`_
* `Web apps (using selenium) <https://hitchtest.readthedocs.org/en/latest/plugins/hitchselenium.html>`_
* Command line apps (using pexpect)
* `Cron <https://hitchtest.readthedocs.org/en/latest/plugins/hitchcron.html>`_
* MySQL
* RabbitMQ
* Elastic Search

`Plugin documentation <https://hitchtest.readthedocs.org/en/latest/plugins/>`_

Getting started
---------------

See the `quickstart tutorial <https://hitchtest.readthedocs.org/en/latest/quickstart/index.html>`_ on how to
get started testing an existing project.

Also check out `cookiecutter-django <https://github.com/pydanny/cookiecutter-django>`_
if you want to start a new Django project with tests.

Status
------

Hitch is currently in beta.

It is regression tested on:

* Operating Systems : Mac OS X Yosemite, Ubuntu, Debian, Fedora and Arch Linux.
* Python versions : 3.5.0, 3.4.3, 3.4.0 and 3.3.0 `(what about python 2?) <https://hitchtest.readthedocs.org/en/latest/faq/what_about_python2.html>`_

It does not currently work on Windows.



See `tested on <https://hitchtest.readthedocs.org/en/latest/misc/tested_on.html>`_ for more details on
how the framework is tested (with itself, naturally).

Contents of this project
------------------------

This project contains:

* The code for the bootstrapper script
* Documentation for the whole project (`hosted at readthedocs <https://hitchtest.readthedocs.org/en/latest/>`_)
* Code for other components is at: https://github.com/hitchtest/
