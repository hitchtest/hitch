FIRST
=====

FIRST is a set of principles for good tests.

These principles come from chapter 9 of `Clean Code <http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882>`_.

Occasionally these principles will conflict with one another and with other good software developement practises (e.g. loose coupling or DRY).


Fast
----

Tests should complete in as little time as possible.


Isolated
--------

Test isolation should be maximized as far as possible.

Isolation means that tests set themselves up and clean up after themselves.

Isolation also means that test code and libraries are kept separate from the code and libraries of the application under test.


Repeatable
----------

Tests must be able to be run repeatedly without intervention, and it should not matter what order they are run in.


Self-verifying
--------------

Tests should be pass-fail and not require human input for verification.


Timely
------

Tests should be written before the code that makes them pass.
