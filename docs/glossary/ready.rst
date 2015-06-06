Ready
=====

A :doc:`service` in Hitch can be said to be ready when:

* The :doc:`setup` method completes without errors.
* The process has started.
* The process has logged the :doc:`ready_line`.
* The :doc:`poststart` method has completed without errors.

The harness is ready when all services are ready.

See also :doc:`loaded`.
