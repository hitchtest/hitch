Why should web application tests only interact with HTML IDs and HTML classes?
==============================================================================

The Hitch framework advises an opinionated approach to testing web applications that is unusual
among testing frameworks.

The basic idea is very simple. Imagine there is some thing you want to click on. The idea is:

* Any *individual* element *that you wish to click on* with should have its own *readable* HTML ID.
* Any element that is part of a group (or a group of groups) that you wish to click on should have one or more *readable* HTML classes.
* Any *test step* that interacts with or checks the web app should use only IDs or HTML classes to identify elements.

This means no "find by text" selectors, no "find by name" selectors and *certainly* no "find by xpath".


The controversial part
----------------------

The controversial part of this is the idea that *testers should change HTML code* in
order to create readable HTML ids or classes for use with their tests.

Many organisations restrict QA access to code bases. This is an organizational
deficiency which will damage the quality of the tests produced.


Why this opinionated approach is important #1: loose coupling
-------------------------------------------------------------

Loose :doc:`/glossary/coupling` is the general idea that software components should know
as little about each another as possible.

The components we're looking at here are "tests" and "your web app".

With this approach, what the test 'knows' about the web application should be restricted
to the HTML classes and IDs, so it is more loosely coupled than other approaches.

Loose coupling is important because it lets you change individual software components
without changing the components that rely upon them.

In this instance that means changing the code without needing to change the test.

In web application tests, tight coupling can manifest in ways that will often end up
breaking tests under benign conditions (see :doc:`/glossary/brittle_tests`):

* Changing the the text in an element (e.g. the exact error message) will break tests that rely upon seeing that exact text for a certain step.

* Changing the language of a web app and then following the same scenario will also break if the test relies upon the elements containing specific English phrases.

* Using an xpath almost *guarantees* that a change to the HTML layout or CSS will cause a test to break.

* Similarly, using a complicated CSS selector will do the same.


Why this opinionate approach is important #2: readability
---------------------------------------------------------

The second reason why restricting your tests to interacting only with classes and IDs
is :doc:`/glossary/readability`.

The more complex an element selector is, the more unreadable it becomes. e.g.::

    - Click: register

Is pretty readable. This::

    driver.find_element_by_css_selector(".buttons.pageitems.reg").click()

Is less readable. And this::

    driver.find_element_by_xpath("//div[class='buttons'][0]/input").click()

Is just nasty.

Unreadability increases with complexity and language power, which is why the
approach of simple and dumb for high level tests, is crucial for
:doc:`/glossary/test_quality`.


Should testers be allowed to *change* IDs and classes?
------------------------------------------------------

In general, no, although *raising an issue* and asking developers to change IDs and
classes to help make tests more readable should be encouraged.

While *adding* HTML IDs and classes has a low chance of causing problems, *changing*
them can cause problems - usually with javascript or CSS that relies upon specific
names for element IDs and classes.

That said, if they're careful and check first, why not.


Do I absolutely *have* to test web applications this way in Hitch?
------------------------------------------------------------------

No.

You are not restricted to only using CSS and HTML IDs. It is a recommended
approach, supported by the built in tools. It is by no means an approach you are
forced to take by the framework. Creating your own steps with hitch is easy enough
if you know some python and you are provided access to the python selenium webdriver
object should you wish to take another approach to interacting with your web
application.

It is possible that the above approach may not work in every scenario you may
need to test anyway.

See also

* :doc:`/misc/clarifying_documentation` (if you thing you see a flaw in this approach, raise a ticket).

