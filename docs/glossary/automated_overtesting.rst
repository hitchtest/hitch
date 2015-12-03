Automated Overtesting
=====================

Automated overtesting is a :doc:`testing_antipattern` for which
fresh automated test cases are written and committed to source control,
for scenarios where:

* No bug was found, either by users or by :doc:`exploratory_testing`.
* Where there were no :doc:`surprise_requirements`.

Automated overtesting can lead to bloated regression test suites that are:

* Are more expensive to run.
* Take a longer time to complete.
* Are more expensive to maintain.
