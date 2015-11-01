Brittle Tests
=============

Brittleness is a property of tests which renders them likely to break easily
despite the lack of bugs in the code.

Brittleness can lead in extreme cases to :doc:`test_failure_habituation` and
:doc:`test_abandonment`.

There are six major causes of brittleness in tests:

* A lack of :doc:`data_isolation`.
* A lack of :doc:`environment_isolation`.
* A lack of :doc:`process_isolation`.
* A lack of :doc:`package_isolation`.
* Tight :doc:`coupling` between tests and code.
* :doc:`sleep_oriented_testing`.

Hitch implements features and a project structure to help protect your tests
against all six sources of brittle test bugs while :doc:`integration_testing`.

See also:

* `Non-determinism by Martin Fowler <http://martinfowler.com/articles/nonDeterminism.html>`_
* `Google not-so-wisely calling their own brittle tests a 'fact of life' <http://googletesting.blogspot.ch/2015/04/just-say-no-to-more-end-to-end-tests.html>`_
