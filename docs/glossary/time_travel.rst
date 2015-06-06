Time Travel
===========

Time travel in Hitch is a process by which the system time is
faked for the services run by the service engine.

You can skip forward in time using the following commands::

    >>> self.services.time_travel(minutes=30)
    >>> self.services.time_travel(hours=30)
    >>> self.services.time_travel(days=30)
