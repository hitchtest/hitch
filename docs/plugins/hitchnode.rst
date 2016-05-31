HitchNode
==========

.. note::

    This documentation applies to the latest version of hitchnode.

HitchNode is a :doc:`/glossary/hitch_plugin` created to make testing applications that use Node easier.

It contains:

* A :doc:`/glossary/hitch_package` to download and install specified version(s) of Node.
* A :doc:`/glossary/service` to set up an isolated Node environment and run it.

Note: the Node service destroys and sets up a new node environment during each test run in order
to provide strict :doc:`/glossary/isolation` for your tests.

Installation
------------

First, install the the plugin in your tests directory::

    $ hitch install hitchnode


Set up Node
------------

In your test, define the Node installation you want to test with:

.. code-block:: python

    import hitchnode

    node_package = hitchnode.NodePackage(
        version="5.0.0"  # Optional (default is the latest version of Node)
    )

    # Downloads & installs Node to ~/.hitchpkg if not already installed by previous test
    node_package.build()


To use, define the service after initializing the :doc:`/glossary/service_bundle` but before starting it:

.. note::

    See also: :doc:`/api/generic_service_api`

.. code-block:: python

    # Check if a package (e.g. less) is already installed:
    import hitchtest
    if not path.exists(path.join(
            hitchtest.utils.get_hitch_directory(),
            "node_modules", "less", "bin", "lessc"
        )):
        # Install the package is not found:
        chdir(hitchtest.utils.get_hitch_directory())
        check_call([node_package.npm, "install", "less"])
