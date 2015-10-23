Brittle Tests
=============

Brittleness is a property of tests which renders them liable to break easily despite the lack of bugs in the code.

Brittleness can lead to :doc:`test_failure_habituation` and :doc:`test_abandonment`.

Solving brittleness in tests is a *hard* engineering problem. `Even Google has this problem. <http://googletesting.blogspot.ch/2015/04/just-say-no-to-more-end-to-end-tests.html>`_

The following are real life examples of tests failures caused by brittle tests:

* Running a system upgrade upgrades the version of python from 2.6 to 2.7, which breaks code that is reliant upon the system python, breaking the test.
* A "sleep" step which waits for an email to be sent before checking for its arrival fails when run on a different machine owing to that machine taking longer to send the email.
* A test which uses a mock object to mock and SMTP client object which breaks if one SMTP client is swapped out with a different client.
* A test that passes on one machine but fails on another because a certain system package was not installed.

Hitch *substantially* minimizes brittleness / false positives with the following features:

* :doc:`event_oriented_testing`
* The :doc:`hitch_package`
* :doc:`/api/environment` checks
* Enforced :doc:`loose_coupling`
* Enforced :doc:`isolation`

See also:

* :doc:`indeterminacy`.
* :doc:`sleep_oriented_testing`
* :doc:`tightly_coupled_tests`
