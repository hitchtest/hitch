Sleep oriented testing
======================

Sleep oriented testing is a common anti-pattern in
functional testing, whereby waiting steps are added that
sleep for a specified duration (e.g. one second) in
order to wait for an event to take place that will
allow the test to continue.

Examples of such events:

* Waiting for a UI element to appear in a page before clicking.
* Waiting or an email to arrive.
* Waiting for row to appear in a database.
* Waiting for file to appear or to change.

Sleep oriented testing causes the following problems
(in order of importance):

* It reduces repeatability - the test can behave differently and fail differently on different computers owing to the different speeds in which they take place.
* It reduces speed - waiting 30 seconds for an event that may take between 10 and 20 seconds is slower than simply waiting for the event and continuing.

See also :doc:`event_oriented_testing`.
