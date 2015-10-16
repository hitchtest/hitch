Hitch Plugin
============

A hitch plugin is a python package installed into the hitch virtualenv
(contained in the .hitch directory) that provides test related
functionality.

The following are all hitch plugins:

* hitchtest - provides core testing functionality.
* hitchcli - for testing command line applications.
* hitchselenium - for testing web applications/websites.
* hitchpython - for testing python code.
* hitchpostgres -for testing code that uses postgres.

Plugins can be installed using the following command::

  $ hitch install pluginname

And they can be used in the engine.py by importing::

  import plugginname

Note that any python package available on pypi can also be installed
this way.

Do not confuse with the related :doc:`hitch_package`.
