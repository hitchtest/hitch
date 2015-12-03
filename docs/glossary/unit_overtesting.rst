Unit Overtesting
================

Unit overtesting is a :doc:`testing_antipattern` where unit tests are
overused to test :doc:`integration_code`.

Unit tests used to test integration code do provide protection from
:doc:`logical_bugs` but they usually do not catch :doc:`integration_bugs`.
Integration tests will catch both logical bugs and integration bugs.
