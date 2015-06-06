Service engine
==============

The service engine is the beating heart of :doc:`hitchserve`. It runs all :doc:`setup`
and :doc:`poststart`, code, it starts all the services and aggregates all of their
output into the output of the test itself.

The service engine also passes messages between the test and the services -
e.g. the :doc:`stop` message or exceptions.
