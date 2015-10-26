Loose coupling
==============

In computing and systems design a loosely coupled system is one in which each
of its components has, or makes use of, little or no knowledge of the
definitions of other separate components.

See: `Loose coupling wikipedia page <https://en.wikipedia.org/wiki/Loose_coupling>`_.

Applied to tests
----------------

Tests must be coupled to the code which is under test, however the degree of coupling
is often flexible. Tests can know a little or a lot about the code which they are testing.

Tight coupling between test code and application code is a common problem causing
:doc:`brittle_tests`. When application code is refactored, changing its interface,
this can often break tests that are coupled to its interface despite not causing any bugs.

Unit tests are especially susceptible to this problem - lower level tests by their
nature must be more tightly coupled to your implementation.

See:

* :doc:`/glossary/test_concreting`
* :doc:`/faq/why_just_html_ids_and_classes`
* :doc:`/faq/when_should_i_use_a_unit_test_and_when_should_i_use_an_integration_test`
