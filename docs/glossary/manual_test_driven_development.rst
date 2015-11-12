Manual test driven development
==============================

Manual test driven development is the practice of using a code-test-refactor cycle
where the test portion is manual or partially manual - for example:

1. Write code
2. Restart server
3. Click button on form.
4. See if the effect of clicking the button was the desired effect.
5. Repeat

Most developers develop via manual test driven development.

Where the :doc:`cost_of_building_a_test_harness` is not prohibitive
and the code is likely to be long-lived, manual test driven development
is an :doc:`testing_antipattern`.

While it is cheaper and faster to build software this way initially,
a lack of high quality automated tests inevitably leads to increasing
:doc:`technical_debt` and :doc:`code_fear`.

The cost of manual testing can also increase geometrically
without :doc:`parameterized_tests`.


See also:

* :doc:`acceptance_test_driven_development`
* :doc:`whiplash_driven_development`
