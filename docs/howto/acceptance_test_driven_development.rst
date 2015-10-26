How to do Acceptance Test Driven Development with Hitch
=======================================================

See also: :doc:`/glossary/behavior_driven_development`.

A recommended approach to :doc:`/glossary/acceptance_test_driven_development`
wth hitch is to do the following steps in order:

1. Write a high level, failing :doc:`/glossary/acceptance_test` for an unimplemented feature or bug.
2. Refactor the high level test.
3. Implement the code that runs the test in the :doc:`/glossary/execution_engine`.
4. Implement the code that makes the test pass.
5. Refactor the code.

Each of these steps should be iterative and going back and changing the step or
steps above it will often be necessary.

Mistakes made at the higher level often become progressively more expensive
the later

Write a high level failing acceptance test
------------------------------------------

.. note::

    See :doc:`/howto/behavior_driven_development` for how to get to this point.

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

