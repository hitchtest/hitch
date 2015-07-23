Selenium
========

Install the hitch selenium plugin like so::

    $ hitch install hitchselenium

.. code-block:: python

        import hitchselenium

        # Service definition in engine's setUp:
        self.services['Firefox'] = hitchselenium.SeleniumService(
            xvfb=False           # Optional (default: False). If xvfb is installed, this will run firefox hidden.
        )

Once it is running, you can interact with the service::

    In [1]: self.driver = self.services['Firefox'].driver

    In [2]: self.driver.get(self.services['Django'].url())
    [ Open Django in firefox ]

    In [3]: self.driver.find_element_by_id("id_description").send_keys("type something...")
    [ Find element with ID description and types "type something" ]

The full selenium docs are here: https://selenium-python.readthedocs.org/en/latest/navigating.html
