Brain Dead Manual Testing
=========================

Brain dead manual testing is the kind of testing that *can* be automated at
a reasonable cost but isn't, because reasons.

Brain dead manual testing has the following qualities:

* Manual testers are given scripts to follow which resemble computer programs (click on button X, check pop up Y appears...).
* Manual testers run these scripts repeatedly as a form of :doc:`regression_testing`.
* Manual testers who follow these scripts are miserable because they're being treated like robots.

Note that *not all manual testing is brain dead* - just the repetitive kind where automation would be cheaper.

The following forms of manual testing especially, are *very much necessary*
even in the presence of a great test harness:

* :doc:`exploratory_testing`
* Where the cost of building a test harness would be prohibitively high.

See also:

* `The Land That Scrum Forgot <https://www.youtube.com/watch?v=hG4LH6P8Syk>`_
* :doc:`manual_test_driven_development`
