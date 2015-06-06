Stop
====

In Hitch, the a 'stop' message is sent under the following circumstances:

* At the end of a successfully completed test with no errors.
* Once an error is detected during a test.
* If a user hits ctrl-C.

The :doc:`service_engine` reacts to the stop message by sending a SIGINT and
SIGQUIT signal to every service near-simultaneously.

The service engine waits until all of the services have closed or until
the :doc:`shutdown_timeout` expires, whichever comes first.

If the shutdown timeout expires, a SIGKILL signal is sent to all remaining
services.
