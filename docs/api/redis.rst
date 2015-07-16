Redis
=====

.. note::

    This documentation applies to the latest version of hitchredis: version 0.3

Install the plugin::

    $ hitch install hitchredis

In your test, define the redis package you will use:

.. code-block:: python

    redis_package = hitchredis.RedisPackage(
        version="2.8.4",
        bin_directory="/usr/local/bin",
    )
    redis_package.verify()

To use, define the service after initializing the ServiceBundle object but before starting it.

.. code-block:: python

    self.services['Redis'] = hitchredis.RedisService(
        redis_package=redis_package                         # Mandatory
        port=16379,                                         # Optional (default: 16379)
    )

Once it is running, you can interact with the service::

    In [1]: self.services['Redis'].cli("-n", "1", "get", "mypasswd").run()
    [ prints contents of mypasswd variable ]
