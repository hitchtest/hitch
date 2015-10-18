How to test web applications
============================

.. note::

    This tutorial assumes that you have the :doc:`glossary/hitch_plugin` :doc:`plugins/hitchselenium`
    installed and its step library is set up.

    If you followed the quickstart tutorial, this should already be done for you.

.. warning::

    This tutorial is a work in progress. It is not currently complete.


Writing a step that clicks on a button or link
----------------------------------------------

To click on an individual item, you need to use the step "click" like so::

    - Click: register

This is telling hitch to click on an HTML element with the HTML ID "register".

.. note::

    This part is sometimes controversial. If you disagree, read :doc:`faq/why_just_html_ids_and_classes` for the rationale.

Now, there's a good chance that:

* Your HTML element does not have that ID - in which case you should *change the HTML itself* so that it does have that ID.
* That button has a different HTML ID - in which case you should use that ID instead (bookmark :doc:`/howto/refactoring_your_tests` for later).



Writing a step that clicks on an item that is part of a group
-------------------------------------------------------------

Sometimes the thing that you want to click on is part of a group, or a group of groups.

For instance, you may want to click on the first link in a list of links. To do that you use the same step::

    - Click: first friend-link

Here, "friend-link" is an *HTML class*.

As before, if the list of elements do not have a readable HTML class signifying what they are, you should *add* a class in the HTML itself.

Elements can have multiple classes, so if an element already has a class but it does not clearly identify all of the items
in the list, you should add a class that does.

If you want to click on the 2nd item::

    - Click: 2nd friend-link

Or the last::

    - Click: Last friend link

Or to click on an item that is part of a group which is *also* itself part of a group, you can specify two classes::

    - Click: First calendar day-31

Try to keep the test steps readable by using appropriately named classes where possible.


Verifying an element exists on the page - e.g. an error message
---------------------------------------------------------------

[ TO DO ]
