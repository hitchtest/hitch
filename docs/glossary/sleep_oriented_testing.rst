Sleep oriented testing
======================

Sleep oriented testing is a common :doc:`testing_antipattern` done when
:doc:`integration_testing`, whereby waiting steps are added that
sleep for a specified duration (e.g. one second) in
order to wait for an event to take place that will
allow the test to continue.

Examples of such events:

* Waiting for a UI element to appear in a page before clicking.
* Waiting or an email to arrive.
* Waiting for row to appear in a database.
* Waiting for file to appear or to change.

Sleep oriented testing causes :doc:`brittle_tests`, since the
sleep is a source of :doc:`indeterminacy`.

See also :doc:`event_oriented_testing`.

Hitch provides a number of features to
