Package Isolation
-----------------

Package isolation is a form of :doc:`isolation` enforced
by hitch that protects tests against failure caused by
the state of package installation.

Lack of package isolation is a common source of :doc:`/glossary/brittle_tests`.

This could mean test failures caused by *not having* software
installed, having the *wrong version* of software installed or
having *damaged* software installed.

Hitch provides package isolation in several ways:

* Hitch test code is run in its own virtualenv in the :doc:`/glossary/hitch_directory`, kept completely separate from application code so its code does not interfere.
* Hitch downloads its own versions of software (e.g. postgres) into ~/.hitchpkg for use with testing. See :doc:`/glossary/hitch_package`.
* Hitch automatically sets up virtualenvs for application code to be tested with.
* Hitch has system checks to detect if necessary system packages are installed (via unixpackage).

See also:

* :doc:`/glossary/data_isolation`
* :doc:`/glossary/environment_isolation`
* :doc:`/glossary/process_isolation`
* :doc:`/faq/why_is_my_test_downloading_and_compiling_software`
* :doc:`/faq/how_does_hitch_compare_to_other_technologies`
