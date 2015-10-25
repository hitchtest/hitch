Brittle Tests
=============

Brittleness is a property of tests which renders them liable to break easily despite the lack of bugs in the code.

Both :doc:`integration_testing` and :doc:`unit_testing` suffer from brittleness, although it is
usually a much bigger problem with with integration tests.

Brittleness can lead to :doc:`test_failure_habituation` and :doc:`test_abandonment`.

There are three major causes of brittleness in tests:

* :doc:`tight_coupling` in tests` (applies more to unit testing)
* A lack of test :doc:`isolation`. (applies more to integration testing)
* :doc:`sleep_oriented_testing` (applies more to integration testing)
* :doc:`indeterminacy` (applies more to integration testing)

The exhibition of brittleness means that a test has a *bug*.

However, solving those bugs is a hard engineering problem. Hard enough that
`even Google has trouble with it. <http://googletesting.blogspot.ch/2015/04/just-say-no-to-more-end-to-end-tests.html>`_.

Hitch provides boilerpate and features to *substantially* minimize brittle tests (see the causes listed above for details).
