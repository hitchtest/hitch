Indeterminacy
=============

Test indeterminacy is a property of tests that cause them to behave differently
during different test runs.

Test indeterminacy is can be caused by indeterminacy in the code or indeterminacy in the test.

Indeterminacy is a *bug* and should be treated as such.

Bugs in the test that can cause indeterminacy are often caused by:

* Different versions of software being integration tested with being run on different machines (python/postgres, etc.).
* The use of 'sleep' to wait for behavior changes or events which take longer on one test run than another.
* Non-isolated environments - when one test writes a file that is written by another, for instance.

Bugs in the application that can cause indeterminacy are often caused by:

* Race conditions.
* Lack of isolation.
