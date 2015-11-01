Integration Testing
===================

Integration testing is a form of testing which tests the interaction of
software modules with one another and with the outside world.

Integration tests are usually, although not always, higher level tests.

Common problems with integration testing are:

* :doc:`/glossary/brittle_tests`
* Maintaining :doc:`test_realism`
* Maintaining :doc:`test_readability`
* Enforcing loose doc:`coupling`
* Building tests that :doc:`/glossary/fail_fast` and :doc:`/glossary/fail_clearly`.
* Speed

Hitch attempts to solve or minimize all of these problems.

.. warning::

    Do not confuse integration testing with :doc:`end_to_end_testing`. End to end testing
    *is* :doc:`integration_testing` but integration testing is not necessarily
    end to end testing. See also :doc:`combinatorial_explosion`.

See also:

* :doc:`/faq/when_should_i_use_a_high_level_test_and_when_should_i_use_a_low_level_test`
* :doc:`/faq/when_should_i_use_a_unit_test_and_when_should_i_use_an_integration_test`
* :doc:`unit_testing`
* :doc:`high_level_testing`
