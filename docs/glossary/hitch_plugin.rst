Hitch Plugin
============

A hitch plugin is a python package installed into the hitch virtualenv
(contained in the .hitch directory) that provides test related
functionality.

The functionality contained for most plugins is either:

* One or more :doc:`hitch_package`
* One or more :doc:`service`
* A :doc:`step_library`.

The following are all hitch plugins:

* hitchcli - contains a step library for testing command line applications.
* hitchselenium - a service to run firefox and a step library to interact with it via selenium.
* hitchpython - a hitch package for python and a service for Celery and Django.
* hitchpostgres - for hitch package for Postgres and a service for Postgres.

Plugins can be installed using the following command::

  $ hitch install pluginname

And they can be used in the engine.py by importing at the top of engine.py::

  import plugginname

Note that *any* python package available on pypi can also be installed
via 'hitch install' and used in your engine.

See also: :doc:`hitch_package`
