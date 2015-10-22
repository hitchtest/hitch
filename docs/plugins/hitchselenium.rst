Selenium
========

.. note::

    This documentation applies to the latest version of hitchselenium.


HitchSelenium is a :doc:`/glossary/hitch_plugin` specifically to make testing web applications easier.

It contains:

* A :doc:`/glossary/service` to run firefox and provide access to its webdriver.
* A :doc:`/glossary/step_library` to perform common actions with a selenium webdriver.


Installation
------------

Install the hitch selenium plugin like so::

    $ hitch install hitchselenium


.. note::

    If you are running Mac OS X you must download and install firefox *manually* before running a test that uses hitchselenium.


Set up the Firefox service
--------------------------

To use, define the service after initializing the :doc:`/api/service_bundle`:

.. code-block:: python

    import hitchselenium

    # Service definition in engine's setUp:
    self.services['Firefox'] = hitchselenium.SeleniumService(
        xvfb=False           # Optional (default: False). If true, this will run firefox hidden (only available on Linux).
        shunt_window=True    # Optional (default: True). This will move the window out of the way of the mouse, to coordinates (0, 0).
        implicitly_wait=5.0  # Optional (default: 5.0). Set implicitly_wait value of the selenium driver.
    )

After the service bundle has been started, you can access the selenium webdriver like so:

.. code-block:: python

    self.driver = self.services['Firefox'].driver


Interacting with Firefox
------------------------

You can then interact with firefox via the selenium webdriver in your steps or with :doc:`/glossary/ipython`::

    In [2]: self.driver.get("http://localhost:8080/")
    [ Opens http://localhost:8080 in firefox ]

    In [3]: self.driver.find_element_by_id("id_description").send_keys("type something...")
    [ Find element with ID description and types "type something" ]

The full selenium driver docs are available here: https://selenium-python.readthedocs.org/en/latest/navigating.html


Using the selenium step library
-------------------------------

Using the selenium web driver can be cumbersome, so there is also a step library provided with steps that,
when used correctly, should aid with :doc:`/glossary/test_readability`.

To set the selenium step library up in your test setup after the service bundle has been started:

.. code-block:: python

    self.webapp = hitchselenium.SeleniumStepLibrary(
        selenium_webdriver=self.services['Firefox'].driver,
        wait_for_timeout=5,
    )

    self.click = self.webapp.click
    self.wait_to_appear = self.webapp.wait_to_appear
    self.wait_to_contain = self.webapp.wait_to_contain
    self.wait_for_any_to_contain = self.webapp.wait_for_any_to_contain
    self.click_and_dont_wait_for_page_load = self.webapp.click_and_dont_wait_for_page_load

For instructions on how to use the step library in your steps see :doc:`/howto/web_applications`.

