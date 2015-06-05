Time Travel
===========

Time travel in saddle is a process by which the system time is
faked for the services run by the service engine.

You can skip forward in time using the following commands::

    >>> import datetime
    >>> self.time_travel(datetime.timedelta(days=30))
