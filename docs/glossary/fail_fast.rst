Fail Fast
=========

Fail fast is a general programming principle principle that failures
of all kinds should cause a program to fail as early as possible.

Similarly, tests that fail more quickly in the presence of an error are better
than tests that fail slowly.

The idea that tests should report failure quickly is a core part of Hitch's
philosophy. It manifests in the following ways:

* The fail fast setting - which causes, by default, test runs to abort in response to the first failure.
* :doc:`environment_checks` - this checks the system for all kinds of conditions which might cause the test to fail and reports them quickly.
* Additional type checks built into the core modules to prevent developers accidentally feeding in the wrong kinds of variables.

See also:

* `Fail Fast Wikipedia Page <https://en.wikipedia.org/wiki/Fail_fast>`_
* :doc:`indeterminacy`.
* :doc:`brittle_tests`.
