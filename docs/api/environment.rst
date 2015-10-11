Environment Checks
==================

.. note::

    This documentation applies to the latest version of hitchtest.

This feature is to help prevent those hours spent tracking down why your test
failed on one machine (e.g. your coworkers' or your continuous integration machine)
but not another, and it ended up being related to that machine's environment.

Hitch provides a variety of checks which you can use to verify that the environment
you are running the test in is suitable to run the test in. If a problem with the
environment is detected the test fails *immediately* with a clear error indicating
the kind of fix required rather than failing later with an obscure, hard to debug
error.

This feature is based upon the twin principles of :doc:`/glossary/isolation` and
:doc:`/glossary/fail_fast`.

To use these checks, simply put them in your settings file under the property 'environment'
or use them in your code as described.

This list of checks is by no means all that you might need. Additional ideas for environment
checks are very welcome. If there is one that you want, please raise an issue at
http://github.com/hitchtest/hitchtest/issues/create



System Packages
---------------

This check verifies that a unixpackage package is installed:

.. code-block:: yaml

  environment:
    - packages:
      - libtool
      - libpq-dev

.. code-block:: python

  from hitchtest.environment import checks
  checks.packages(["libtool", "libpq-dev", ])

This is a simple way of checking, in a *UNIX platform indendent* way if a list of
packages are installed.

The package names used are, by default, Ubuntu package names. Note that the list
of checkable packages is not very long, but if you want to use one which is not
currently recognized, you can fork and issue a pull request to this repository:
http://github.com/unixpackage/unixpackage.github.io


Debs
----

This check verifies that a particular set of debian packages are installed:

.. code-block:: yaml

  debs:
    - node-less

.. code-block:: python

  from hitchtest.environment import checks
  checks.debs(["node-less", ])

If it is run on a non-debian system, this check is skipped.


Brew
----

This check verifies that a particular set of brew packages are installed:

.. code-block:: yaml

  brew:
    - libtool
    - automake

.. code-block:: python

  from hitchtest.environment import checks
  checks.brew(["libtool", "automake", ])

If it is run on a non-Mac OS system or on a Mac OS system without brew installed,
this check is skipped.


Internet detected after
-----------------------

This check should be used for all tests that rely upon access to the internet
to function.

This check pings 8.8.8.8 (google DNS servers). If there is no valid response after
the specified number of seconds, it fails:

.. code-block:: yaml

  internet_detected_after: 15

As soon as there is a response, the test will continue.



Free ports
----------

This check verifies that the specified ports are not currently in use and
fails if they are:

.. code-block:: yaml

  environment:
    - freeports:
      - 18080
      - 15432


Approved platforms
------------------

This check verifies that the test is being run on an approved platform:

.. code-block:: yaml

  approved_platforms:
    - darwin
    - linux

The platform type is checked against python's 'sys.platform'.


System bits
-----------

This check verifies that your system is either 32 bit or 64 bit:

.. code-block:: yaml

  systembits: 64
