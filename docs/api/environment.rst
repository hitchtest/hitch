Environment API
===============

Hitch provides a group of checks which you can use to verify that the environment
you are running the test in is suitable for it. If a problem with the environment is
detected, the test fails early, with a clear error. This feature is to enable your
tests to adhere to the twin principles of :doc:`/glossary/isolation` and :doc:`/glossary/fail_fast`.

To use these checks, simply put them in your settings file under the property 'environment'.

Free ports
----------

This check verifies that the following ports are not currently in use:

.. code-block:: yaml

  freeports:
    - 18080
    - 15432

Debs
----

This check verifies that a particular set of debian packages are installed:

.. code-block:: yaml

  debs:
    - node-less

If it is run on a non-debian system, this check is skipped.

Brew
----

This check verifies that a particular set of brew packages are installed:

.. code-block:: yaml

  brew:
    - libtool
    - automake

If it is run on a non-Mac OS system with brew installed, this check is skipped.

System bits
-----------

This check verifies that your system is either 32 bit or 64 bit:

.. code-block:: yaml

  systembits: 64

Internet detected after
-----------------------

This check pings 8.8.8.8 (google DNS servers). If there is no valid response after
the specified number of seconds, it fails:

.. code-block:: yaml

  internet_detected_after: 2

Approved platforms
------------------

This check verifies that the test is being run on an approved platform:

.. code-block:: yaml

  approved_platforms:
    - darwin
    - linux

The platform type is checked against python's 'sys.platform'.
