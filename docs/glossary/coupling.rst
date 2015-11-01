Coupling
========

In computing and systems design a loosely coupled system is one in which each
of its components has, or makes use of, little or no knowledge of the
definitions of other separate components.

Applied to tests
----------------

Tests are essentially just software components. They are *always* coupled to
the code which they are testing, however they can be very tightly coupled or
they can be more loosely coupled.

Tight coupling between test code and application code is a common problem causing
:doc:`brittle_tests`. When application code is refactored, and that refactoring
changes the interface that code has to the world outside of its boundaries,
tests that relied upon that interface will break, *whether or not there was a bug*.

Such tests must either be refactored constantly alongside the code (which is a
higher maintenance cost), or be tossed out altogether.

Tight coupling is a problem that especially plagues :doc:`unit_testing` and
:doc:`low_level_testing`.


Applied to programming in general
---------------------------------

More tightly coupled code - sometimes described as a 'big ball of mud' or
'spaghetti code' is also harder and more expensive to test than loosely coupled code,
as well as harder to reason about.

Loosely coupled code, by contrast, is *much* easier to test, since the individual
modules can be tested individually (which is cheaper/quicker) and the reduced
interaction between these software modules makes it easier to reason about them.

See also:

* :doc:`/glossary/test_concreting`
* :doc:`/faq/why_just_html_ids_and_classes`
* :doc:`/faq/when_should_i_use_a_unit_test_and_when_should_i_use_an_integration_test`
* See: `Loose coupling wikipedia page <https://en.wikipedia.org/wiki/Loose_coupling>`_.
