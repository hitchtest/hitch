HitchVagrant
============

.. note::

    This documentation applies to the latest version of hitchvagrant.


Installation
------------

If it is not already installed, install the hitch vagrant package::

    $ hitch install hitchvagrant


Setup
-----

To use, define the service after initializing the :doc:`/api/service_bundle`:

Like so:

.. code-block:: python

    import hitchvagrant

    # Service definition in engine's setUp:
    self.services['MyVM'] = hitchvagrant.VagrantService(
        directory="vagrantubuntu/",     # Directory containing Vagrantfile (optional)
    )


Interaction
-----------

Once it is running, you can run ssh commands against the machine::

    In [1]: self.services['MyVM'].ssh("pwd").run()
    /vagrant
