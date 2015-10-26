Service Bundle
==============

A service bundle is a :doc:`/glossary/hitchserve` object which runs one or more services together
so that, as a group, they can be tested.

It does the following and more:

* Starts the services together in parallel, except where service dependencies are defined.
* Starts the services with libfaketime so that tests can tell the services that time has passed.
* Provides a convenience function to let the tester/developer connect to any of the services' IPython kernels.
* Shuts the services down at the end and SIGKILLs them *and their children* if they refuse to die.

See also:

* :doc:`service`
