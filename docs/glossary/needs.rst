Needs
=====

By default, all services are started simultaneously.

If you have one service which requires another to be set up
before it is run (e.g. django requires postgres and redis),
you can add a list of services that the service 'needs', and
the service engine will not start it until those services
are ready.

Once all services are started and ready, the engine
is declared ready.

The :doc:`service engine` determines service readiness
and starts services accordingly.
