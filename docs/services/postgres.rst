Postgres
========

.. note::

    This documentation applies to the latest version of hitchpostgres: version 0.3

Install the plugin::

    $ hitch install hitchpostgres

In your test, define the postgres installation you will use, e.g. a system postgres:

.. code-block:: python

    postgres_package = hitchpostgres.PostgresPackage(
        version="9.3.9",
        bin_directory="/usr/local/bin",
    )
    postgres_package.verify()

To use, define the service after initializing the ServiceBundle object but before starting it.

.. code-block:: python

    import hitchpostgres

    # Service definition in engine's setUp:
    postgres_user = hitchpostgres.PostgresUser("newpguser", "pguserpassword")

    self.services['Postgres'] = hitchpostgres.PostgresService(
        postgres_package=postgres_package,                                          # Mandatory
        port=15432,                                                                 # Optional (default: 15432)
        users=[postgres_user, ],                                                    # Optional (default: no users)
        databases=[hitchpostgres.PostgresDatabase("databasename", newpguser), ]     # Optional (default: no databases)
        pgdata=None,                                                                # Optional location for pgdata dir (default: put in .hitch)
    )


Once it is running, you can interact with the service::

    In [1]: self.services['Postgres'].databases[0].psql("-c", "SELECT * FROM yourtable;").run()
    [ Prints output ]

    In [2]: self.services['Postgres'].databases[0].psql().run()
    [ Launches into postgres shell ]


