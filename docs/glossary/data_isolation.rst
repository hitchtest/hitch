Data Isolation
==============

Data isolation is a form of test :doc:`isolation` that
helps protect integration tests from being affected by the
current state of *data files* on the machine.

Lack of data isolation is a common source of :doc:`/glossary/brittle_tests`.

Data isolation is an especially common problem for integration
tests that make use of databases.

The hitch database plugins maintain data isolation by nuking
the database data directory and creating a new one *from scratch*
at the beginning of each test run, before starting the database
server and creating databases.

This helps provide an exceptionally strong guarantee that previous
test runs will not affect subsequent test runs.

Hitch stores data files in the :doc:`/glossary/hitch_directory`.

See also:

* :doc:`/glossary/package_isolation`
* :doc:`/glossary/environment_isolation`
* :doc:`/glossary/process_isolation`
* :doc:`/faq/how_does_hitch_compare_to_other_technologies`


http://googletesting.blogspot.com/2008/04/tott-avoiding-flakey-tests.html
