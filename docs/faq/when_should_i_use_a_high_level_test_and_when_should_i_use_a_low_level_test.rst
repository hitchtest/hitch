When should I use a high level test and when should I use a low level test?
===========================================================================

:doc:`/glossary/automated_testing` can be done on a variety of different levels - from
:doc:`/glossary/low_level_testing` that surrounds tiny modules all the way
up to :doc:`/glossary/end_to_end_testing`
that covers an entire system and its architectural set up.

Both :doc:`/glossary/high_level_testing` and low level testing have their advantages,
which is why one should not generally be used to the exclusion of the other.

A good project will have a variety of high level and low level tests, all
used together. A good tester will pick the right level to suit the various
trade offs.

Note that integration tests can be high level *or* low level, and the decision
whether or not to use them requires an entirely different set of trade offs.
See :doc:`when_should_i_use_a_unit_test_and_when_should_i_use_an_integration_test`
for that.

Note that :doc:`/glossary/test_driven_development` is useful in nearly all
scenarios, but its usefulness is highly dependent on picking the *right level*
to write tests for, as well as using the right tools.

New projects or legacy projects without tests
---------------------------------------------

Picking a good default level to test at for a project is the best
way to get off on the right foot.

By default, you should write tests at the
:doc:`/glossary/highest_convenient_level`.

A good approach to take is :doc:`/glossary/behavior_driven_development`
and :doc:`/glossary/acceptance_test_driven_development`.

In the beginning you will only have a few tests, so the implications
of how long it takes to run the entire test suite will not be that
big.

When you deploy your code and users start using it (whether they be
simulated by QA or real, actual users), you will notice that you
have bugs reported.

It is crucial that you write failing test cases for all of these bugs
*except*:

* Those where the cost of building a harness to replicate them would be prohibitive.
* Those for which the fix is both trivial (e.g. a one liner) and mainly related to misunderstood requirements (e.g. changing text).

When should I extend my current test harness?
---------------------------------------------

At some point you will find that you cannot replicate some bugs
reported by users with your set up, but the cost of building
a harness is not prohibitive.

You may find that the reported bugs are related to a browser that
you do not run tests on, for instance.

At this point, you should very seriously consider extending your
test harness so that it can handle this new source of bugs and
incorporating it into your regression test suite.

When should I build a new, *higher* level test harness?
-------------------------------------------------------

At some point you may find that you encounter a bug that is related
to something that is *out of the scope* of your current test harness.
If you encounter a deployment related bug, for instance, and your
current harness does not even do deployment in the same way, that
is probably the best time to build a new, separate test harness
that can test deployment scenarios.

Deployment tests that create a virtual machine from scratch, upgrade
it and install all necessary packages will be very slow, but there
will be certain kinds of bugs that *only* they will catch.

You will need a few of these at some point.


When should I build a new, *lower* level test harness?
------------------------------------------------------

As you refactor projects that you work on, especially if you work
on *decoupling* the software modules that it is comprised of, you will
find that some of these modules start becoming more independent
and need to know less and less about the system in which they are used.

Some of these software modules you may be able to replace entirely
with already well tested 3rd party modules.

Some, however, you will not.

Once you consider the interface on these modules *stable*, that is
a good time to wall them in with tests.

If the interface is stable, you should not suffer the ill effects
of :doc:`/glossary/test_concreting`.
