When should I use a unit test and when should I use an integration test?
========================================================================

Integration tests are tests that surround large software systems that are made up
of a lot of interconnecting parts and interact with them as the outside world
would. They are not necessarily written in the same language as the code
they are testing.

Hitch is a testing framework designed specifically for writing integration tests
for code written in any language.

Unit tests usually surround smaller blocks of code and directly call the APIs
of the blocks of code they are testing. They are written in the same language as
the code they are testing.

py.test and nose are good python unit testing frameworks. Other languages
have their own equivalents.

Both unit tests and integration tests *can* catch bugs in *any* kind of code.
However, they both have different trade offs and those trade offs should
be understood before writing either one.


When are integration test more useful than unit tests?
------------------------------------------------------

Integration tests are most useful for testing integration code.

Integration code is the kind of code which is mostly linking systems
together. Most web apps are good examples of pure integration code -
linking browsers, networks, REST APIs, email servers, databases,
payment gateways and all manner of other APIs.

Integration tests that either use or *accurately mock* all of these components
together can mimic the effect of scenarios that traverse all of them and
uncover bugs that occur along the way. These are realistic tests
(see :doc:`test_realism`).

Unit tests that test the same kind of code usually do so by making
extensive use of *mock objects*. Mock objects are not only unrealistic
representations of real objects, using them in your tests tightly couples
your code to your tests.

Thus mock objects could be considered a 'code smell'. Extensive use of
them tends to indicate that you should have written an integration test
to cover the code instead of a unit test.


When are unit tests more useful than integration tests?
-------------------------------------------------------

Integration tests, especially *realistic* integration tests, uncover a
greater variety of bugs than unit tests but they do run more slowly
than unit tests.

This is *very often not a problem* - computing power is very cheap
these days, after all, and feedback on automated tests does not
have to be instantaneous or even quick to be vitally useful.

Also: you can optimize for speed. You can't optimize for unrealistic.

However, for some scenarios a unit test is no less realistic than an
equivalent integration test. Code that is almost entirely *logical*
rather than integrational is well suited to unit tests.

Such code can include:

* Algorithms that perform complex calculations
* Algorithms that are parsing text or other input
* Algorithms that do hard computing problems
* Code that is largely functional

The relative cheapness of running unit tests also makes it possible to
apply tools such as Haskell's quickcheck / Python's Hypothesis to cover
more input scenarios to functions than a human could even imagine.


What about code where algorithmic and logical code is thoroughly mixed together?
--------------------------------------------------------------------------------

It is often the case with legacy code bases that algorithmic/logical code (e.g.
functions that calculate pricing) and integrational code (e.g. code for storing/retrieving
data in the database) are thoroughly mixed up and cannot easily be separated.

This is an example of :doc:`/glossary/tight_coupling`.

In such cases, unit tests are of very limited value as well - at least initially.

A good approach to code bases like these is to gradually surround the
entire code base with integration tests and *then* refactor it until the
logical/algorithmic code and the integrational code are separated from one
another.

Once the logical code and the integration code are separated and talk
to one another across tight, well defined API boundaries, unit tests
become useful again.

See also:

* :doc:`how_should_i_choose_where_to_surround_my_code_with_tests`
