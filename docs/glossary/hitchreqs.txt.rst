hitchreqs.txt
=============

hitchreqs.txt is a file containing a list of :doc:`hitch_plugin`s required
by your testing environment, and their versions.

It is read by "hitch init" when you first run it in order to determine
which plugins and which plugin versions to run.

When "hitch init" is run in a pre-initialized environment it attempts
to ensure that all of the packages are installed and the correct version.

When you run "hitch upgrade", hitch attempts to upgrade all plugins to
their latest versions and records them in hitchreqs.txt.

When you run "hitch install", hitch installs a plugin and its dependencies
and saves those to hitchreqs.txt.

.. note::

    For python programmers: yes, it is just a requirements.txt and those
    are all valid python packages hosted on pypi.
