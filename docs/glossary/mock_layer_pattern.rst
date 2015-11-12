Mock Layer Pattern
==================

The mock layer pattern is a :doc:`testing_pattern` and coding pattern
where core code that is built by :doc:`manual_test_driven_development`
is segregated from code that is built by :doc:`acceptance_test_driven_development`.

It is used to provide the benefits of acceptance test driven development
for a core system while reducing the :doc:`cost_of_building_a_test_harness`
to an acceptable level.

Example:

If you have an architecture as follows:

Core system <-> Driver for custom hardware <-> Custom Hardware

The mock layer pattern can be applied like so when building an extension to a core system:

* Create a driver for the custom hardware using :doc:`manual_test_driven_development`
* Ensure that there is very loose :doc:`coupling` between the core system and the driver for custom hardware.
* Move as much business logic and complexity as possible into the core system.
* Use :doc:`acceptance_test_driven_development` on the core system.
* Create a mock for the driver for use with the core system.
* For all subsequent updates to the driver, use :doc:`manual_test_driven_development`.

The mock layer pattern can also be applied when refactoring code.
