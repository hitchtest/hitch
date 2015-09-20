How do I uninstall hitch completely?
====================================

If you want to remove all trace of hitch after installing it on your
machine, you just need to do the following::

  $ hitch cleanpkg

Followed by (this may requires sudo)::

  $ pip uninstall hitch

Additionally, you may want to:

* Delete the ~/.unixpackage directory.
* Delete the .hitch directory from your tests folder.

Note that the above will not uninstall system packages installed
during the course of running tests.
