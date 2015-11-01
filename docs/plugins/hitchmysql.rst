HitchMySQL
==========

.. note::

    This documentation applies to the latest version of hitchmysql.

HitchMySQL is a :doc:`/glossary/hitch_plugin` created to make testing applications that use MySQL easier.

It contains:

* A :doc:`/glossary/hitch_package` to download and install specified version(s) of MySQL.
* A :doc:`/glossary/service` to set up an isolated MySQL environment and run it.

Note: the MySQL service destroys and sets up a new database during each test run in order
to provide strict :doc:`/glossary/isolation` for your tests.

Installation
------------

First, install the the plugin in your tests directory::

    $ hitch install hitchmysql


Set up MySQL
------------

In your test, define the MySQL installation you want to test with:

.. code-block:: python

    import hitchmysql

    mysql_package = hitchmysql.MySQLPackage(
        version="5.6.26"  # Optional (default is the latest version of MySQL)
    )

    # Downloads & installs MySQL to ~/.hitchpkg if not already installed by previous test
    mysql_package.build()


To use, define the service after initializing the :doc:`/glossary/service_bundle` but before starting it:

.. note::

    See also: :doc:`/api/generic_service_api`

.. code-block:: python

    # Define a MySQL user for your service to set up
    mysql_user = hitchmysql.MySQLUser("newpguser", "pguserpassword")

    # Define a MySQL database for your service to set up
    mysql_database = hitchmysql.MySQLDatabase(
        name="databasename",                  # Mandatory
        owner=mysql_user,                      # Mandatory
        dump="dumps/yourdump.sql"             # Optional (default: create empty database)
    )

    self.services['MySQL'] = hitchpostgres.PostgresService(
        mysql_package=mysql_package,       # Mandatory
        port=13306,                        # Optional (default: 13306)
        users=[mysql_user, ],              # Optional (default: no users)
        databases=[mysql_database, ]       # Optional (default: no databases)
    )


Interacting with MySQL
----------------------

Once it is running, you can interact with the service and its databases::

    In [1]: self.services['MySQL'].databases[0].mysql("SELECT * FROM yourtable;").run()
    [ Prints output ]

    In [2]: self.services['MySQL'].databases[0].mysql().run()
    [ Launches into mysql shell ]


