Code Fear
=========

"Code fear" is the paralyzing fear of changing legacy code.

Code fear is instigated by developers' inability to fully comprehend the effects
of changing code and the knowledge that breaking changes may not be detected until
the code is in the hands of a user.


Causes of code fear
-------------------

Code fear is a problem caused largely by:

* :doc:`technical_debt`, meaning:
** A lack of tests and a lack of :doc:`test_quality`
** :doc:`tight_coupling` of code.
** Non-:doc:`DRY` code.
* :doc:`surprise_requirements`
* A culture of blame surrounding bugs
* Time pressure


Effects of code fear
--------------------

* Development of new features and bug fixes slows to a crawl.
* Refactoring of old code stops completely.
* Poor architectural decisions remain locked in place.
* Developers copy and paste large blocks of existing code when implementing new features in order to avoid changing old code.
* Developers implement hacks to accomodate other hacks.
* Developers clamor, beg and plead to be allowed to rewrite the project from the ground up.
* Managers often hire additional developers in an attempt to speed up development.

Code fear instigates a :doc:`vicious_cycle` of technical debt.

Are you having a problem with code fear? `We can help you <https://hitchtest.com/consulting.html>`_

