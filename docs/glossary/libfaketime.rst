libfaketime
===========

libfaketime intercepts various system calls which :doc:`services <service>`
use to retrieve the current date and time. It can then report faked dates
and times (specified by you, the user) to these services.

It is currently *included* in Hitch and compiled for your architecture upon
installation (e.g. from pypi).

It works on Linux and Mac OS.

This can be used to ascertain that the services you run behave correctly
when they are moved forward to specific points in time.

Libfaketime has the following known issues:

* Java -- Java apps do not pick up the faked time correctly.
* NodeJS -- currently breaks all node.js apps in recent linux kernels.
* Windows -- does not work at all on Windows.


See: `Libfaketime Project Page <https://github.com/wolfcw/libfaketime>`_
