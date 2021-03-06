Tested on
=========

Working on
----------

This is an list of environments that Hitch is tested on
and been found to work. If you use one of these environments
and you discover a problem, that's a bug. Please raise an issue.

OSes:

* Ubuntu 14.04
* Ubuntu 15.10
* Mac OS X Mavericks
* Mac OS X Yosemite
* Mac OS X Mavericks
* Debian Jessie
* Fedora 20
* CentOS 6.4
* Arch (latest rolling release)

Additionally, the following environments have been tested with and
seem to run Hitch okay:

* Docker
* Jenkins
* Travis CI


Not working on
--------------

This is a list of other UNIX systems that Hitch will not currently work on, but
might be made to function with with some work. If you really want one of these systems
to run hitch, that's a feature request. It may happen if you raise an issue.

* Mandriva
* OpenSUSE
* Mac OS X with macports
* BSD
* Gentoo
* Mac OS X with no package manager
* Slackware
* LFS


.. note::

    95% of getting these environments to work involves getting unixpackage to work with them.
    Please consider `helping out <https://github.com/unixpackage/unixpackage/blob/master/CONTRIBUTING.rst>`_
    with it if you'd like to one of these flavors of UNIX / environments supported.

This is a list of environments that probably aren't happening in the near future but may happen one day:

* Cygwin
* Windows


Untested but should still work
------------------------------

This is a list of environments that Hitch has *not* been tested on, but
hopefully should still work, but I'm not as confident about.

If it doesn't work, that's a bug. Please raise an issue if you find a problem.

If you have access to one of these, *please* try out the example project
and submit a pull request adding your environment if it works or raise
an issue if it doesn't:

* Red Hat
* Ubuntu/Debian based distros like Trisquel, Kali or Mint
* Red Hat based distros like Oracle Linux
* Linux systems not mentioned above
* Any continuous integration system not mentioned above
