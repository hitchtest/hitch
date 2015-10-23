hitchreqs.txt
=============

hitchreqs.txt is a file containing a list of hitch plugins required
by your testing environment, their current versions and their
dependencies.

All of the plugins are python packages hosted on pypi. Many have
dependencies.

hitchreqs.txt is read by "hitch init" when you first run it in order
to determine which hitch plugins to install and run.

When "hitch init" is run in a pre-initialized environment it attempts
to ensure that all of the packages are installed and the correct version.

When you run "hitch upgrade", hitch attempts to upgrade all plugins to
their latest versions and records the versions in hitchreqs.txt.

When you run "hitch install", hitch installs the latest version of a
plugin and its dependencies and saves its version to hitchreqs.txt.

See also:

* :doc:`hitch_plugin`
* Not to be confused with :doc:`hitch_package`
