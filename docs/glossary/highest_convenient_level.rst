Highest convenient level
========================

The highest convenient level is the level of testing when writing
code where the feedback for a single test can be used for
:doc:`/glossary/test_driven_development`.

The highest convenient level is a level where a *single*
test can :doc:`run_to_completion` in under 60 seconds
and while maintaining the highest level of
:doc:`test_realism` and :doc:`isolation`
for the project in question.

Tests that run longer than 60 seconds risk upsetting developer
:doc:`test_driven_development_flow`, rendering them less useful.

Tests that are very low level may provide quicker feedback
however, since:

* They will not be able to exhibit such a high level of :doc:`test_realism`.
* Your test will be required to exhibit a higher degree of :doc:`coupling` to the code under test.

Their feedback will not necessarily be as useful as a higher
level test's feedback.
