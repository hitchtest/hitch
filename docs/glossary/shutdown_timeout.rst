Shutdown timeout
================

Shutdown timeout is the duration which saddle waits after
sending a SIGINT/SIGQUIT before sending a SIGKILL.

Unless directly specified, it is assumed that the shutdown
timeout is the same as the global timeout.

See also:

* :doc:`stop`
* :doc:`timeout`
