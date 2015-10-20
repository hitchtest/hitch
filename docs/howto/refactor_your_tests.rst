How to refactor your tests
==========================

A good, although uncommon development practice when building features or
fixing bugs is refactoring.

Refactoring means making small, incremental changes that improve the
quality of code.

This usually means:

* De-duplicating code
* Decoupling code
* Minimizing the amount of imperative code (e.g. python code) in favor of declarative code (e.g. YAML configuration).
* Improving the code's readability (changing names, adding comments)

Tests are code too, so it's good practice to refactor your tests to gradually improve :doc:`/glossary/test_quality`
as you write new tests or fix existing ones.

Of course, you should only refactor *passing* tests and you should always run passing tests
after refactoring to ensure that they are still passing.

Here is a list of things which commonly need refactoring in tests.


De-duplicate duplicated tests
-----------------------------

You may find after a while that your test suite has a lot of duplication - for example,
tests that do almost the same thing in two or three slightly different ways.

See :doc:`/glossary/parameterize_test_cases` for how to remove some of that duplication.


Move configuration from engine.py to all.settings
-------------------------------------------------

Your execution engine should be kept as short as possible yet still capable. If you have
any long lists in your engine.py, moving them into all.settings will help to keep it clean.


Change HTML IDs and Classes to make them more readable
------------------------------------------------------

Beware! This might be best left to a developer since it may require code changes as well
if the ID is used in many places (code, javascript, CSS, etc.) as well as changing
other IDs to accomodate.

If you have test steps that look like this::

    - Click: btn-rgstr-a1

Because the registration button had the HTML ID 'btn-rgstr-a1' when you wrote the test,
it might be worth changing the ID in the test and in the HTML code to make it more
readable, e.g. to something like::

    - Click: register
