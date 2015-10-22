Postgres
========

.. note::

    This documentation applies to the latest version of hitchpostgres.

HitchPostgres is a :doc:`/glossary/hitch_plugin` created to make testing applications that use Postgresql easier.

It contains:

* A :doc:`/glossary/hitch_package` to download and install postgresql.
* A :doc:`/glossary/service` to set up a test-specific postgresql environment and run postgresql.

Note: the postgresql service destroys and sets up a new database during each test run in order
to provide :doc:`/glossary/isolation` for your tests.

Installation
------------

First, install the the plugin in your tests directory::

    $ hitch install hitchpostgres


Set up postgres
---------------

In your test, define the postgres installation you will use, e.g. a system postgres:

.. code-block:: python

    import hitchpostgres

    postgres_package = hitchpostgres.PostgresPackage(
        version="9.3.9"  # Optional (default is the latest version of postgres)
    )

    # Downloads & installs Postgres to ~/.hitchpkg if not already installed by previous test
    postgres_package.build()


To use, define the service after initializing the :doc:`/api/service_bundle`:

.. code-block:: python

    # Define a postgresql user for your service to set up
    postgres_user = hitchpostgres.PostgresUser("newpguser", "pguserpassword")

    # Define a postgresql database for your service to set up
    postgres_database = hitchpostgres.PostgresDatabase(
        name="databasename",                  # Mandatory
        owner=newpguser,                      # Mandatory
        dump="dumps/yourdump.sql"             # Optional (default: create empty database)
    )

    self.services['Postgres'] = hitchpostgres.PostgresService(
        postgres_package=postgres_package,    # Mandatory
        port=15432,                           # Optional (default: 15432)
        users=[postgres_user, ],              # Optional (default: no users)
        databases=[postgres_database, ]       # Optional (default: no databases)
        encoding='UTF-8',                     # Optional (default: UTF-8)
        locale='en_US'                        # Optional (default: en_US)
        pgdata=None,                          # Optional location for pgdata dir (default: put in .hitch)
    )


Interacting with Postgres
-------------------------

Once it is running, you can interact with the service and its databases::

    In [1]: self.services['Postgres'].databases[0].psql("-c", "SELECT * FROM yourtable;").run()
    [ Prints output ]

    In [2]: self.services['Postgres'].databases[0].psql().run()
    [ Launches into postgres shell ]


