Postgres
========

Install like so::

    $ hitch install hitchpostgres

To use, define the service after initializing the ServiceBundle object but before starting it.

.. code-block:: python

        import hitchpostgres

        # Service definition in engine's setUp:
        postgres_user = hitchpostgres.PostgresUser("newpguser", "pguserpassword")

        self.services['Postgres'] = hitchpostgres.PostgresService(
            version="9.3.6",                                                            # Mandatory
            port=15432,                                                                 # Optional (default: 15432)
            postgres_installation=hitchpostgres.PostgresInstallation(                   # Optional (default: assumes postgres commands are on path)
                bin_directory = "/usr/lib/postgresql/9.3/bin/"
            ),
            users=[postgres_user, ],                                                    # Optional (default: no users)
            databases=[hitchpostgres.PostgresDatabase("databasename", newpguser), ]     # Optional (default: no databases)
            pgdata=None,                                                                # Optional location for pgdata dir (default: put in .hitch)
        )


Once it is running, you can interact with the service::

        In [1]: self.services['Postgres'].databases[0].psql("-c", "SELECT * FROM yourtable;").run()
        [ Prints output ]

        In [2]: self.services['Postgres'].databases[0].psql().run()
        [ Launches into postgres shell ]


