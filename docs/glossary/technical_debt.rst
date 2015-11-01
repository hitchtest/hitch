Technical Debt
==============

Technical debt is a lack of code quality that is not immediately
apparent to users.

It manifests in the form of slower feature development and buggier code.

Technical debt falls into one of the following three categories:

* A lack of tests and/or a lack of :doc:`test_quality`
* Tight :doc:`coupling` of code.
* Non-:doc:`DRY` code.
* Code that does not :doc:`fail_fast`

Technical debt usually *compounds* owing to the positive feedback loop
caused by :doc:`code_fear` and :doc:`test_concreting`. It is an example of
a :doc:`vicious_cycle`.
