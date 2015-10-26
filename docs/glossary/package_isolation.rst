Package Isolation
-----------------

Package isolation is a form of test :doc:`isolation` that
helps protect integration tests from being affected by the
current state of the system packages.

Lack of isolation is a common source of :doc:`/glossary/brittle_tests`.

Hitch provides package isolation for your tests via:

* Plugins that make use of the :doc:`/glossary/hitch_package` to download and compile software into ~/.hitchpkg.
* Running its own testing code in an isolated virtualenv.

See also:

* :doc:`/glossary/data_isolation`
* :doc:`/glossary/environment_isolation`
* :doc:`/glossary/process_isolation`
* :doc:`/faq/why_is_my_test_downloading_and_compiling_software`
* :doc:`/faq/how_does_hitch_compare_to_other_technologies`
