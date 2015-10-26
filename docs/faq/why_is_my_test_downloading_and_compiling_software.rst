Why is my test downloading and compiling software?
--------------------------------------------------

Hitch usually downloads and compiles the software (e.g. python/postgres)
it uses to run your test with on the first test run.

Often this is software you may already have installed on your machine.

This is done to:

* Maintain :doc:`/glossary/package_isolation`.
* Cut down on :doc:`/glossary/brittle_tests`.
* Allow a greater level of :doc:`/glossary/test_realism`.

Examples of where this helps (with python):

* Upgrading your system will not cause behavior changes in your tests because the version of python has changed.
* You can develop and test against the exact same version of python that you use on production.
* You can tweak the version in your tests before running a full test run to give confidence that upgrading your version of python in production will not cause bugs.
* You can trivially test your code against *multiple* versions of python on the same test run (see :doc:`/howto/parameterize_test_cases`.).

While it is inconvenient to download and compile software on the first
test run, there is a substantial benefit to taking this appraoch.


See also:

* :doc:`why_does_the_first_test_run_take_so_long`
