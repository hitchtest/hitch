Surprise requirements
=====================

Surprise requirements are requirements which are not covered by functional
tests which developers are *unaware of*.

It is a common problem on legacy code bases which have had significant developer
turnover. Developers who implemented functionality and later leave not only
leave with the knowledge of how their code worked, they often leave with the
knowledge of how the code was *supposed* to work.

When later developers are aware of their ignorance they will often
be hit by :doc:`code_fear`. When they are unaware of their ignorance, they
will often deploy code that violates user expectations or breaks existing
functionality.

"surprise requirements" can be reduced or eliminated by:

* Increasing :doc:`test_coverage` and :doc:`test_quality`.
* Using :doc:`automated_acceptance_tests`
* Improving documentation.
* Reducing developer turnover.
