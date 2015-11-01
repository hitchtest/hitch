Process Isolation
=================

Process isolation is a form of test :doc:`isolation` that
helps protect integration tests from being affected by the
behavior of processes running on its machine.

Lack of process isolation is a common source of :doc:`/glossary/brittle_tests`.

Hitch enforces process isolation via the following mechanisms:

* Starting *all* processes the test relies upon itself - database, redis, web server, etc.
* Monitoring these processes and failing quickly with a clear message if any of them die early with an error.
* Ordering all processes to stop at the end of a test (SIGTERM) and killing them (SIGKILL) if they do not respond.
* Killing their children and grandchildren too, if the process stops responding (with SIGKILL).
* Failing quickly with a clear message if another process is using a network port your test will need (this is also environmental isolation)s.

See also:

* :doc:`/glossary/package_isolation`
* :doc:`/glossary/environment_isolation`
* :doc:`/glossary/process_isolation`
* :doc:`/faq/how_does_hitch_compare_to_other_technologies`
