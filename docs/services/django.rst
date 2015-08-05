Django
======

.. note::

    This documentation applies to the latest version of hitchpython: version 0.2


First, if it is not already installed, install the hitch python package::

    $ hitch install hitchpython

To use, define the service after initializing the ServiceBundle object but before starting it.

Like so:

.. code-block:: python

    # Imports
    import hitchpython

    # Service definition in engine's setUp:
    self.services['Django'] = hitchpython.DjangoService(
        version="1.8",                       # Django version. Mandatory
        python=python_package.python,        # Python executable path. Mandatory
        port=18080,                          # Optional (default: 18080)
        managepy=None,                       # Optional full path to manage.py (default: None, assumes in project directory)
        settings="remindme.settings",        # Optional (default: settings)
        fixtures=['fixture1.json',],         # Optional (default: None)
        sites=False,                         # Optional (default: False - Put http://127.0.0.1:18080/ (with specified port) into django_sites table.)
        syncdb=False,                        # Optional (default: False - Run syncdb (for versions of django below 1.8))
        migrations=True,                     # Optional (default: True - Run migrate (for Django 1.8 or earlier versions using South))
        needs=[self.services['Postgres'], ]  # Optional (default: no prerequisites)
    )

Once it is running, you can interact with the service::

    In [1]: self.services['Django'].manage("help").run()
    [ Prints help ]

    In [2]: self.services['Django'].url()
    http://127.0.0.1:18080/

    In [3]: self.services['Django'].savefixture("fixtures/database_current_state.json").run()
    [ Saves the current state of the database as a fixture to file ]
