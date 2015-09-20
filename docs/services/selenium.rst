Selenium
========

.. note::

    This documentation applies to the latest version of hitchselenium: version 0.4.1

Install the hitch selenium plugin like so::

    $ hitch install hitchselenium

.. code-block:: python

        import hitchselenium

        # Service definition in engine's setUp:
        self.services['Firefox'] = hitchselenium.SeleniumService(
            xvfb=False           # Optional (default: False). If true, this will run firefox hidden.
            shunt_window=True    # Optional (default: True). This will move the window out of the way of the mouse, to coordinates (0, 0).
            implicitly_wait=5.0  # Optional (default: 5.0). Set implicitly_wait value of the selenium driver.
        )

Once it is running, you can interact with the service::

    In [1]: self.driver = self.services['Firefox'].driver

    In [2]: self.driver.get(self.services['Django'].url())
    [ Open Django in firefox ]

    In [3]: self.driver.find_element_by_id("id_description").send_keys("type something...")
    [ Find element with ID description and types "type something" ]

The full selenium driver docs are here: https://selenium-python.readthedocs.org/en/latest/navigating.html
