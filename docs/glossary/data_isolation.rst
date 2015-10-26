Data Isolation
==============

Data isolation is a form of test :doc:`isolation` that
helps protect integration tests from being affected by the
current state of *data files* on the machine.

Lack of isolation is a common source of :doc:`/glossary/brittle_tests`.

Data isolation is an especially common problem for integration
tests that make use of databases.

The hitch database plugins maintain data isolation by creating
the database data directory *from scratch* at the beginning of
each test run before starting the service.

This helps provide a strong guarantee that previous test runs
will not affect subsequent test runs.

Hitch stores data files in the :doc:`/glossary/hitch_directory`.

See also:

* :doc:`/glossary/package_isolation`
* :doc:`/glossary/environment_isolation`
* :doc:`/glossary/process_isolation`
* :doc:`/faq/how_does_hitch_compare_to_other_technologies`
