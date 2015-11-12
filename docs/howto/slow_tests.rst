How to develop effectively with slow tests
==========================================

While :doc:`/glossary/unit_testing` is usually extremely fast, unit tests suffer
from tight :doc:`/glossary/coupling` and a lack of :doc:`/glossary/test_realism`.

On the other hand, realistic and loosely coupled functional tests can inevitably
end up being very slow to run. Unless properly handled this can end up lengthening
you code-test-refactor cycle and reducing your productivity.

Long test runs should not scare you as much as unrealistic or tightly coupled tests,
however. Even test runs that take multiple days to complete can end up being more useful
than tests that take seconds and they don't even have to slow you down.

It is easier to mitigate the effect of slower tests than it is to mitigate
the effect of a lack of realism or tight coupling in your tests.

:doc:`/glossary/you_can_optimize_slow_you_cant_optimize_unrealistic`.

There are two goals to :doc:`/glossary/regression_testing`:

* Providing confidence in the latest code required to release.
* Providing feedback about newly introduced bugs as quickly as possible.

If you split these goals and approach them separately, you can develop
more effectively.


#1 Use acceptance test driven development to develop features
-------------------------------------------------------------

Goal : provide feedback as quickly as possible about newly introduced bugs

If you can reduce your acceptance tests to < 1 minute, you can run one nearly
constantly while you develop - targeting the feature which you are working on.

This will end up catching a large majority of bugs in your code *while you develop*
in a matter of seconds.

More important than how long a test takes when it passed is how quickly it is
*designed to fail when there is a bug*. If you can get failure feedback in
~5 seconds on a 60 second long test, that is every bit as good as instantaneous
feedback.

You do not have to wait for the test to complete to continue developing either.

60 second long acceptance tests can run in the background while you work. The
longer the test runs the more confidence you will have that you haven't broken
anything.

[ graph of confidence level ]



#2 Introduce multiple layers of regression testing
--------------------------------------------------

Goal : provide feedback as quickly as possible about newly introduced bugs

While developing against one test focused on the feature you are working on
will catch most bugs, you can still end up breaking code covered by other
tests. This is a particular problem on code bases with very tightly coupled
code (i.e. big balls of mud).

However, you can take a focused approach to catching regression bugs without
waiting for 48 hour test runs to complete by running targeted regression
testing that is designed to fail and provide feedback as fast as possible.

* Running groups of tests associated with what you were working on before pushing (e.g. hitch test . --tag feature-email-user).
* Running random tests constantly on the development branch [ feature coming soon ].

#3 Run entire suites of regression tests during evenings, nights and weekends
-----------------------------------------------------------------------------

Goal : providing confidence in the latest code.

During periods when your code base is not being worked upon you can run


#3 Take advantage of time not spent developing: lunch, evenings, nights and weekends
------------------------------------------------------------------------------------

If you can run a full set of realistic regression tests in under 12 hours



#1 Throw hardware at the problem
--------------------------------

This is often a good approach to performance problems since hardware - relative
to developers, at least - is cheap. If you have a spare computer, you can adopt it
to run automated tests full time - while you are working and while you are sleeping.

80% of bugs are caught by 20% of the tests.

While this

However, it is easier to mitigate the effect of
slower tests than it is to mitigate the effect of unrealistic and tightly coupled
tests.

Below are a set of practices which can

This

Pareto rule
Realistic tests
Develop against a single test
Rope in some spare computers
Randomized testing
Overnight testing
