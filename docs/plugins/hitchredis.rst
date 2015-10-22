Redis
=====

.. note::

    This documentation applies to the latest version of hitchredis.

HitchRedis is a :doc:`/glossary/hitch_plugin` specifically to make testing applications that use Redis easier.

It contains:

* A :doc:`/glossary/hitch_package` to download and install redis.
* A :doc:`/glossary/service` to run Redis.


Installation
------------

If it is not already installed, install the hitchredis package::

    $ hitch install hitchredis


Set up Redis
------------

In your test, define the redis package you will use:

.. code-block:: python

    import hitchredis

    redis_package = hitchredis.RedisPackage(
        version="2.8.4"                         # Optional (default is the latest version of redis)
    )

    # Downloads & installs redis to ~/.hitchpkg if not already installed
    redis_package.build()

To use, define the service after initializing the :doc:`/api/service_bundle`:

.. code-block:: python

    self.services['Redis'] = hitchredis.RedisService(
        redis_package=redis_package                         # Mandatory
        port=16379,                                         # Optional (default: 16379)
    )


Interacting with Redis
----------------------

Once it is running, you can interact with the service::

    In [1]: self.services['Redis'].cli("-n", "1", "get", "mypasswd").run()
    [ prints contents of mypasswd variable ]
