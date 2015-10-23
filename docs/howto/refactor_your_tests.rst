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
* Improving the code's readability (changing names, adding comments, disambiguating identifiers).

Tests are code too, so it's good practice to refactor your tests to gradually improve :doc:`/glossary/test_quality`
as you write new tests or fix existing ones.

Of course, you should only refactor *passing* tests and you should always run passing tests
after refactoring to ensure that they are still passing.

Here is a non-exhaustive list of things which you could work on while writing new tests or changing
old ones that you can do to improve your test quality:


De-duplicate duplicated tests
-----------------------------

You may find after a while that your test suite has a lot of duplication - for example,
tests that do almost the same thing in two or three slightly different ways.

See :doc:`/glossary/parameterize_test_cases` for how to remove some of that duplication.


Move configuration from engine.py to all.settings
-------------------------------------------------

Your execution engine should be kept as short as possible yet still capable. If you have
any long lists or chunks of data in your engine.py, moving them into all.settings will
help to keep it clean.


Change HTML IDs and Classes to make them more readable
------------------------------------------------------

Beware! This might be best left to a developer since it may require code changes as well
if the ID is used in many places (code, javascript, CSS, etc.) as well as changing
other IDs to accomodate.

If you have test steps that look like this::

    - Click: btnreg

Because the registration button had the HTML ID 'btnreg' when you wrote the test,
it might be worth changing the ID in the test and in the HTML code to make it more
readable, e.g. to something like::

    - Click: register-button

Similarly, if there is a button with ID::

    - Click: register

It *may* be worth renaming it to::

    - Click: register-button

If there is *any possibility of confusion* between register "something else" (e.g. a register link).




Increase the realism of your tests
----------------------------------


Run your tests in a more cost effective way
-------------------------------------------

If you have an extremely realistic test suite, it may end up being very expensive and
very slow to run it from beginning to end. This is not necessarily a bad thing, although
when it does start happening you need to start prioritizing some test cases over others
and ensure that they are run


Bring continuous integration environment closer to production
-------------------------------------------------------------
