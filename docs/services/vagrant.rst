Vagrant
=======

.. note::

    This documentation applies to the latest version of hitchvagrant: version 0.1

Prerequisites
-------------

First, if it is not already installed, install the hitch vagrant package::

    $ hitch install hitchvagrant

Also ensure that vagrant is installed::

    $ sudo apt-get install vagrant

Usage
-----

To use, define the service after initializing the ServiceBundle object but before starting it.

Like so:

.. code-block:: python

    # Imports
    import hitchvagrant

    # Service definition in engine's setUp:
    self.services['MyVM'] = hitchvagrant.VagrantService(
        directory="vagrantubuntu/",     # Directory containing Vagrantfile (optional)
    )

Once it is running, you can run ssh commands against the machine::

    In [1]: self.services['MyVM'].ssh("pwd").run()
    /vagrant
