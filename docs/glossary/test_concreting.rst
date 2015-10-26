Test Concreting
===============

Test concreting is when tests lock down code interfaces by strongly
disincentivizing developers from refactoring them.

It is a common cause of :doc:`technical_debt` - when tests surround
bad interfaces.

Tests that surround a block of code provide protection against bugs from
creeping in when the code *underneath* it is refactored, so they incentivize
refactoring *underneath* the interface.

However, since changing the interface that connects to the test will
*always* break the test, the developer has a strong incentive *not* to
refactor the interface.

The negative effects of test concreting can be avoided by:

* Explicitly designing tests with :doc:`loose_coupling` in mind.
* Perpetually refactoring code in order to make it more loosely coupled.
* *Only* surrounding code interfaces with tests once those interfaces are clean and have a low likelihood of changing.

Test concreting on good, clean interfaces is not a problem.

Hitch is explicitly built with loose coupling in mind in order to
help mitigate the effect of test concreting.

See also:

* :doc:`/faq/why_just_html_ids_and_classes`
* :doc:`code_fear`
* :doc:`high_level_testing`
