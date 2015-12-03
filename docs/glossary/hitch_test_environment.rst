Hitch Test Environment
======================

A hitch test environment is a computing environment in which hitch tests are run.
Generally there are two types of enviroment you would want to run tests on:

* :doc:`test_driven_development_environment`
* :doc:`continuous_integration_environment`
* :doc:`automated_exploratory_testing_environment`

Hitch uses :doc:`settings` to determine how the test should behave differently on
different environments (e.g. running firefox with XVFB on CI but not on TDD).

Hitch is currently restricted to running on UNIX system environments (for a full list
see :doc:`/misc/tested_on`), but it is capable of setting itself up with only a few
simple steps.
