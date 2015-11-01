Isolation
=========

Isolation is a property of tests that prevents system state from 'contaminating' the
test environment.

*Lack* of isolation is usually the cause of :doc:`/glossary/brittle_tests`.

Tests that show a high degree of isolation strictly control their own environment wherever
possible and where they cannot, they :doc:`/glossary/fail_fast` and :doc:`/glossary/fail_clearly`.

Common examples of 'brittle' integration tests suffering from a lack of isolation include:

* Databases that are changed by one test and then re-used in subsequent tests.
* Files which are created by tests and not destroyed, affecting the behavior of subsequent tests.
* A lack of control over crucial software which the test relies upon (e.g. because system package manager software was used).
* Accidentally using the same service from a previous test run because it was not shut down properly.

Hitch maintains three types of isolation:

* :doc:`/glossary/package_isolation`
* :doc:`/glossary/data_isolation`
* :doc:`/glossary/process_isolation`

Strict isolation in integration tests is analogous to the concept of strict typing in programming
languages.

See also:

* :doc:`/glossary/test_realism`
* `Non-determinism by Martin Fowler <http://martinfowler.com/articles/nonDeterminism.html>`_
