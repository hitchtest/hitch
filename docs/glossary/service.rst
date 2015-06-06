Service
=======

A service in Hitch is a process which must be run for the
duration of the test.

It is either:

* A process that is running as part of the software under test.
* A process that is required for the software under test to function
(e.g. a database).
* A mock service - a service imitating a real external service
required by the software under test (e.g. :doc:`hitchsmtp`).

All services have a :doc:`setup` and :doc:`poststart` method that runs
just before the process starts and just after it is :doc:`ready`.

For example, the :doc:`postgres_service` runs the initdb command
in setup to create the database data directory and creates databases
and users specified in fixtures in poststart.

See also `Service (systems architecture) <https://en.wikipedia.org/wiki/Service_(systems_architecture)>`_.
