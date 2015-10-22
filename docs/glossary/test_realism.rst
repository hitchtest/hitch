Test Realism
============

Test realism is the level of realism in the scenarios mocked by your tests.

Examples:

* A test that uses real data from production is more realistic than tests that don't.
* A test that doesn't use a browser to test a web application is less realistic than one that does.
* A test that runs code with the exact database version used in production is more realistic than one that uses a later or earlier version.

In general:

* The more things that your tests mock, the less realistic a test is.
* The more realistic a test is, the slower and more expensively it will run, but *the more bugs it will catch*.

Hitch aims to make it easy to produce tests that are as realistic as possible and yet still
fast enough that they can be used to develop against.

See also:

* :doc:`/faq/when_should_i_use_a_unit_test_and_when_should_i_use_an_integration_test`
* :doc:`/faq/why_is_my_test_downloading_and_compiling_software`
* :doc:`/faq/why_does_the_first_test_run_take_so_long`
