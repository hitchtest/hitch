How to do Behavior Driven Development with Hitch
================================================

.. note::

    Before starting BDD, you may want to familiarize yourself with
    the `Cynefin framework <http://lizkeogh.com/cynefin-for-developers/>`_
    as an approach to actually thinking about your requirements
    and `using BDD as a sensemaking technique <http://lizkeogh.com/2014/07/29/using-bdd-as-a-sensemaking-technique/>`_

Building a project starts out with requirements analysis.

Behavior driven development is an approach taken from test driven development
and domain driven design applied to software development.

The basic approach consists of two very basic tasks:

* Coming up with scenarios and writing them down in a DSL.
* Thinking about the scenarios, having conversations about them with stakeholders and reworking them.
* Ending up with a DSL that can be used to drive a realistic test which can be used to develop against.

A recommended approach to apply a :doc:`/glossary/behavior_driven_development`
approach with Hitch would be to build a project by taking the following steps
in order and iterating upon each one before moving to the next step:

1. Write test case name
2. Write test case description
3. Write test case scenario
4. Parameterize test case scenarios if necessary
5. Implement any necessary mock services, test steps, etc. in the test execution engine.
6. Implement the code that fulfils the test.

Steps 1-6 constitute behavior driven development and steps 4-6 constitute
:doc:`/glossary/acceptance_test_driven_development`.

Steps 1-3 are ultimately more about *conversations* than they are about writing
code, and the best scenarios are written with input from as many stakeholders
as possible.

At *each* point in the process, new requirements, ideas, problems and information
will emerge. If it takes a long time to write a single scenario because of the
communications overhead, *that's ok*. It's still *a lot* cheaper than discovering a
mistake in your specifications weeks or even months later while implementation
is already in progress.

Scenarios should be written by a :doc:`/glossary/customer_representative`.

This approach can be used to:

* Create test scenarios for new features to develop against.
* Write test scenarios for failing test cases.


Describe the behavior
---------------------

Initially with just the name and no scenario:

.. code-block:: yaml

  - name : Buy a toy car from the store

Iterate upon it:

.. code-block:: yaml

  - name : Search for and buy a toy car the store

Iterate upon it some more:

.. code-block:: yaml

  - name : Search for and buy a Fisher-Price Power Wheels Disney Frozen Jeep from the store

Then flesh it out with a more detailed description:

.. code-block:: yaml

  - name : Search for and buy a Fisher-Price Power Wheels Disney Frozen Jeep from the store
    description: |
      User browses the website, finds the toy and purchases.

This might give you an idea for another scenario. That's good. You may end up doing that a lot.
Note it down and put it aside:

.. code-block:: yaml

  - name : Browse via categories and buy a toy from the store

Return to iterating upon the original scenario:

.. code-block:: yaml

  - name : Search for and buy a Fisher-Price Power Wheels Disney Frozen Jeep from the store
    description: |
      User searches the website, finds the toy, puts it in the shopping cart,
      registers as a first time user and purchases with a credit card.


Flesh out the scenario
----------------------

Once the description is nailed down sufficiently, you can attack the scenario.

Your test cases should generally follow the structure of Given-When-Then, where
the preconditions and first few steps specify a "given" situation to start the
scenario in, the "when" specifies a series of steps and "Then" specifies the
outcome.

.. code-block:: yaml

  - name : Search for and buy a Fisher-Price Power Wheels Disney Frozen Jeep from the store
    preconditions:

    description: |
      User searches the website, finds the toy, puts it in the shopping cart,
      registers as a first time user and purchases.
    scenario:
      - Load the website
      - Search for: Power Wheels Disney Frozen Jeep
      - Click on Fisher-Price Power Wheels Disney Frozen Jeep
      - Click purchase
      - Check out shopping cart
      - Sign up
      - Enter credit card details
      - Click purchase

And iterate upon it, of course, until you have a well defined test case that covers input
from all stakeholders that you can turn into an executable test:

.. code-block:: yaml

  - name : Search for and buy a Fisher-Price Power Wheels Disney Frozen Jeep from the store
    preconditions:
      database: basic-database-with-power-wheels
      browser: firefox
    description: |
      User searches the website with firefox, finds the toy, puts it in the shopping cart,
      registers as a first time user and purchases.
    scenario:
      - Load the website
      - Search for: Power Wheels Disney Frozen Jeep
      - Click on Fisher-Price Power Wheels Disney Frozen Jeep
      - Click: purchase
      - Click: check-out-shopping-card
      - Fill form:
          Name: Barack Obama
          Password1: nowletmebeclear
          Password2: nowletmebeclear
          Delivery Address: 1600 Pennslyvania Ave.
      - Click: register
      - Fill form:
          Credit card name: Barack Obama
          Credit Card Number: 1135 4913 9201 1102 9999
          Three digit security code: 012
          Expiry date: 01/18
          Card Address: 1600 Pennslyvania Ave.
      - Click: purchase
      - Verify that display page was displayed
      - Verify that purchase order was recorded:
          Name: Barack Obama
          Item: Power Wheels Disney Frozen Jeep

Once you have a test or a group of tests you are happy with, you can move on to the next group of
steps - :doc:`/howto/acceptance_test_driven_development`.
