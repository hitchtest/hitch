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

Tight coupling between test code and application code is a common cause of
:doc:`brittle_tests`. When application code is refactored and that refactoring
changes the interface that code has to the world outside of its boundaries,
tests that were coupled to that that interface will break,
*regardless of whether there was a bug*.

This causes three enormous problems:

* Developers have to throw away the tests. This is a waste. This decreases test coverage.
* Developers have to constantly refactor their tests. This is also a waste. Less coupled tests do not have to be refactored.
* *Most* commonly, developers circumvent both problems and the project suffers from :doc:`/glossary/test_concreting`.

Tight coupling is a problem that plagues :doc:`low_level_testing` and :doc:`unit_testing`
especially.


Applied to programming in general
---------------------------------

More tightly coupled code - sometimes described as a 'big ball of mud' or
'spaghetti code'. It is harder and more expensive to test than loosely coupled code,
as well as harder to reason about.

Loosely coupled code, by contrast, is *much* easier to test, since the individual
modules can be tested individually (which is cheaper/quicker) and the reduced
interaction between these software modules makes it easier to reason about them.

There is virtually *never* an instance where decoupling components in a software
system is not a good idea. Decoupling is a good thing to do when refactoring.

See also:

* :doc:`/glossary/test_concreting`
* :doc:`/faq/why_just_html_ids_and_classes`
* :doc:`/faq/when_should_i_use_a_unit_test_and_when_should_i_use_an_integration_test`
* See: `Loose coupling wikipedia page <https://en.wikipedia.org/wiki/Loose_coupling>`_.
