6: Writing your test steps
==========================

Now that you've gotten all of your services running, you've done the hardest
part. You can use the stub test to start everything and pause, letting you
click around and do some exploratory testing if you like.

Your test still looks something like this however:

.. code-block:: yaml

  - name: Stub
    engine: engine.py:YourProjectTestExecutionEngine
    scenario:
      - Pause

Adding a scenario simply means adding another line:

.. code-block:: yaml

  - name: Stub
    engine: engine.py:YourProjectTestExecutionEngine
    scenario:
      - Load website
      - Pause

Hitch will look for and run a corresponding underscore_case method in your engine:

.. code-block:: python

    def load_website(self):
        # your code goes here

If you also want to feed the method a parameter, you can:

.. code-block:: yaml

  - name: Stub
    engine: engine.py:YourProjectTestExecutionEngine
    scenario:
      - Load website
      - Click on: register_button
      - Pause

Which, when it calls this:

.. code-block:: python

    def click_on(self, button_id):
        self.driver.find_element_by_id(button_id).click()

Will click on a button.

If you want to feed the method a whole bunch of parameters, well, you can do that too:

.. code-block:: yaml

  - name: Stub
    engine: engine.py:YourProjectTestExecutionEngine
    scenario:
      - Load website
      - Click on: register_button
      - Register:
          Your name: Nikola Tesla
          Your age: 18
          Your favorite hobbies:
            - Inventing
            - Electricity
            - Annoying Edison
      - Pause

This will call a method like this:

.. code-block:: python

    def register(self, your_name="", your_age="", your_favorite_hobbies=None):
        # The parameters will look like this
        assert your_name = "Nikola Tesla"
        assert your_age = "18
        assert your_favorite_hobbies == ["Inventing", "Electricity", "Annoying Edison", ]

As you can see, how the tests are written, configured and run is left mostly up to you.

