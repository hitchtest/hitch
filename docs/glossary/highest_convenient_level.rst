Highest convenient level
========================

The highest convenient level is the level of testing when writing
code where the feedback for a single test can be used for
:doc:`/glossary/test_driven_development`.

The highest convenient level is a level where a *single*
test can most realistically run to completion in under 60 seconds
and while maintaining the highest level of
:doc:`/glossary/test_realism` and :doc:`/glossary/isolation`
for the project in question.

Tests that run longer than 60 seconds risk upsetting developer
flow, rendering them much less useful for test driven development.

Tests that are very low level may provide quicker feedback,
and you may be able to run tens or hundreds per second, however:

* They will almost always test much less realistically.
* They will have tighter :doc:`/glossary/coupling` to the code under test.

.. note::

    A test that takes 60 seconds to finish successfully should still
    fail much earlier in the presence of a bug, especially if the
    test is designed to :doc:`/glossary/fail_fast`.
