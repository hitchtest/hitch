Why is Hitch so fast?
=====================

There are two main reasons why Hitch is generally faster than other testing
frameworks: parallelization and built in epoll/kqueue triggers.

Automatic Parallelization
-------------------------

When hitch services are started they are started in parallel by default. If
you have seven services (like the example project), hitch will try to start
all of the services that do not have a "needs" property set. As soon as
services are ready that are prerequisites of other services, those will be
started.

This means two things: even very complex service architectures can be
started extremely quickly and also that your test speed will increase
substantially the more CPU power, RAM and CPU cores you have.

As an example, the django-remindme-tests project runs the following
services:

* Postgresql (including running initdb to create all necessary database
files and creating a user and database after service start-up)
* Django (including installing fixtures and running migrations)
* Mock Cron server
* Mock SMTP server
* Celery
* Redis
* Selenium (running and connecting to firefox).

When tested on a laptop with an SSD, and an i5 processor with 4 CPU cores,
just starting firefox takes 4.5 seconds. *All* of the above, when
parallelized, takes between 5.1 and 5.8 seconds.


Epoll/Kqueue Triggers
---------------------

A common feature of other testing frameworks is the use of 'sleeps' and
polling to determine if an event has occurred. This can not only contribute
to test indeterminacy, it slows down your integration tests.

A feature of hitch that contributes to its speed is the in-built use of
epoll/kqueue triggers. These are kernel features in Linux, FreeBSD and Mac
OS X that allow 'watches' to be put on files. When a file is changed, the
test is automatically notified without the need for polling.

This is used in the following situations:

* To ascertain service readiness - the instant that Postgresql logs the
line "database system is ready to accept connections", for example, Hitch
will move straight on to creating users and databases.

* Mock service interactions - the instant that the mock SMTP server
receives an email, it logs out a snippet of JSON. The watcher on the mock
SMTP logs receives the epoll trigger during that split second and the test
can continue.

