Isolation
=========

Isolation is a property of tests that prevents system state from 'contaminating' the environment.

*Lack* of isolation is a common cause of :doc:`/glossary/brittle_tests`.

Tests that show a high degree of isolation should control their own environment wherever
possible and where they cannot, :doc:`/glossary/fail_fast` and :doc:`/glossary/fail_clearly`.

Common examples of integration tests that suffer from a lack of isolation include:

* Databases that are changed by one test and then used in subsequent tests.
* Files which are created by tests and not destroyed, affecting the behavior of subsequent tests.
* A lack of control over crucial software which the test relies upon (e.g. using the system package manager's database).
* Accidentally using the same service from a previous test run because it was not shut down properly.
