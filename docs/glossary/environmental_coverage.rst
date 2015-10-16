Environmental Coverage
======================

Evironmental coverage is a measure of how well the environment
which code is *supposed* to run in is covered by its functional tests.

A web application with functional tests that test it in a *variety* of
web browsers has a higher environmental coverage than a web application
with functional tests that test it with just one browser.

Similarly, a web application with functional tests that test it in *one*
browser still has higher environmental coverage than a web application that
has no browser tests at all.

Projects with high :doc:`code_coverage` often still have low
:doc:`environmental_coverage`. This is a common source of bugs.

See also

* :doc:`if_it_is_measured_it_goes_up`
* :doc:`test_realism`
