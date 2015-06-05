Loaded
======

A :doc:`service` is loaded but not :doc:`ready` if the :doc:`setup` method
has completed, the service has been started and the service has issued
a log message indicating its readiness.

The :doc:`poststart` method is run when a service is loaded.
