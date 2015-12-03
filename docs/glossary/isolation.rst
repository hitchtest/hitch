Isolation
=========

Isolation is a property of tests that prevents their behavior from being affected by the state
of the system running them. It is a large and underappreciated problem when integration testing.

Non-isolated integration tests are often referred to as :doc:`/glossary/brittle_tests`.

Common examples of 'brittle' integration tests suffering from a lack of isolation include:

* Databases that are changed by one test and then re-used in subsequent tests.
* Files which are created by tests and not destroyed which affect the behavior of subsequent tests.
* A system package manager upgrading a crucial piece of software that the test relies upon, breaking it.
* A stray process monopolizing a network port used by the test.

Radical isolation is a primary goal of Hitch. Hitch achieves this by controlling as much
of the environment as is feasible and running a suite of checks for the rest.

* :doc:`/glossary/package_isolation`
* :doc:`/glossary/data_isolation`
* :doc:`/glossary/process_isolation`
* :doc:`/glossary/environment_isolation`


See also:

* :doc:`/glossary/test_realism`
* `Non-determinism by Martin Fowler <http://martinfowler.com/articles/nonDeterminism.html>`_
