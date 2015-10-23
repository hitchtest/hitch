Test Realism
============

The level of realism in the scenarios recreated by your tests.

For example:

* A test that uses real data from a live database is more realistic than tests that do not.
* A test that doesn't use a browser to test a web application is less realistic than one that does.
* A test that runs code with the exact database version used in production is more realistic than one that doesn't.

In general:

* The less realistic a test set up is, the harder it is to create a test with it which reproduces a bug reported by a user.
* Highly realistic tests catch substantially more bugs than unrealistic tests.
* Realism often comes at the expense of test speed, cost and convenience.

Hitch aims to make it easy to create integration tests that are as realistic as possible and yet still
fast enough on modern hardware that they can be effectively used to do test driven development.

Unlike many other frameworks, hitch *explicitly prioritizes realism over speed*.

Tests that are more realistic are sometimes described as "closer to production".

See also:

* :doc:`/faq/when_should_i_use_a_unit_test_and_when_should_i_use_an_integration_test`
* :doc:`/faq/why_is_my_test_downloading_and_compiling_software`
* :doc:`/faq/why_does_the_first_test_run_take_so_long`
* :doc:`/howto/refactor_your_tests`
