How to do Behavior Driven Development with Hitch
================================================

A recommended approach to apply a :doc:`/glossary/behavior_driven_development`
approach with Hitch would be to build a project by taking the following steps
in order and iterating upon each one before moving to the next step:

1. Write test case name
2. Write test case description
3. Write test case scenario
4. Parameterize the test case scenario if necessary
5. Implement any necessary mock services, test steps, etc. in the test execution engine.
6. Implement the code that fulfils the test.

Bringing together input from as many stakeholders as possible for each
iteration will help improve what comes out at the other end - often
substantially.

At *each* point in the process, new requirements, ideas, problems and information
will emerge if you bring together the stakeholders. This can then be used
to step back and re-examine your preconceptions and generate new scenarios.

The *earlier* you get this input and modify your approach, the less expensive
a mistake or bad decision becomes. Taking the approach of Behavior Driven
Development and using it as a tool for communication as much as it is a tool
for generating test cases is a good way to create high quality software.

This approach can also be used to turn bugs into fixes and it works well
on greenfield projects as well as legacy projects.

Describe the behavior
---------------------

Initially with just the name and no scenario::

  - name : Buy a toy car from the store

Iterate upon it::

  - name : Search for and buy a toy car the store

Iterate upon it::

  - name : Search for and buy a Fisher-Price Power Wheels Disney Frozen Jeep from the store

Then flesh it out with a more detailed description::

  - name : Search for and buy a Fisher-Price Power Wheels Disney Frozen Jeep from the store
    description: |
      User browses the website, finds the toy and purchases.

This might give you an idea for another scenario. That's good. You may end up doing that a lot.
Note it down and put it aside::

  - name : Browse via categories and buy a toy from the store

Return to iterating upon the original scenario::

  - name : Search for and buy a Fisher-Price Power Wheels Disney Frozen Jeep from the store
    description: |
      User searches the website, finds the toy, puts it in the shopping cart,
      registers as a first time user and purchases with a credit card.


Flesh out the scenario
----------------------

Once the description is nailed down sufficiently, you can attack the scenario::

  - name : Search for and buy a Fisher-Price Power Wheels Disney Frozen Jeep from the store
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

And iterate upon it, of course::

  - name : Search for and buy a Fisher-Price Power Wheels Disney Frozen Jeep from the store
    description: |
      User searches the website, finds the toy, puts it in the shopping cart,
      registers as a first time user and purchases.
    scenario:
      - Load the website
      - Search for: Power Wheels Disney Frozen Jeep
      - Click on Fisher-Price Power Wheels Disney Frozen Jeep
      - Click purchase
      - Check out shopping cart
      - Fill form:
          Credit card name: John Smith
          Credit Card Number: 4135 8371 7032 1102 9999
          Three digit security code: 451
          Expiry date: 01/18
      - Click purchase

