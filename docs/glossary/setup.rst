Setup
=====

Setup has two meanings in Hitch:

:doc:`service` setup
--------------------

Services in Hitch have a setup method, which is called before the service
is started.

See also :doc:`poststart`.


Testcase setUp
--------------

The harness TestCase class that you create to test your application inherits
from python's unittest TestCase class.

The setUp method is run before each test to create a running environment that
can be tested. It starts all services, sets up all :doc:`preconditions <precondition>`
and does any other miscellaneous setup required.
