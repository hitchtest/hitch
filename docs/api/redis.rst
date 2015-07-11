Redis
=====

Install like so::

    $ hitch install hitchredis

To use, define the service after initializing the ServiceBundle object but before starting it.

.. code-block:: python

        self.services['Redis'] = hitchredis.RedisService(
            version="2.8.4"                                     # Mandatory
            redis_exec="redis-server",                          # Optional (default: redis-server)
            redis_cli="redis-cli",                              # Optional (default: redis-cli)
            port=16379,                                         # Optional (default: 16379)
        )

Once it is running, you can interact with the service::

    In [1]: self.services['Redis'].cli("-n", "1", "get", "mypasswd").run()
    [ prints contents of mypasswd variable ]
