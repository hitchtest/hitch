Why use Hitch instead of Django's Official Testing Framework?
=============================================================

Django already comes with four official classes for testing web apps:

* SimpleTestCase - a low level unit tester for Django views.
* TransactionTestCase - a low level unit tester for Django views which also rolls back the database.
* TestCase - a low level unit tester which performs the above and also loads fixtures and adds django specific assertions.
* LiveServerTestCase - a higher level TransactionTestCase which runs the django web server to allow for the use of selenium.

See : https://docs.djangoproject.com/en/1.8/topics/testing/tools/ for more.


No mock objects required
------------------------

SimpleTestCase, TransactionTestCase and TestCase all require at a minimum, the use of the
RequestFactory mock object. Hitch requires no mock objects and all code run during integration
tests will think that it is being run on a live system.

Read here for more on why mock objects are considered harmful: http://www.disgruntledrats.com/?p=620


You can run Celery (and other services)
---------------------------------------

Hitch allows you to run tests that involve interactions between the web server and celery and
potentially many other services as well.


Loosely coupled
---------------

Hitch tests at a high level. Strictly speaking only 2-3 lines of code would need to be changed in the
tests to swap the entirety of Django with a different web framework.
