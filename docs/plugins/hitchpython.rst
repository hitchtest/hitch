HitchPython
===========

.. note::

    This documentation applies to the latest version of hitchpython.

HitchPython is a :doc:`/glossary/hitch_plugin` specifically to make testing python code easier.

It contains:

* a :doc:`/glossary/hitch_package` to set up installations of python and a corresponding virtualenv for your project.
* A :doc:`/glossary/service` to run Django.
* A :doc:`/glossary/service` to run Celery.

Installation
------------

To install::

    $ hitch install hitchpython


Set up your test's virtualenv
-----------------------------

To create a virtualenv that your test can use, you need the following
in your :doc:`/glossary/test_setup`:

.. code-block:: python

    import hitchpython

    # Defines the python package
    python_package = hitchpython.PythonPackage(
        version="2.7.10"                                # Mandatory
    )

    # Downloads & installs python to ~/.hitchpkg if not already installed
    python_package.build()

    # python_package.python = "/path/to/projects/virtualenv/python"
    # python_package.pip = "/path/to/projects/virtualenv/pip"


Run Django Service
------------------

hitchpython also contains a service class that can be used to run
Django in your test.

To use, define the service after initializing the :doc:`/api/service_bundle`

.. code-block:: python

    # Service definition in setup:
    self.services['Django'] = hitchpython.DjangoService(
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

Once it is running, you can also interact with the service::

    In [1]: self.services['Django'].manage("help").run()
    [ Prints help ]

    In [2]: self.services['Django'].url()
    http://127.0.0.1:18080/

    In [3]: self.services['Django'].savefixture("fixtures/database_current_state.json").run()
    [ Saves the current state of the database as a fixture to file ]


Run Celery Service
------------------

hitchpython also contains a service class that can be used to run
Celery during your test.

To use, define the service after initializing the :doc:`/api/service_bundle`:


.. code-block:: python

    # Service definition in setup:
    self.services['Celery'] = hitchcelery.CeleryService(
        python=python_package.python,                     # Mandatory
        app="remindme",                                   # Mandatory
        beat=False,                                       # Optional (default: False)
        loglevel="INFO",                                  # Optional (default: INFO)
        concurrency=2,                                    # Optional (default: 2)
        broker=None,                                      # Optional (default: None)
        needs=[ self.services['Redis'], ]                 # Optional (default: no prerequisites)
    )

Once it is running, you can also interact with the service in a hitch step or with ipython::

    In [1]: self.services['Celery'].help().run()
    [ Prints help ]

    In [1]: self.services['Celery'].status().run()
    [ Prints celery queue status ]

    In [1]: self.services['Celery'].control(*args).run()
    [ Run specific celery control commands ]

    In [1]: self.services['Celery'].inspect(*args).run()
    [ Run specific celery inspect commands ]
