Test Setup
==========

The test setup in hitch is the python method in your :doc:`/glossary/execution_engine` which
contains all of the code run before any of your steps.

.. code-block:: python

    class ExecutionEngine(hitchtest.ExecutionEngine):
        def setup(self):
            # do test set up here

It usually does the following:

* Checks for required :doc:`/glossary/hitch_package`s. Downloads and installs them if they are unavailable.
* Defines the :doc:`/glossary/service_bundle` and services.
* Starts the service bundle.
* Any user defined set up required by :doc:`/glossary/preconditions`.

See also:

* :doc:`/glossary/tear_down`
