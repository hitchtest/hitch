Test Concreting
===============

Test concreting is when tests lock down code interfaces by discouraging
developers from refactoring them.

It is a common cause of :doc:`technical_debt`. Tests surrround
badly designed interfaces, yet they give a level of confidence in the
code underneath which developers do not want to abandon.

Tests that surround a block of code provide protection against bugs from
creeping in when the code *underneath* it is refactored, so they still
incentivize refactoring *beneath* the interface.

However, since changing the interface that connects to the test will
*always* break the test, the developer has a strong incentive *not* to
change the interface.

The negative effects of test concreting can be avoided by:

* Explicitly designing tests with loose :doc:`coupling` in mind.
* Perpetually refactoring all code (test and application code) in order to make it more loosely coupled.
* *Only* surrounding code interfaces with tests once those interfaces are clean and have a low likelihood of changing.

Test concreting on good, clean interfaces is not a problem.

Hitch is explicitly built with loose coupling in mind (e.g.
see :doc:`/faq/why_just_html_ids_and_classes`) in order to
help mitigate the effect of test concreting.

The effect of test concreting can also happen in the absence of
automated tests, via the *implied testing* by users using the
software in production.

See also:

* :doc:`code_fear`
* :doc:`high_level_testing`
* :doc:`low_level_testing`
* :doc:`tightly_coupled_testing`
