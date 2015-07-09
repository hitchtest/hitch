Why install Hitch on the system path?
=====================================

The instructions in quickstart tell you to install hitch like so::

  $ sudo pip install hitch

Or::

  $ pip install hitch

This *does* go against typical advice on best practice, which is to
install your python packages in a virtualenv.

The reason for doing this is that this package is mainly just a
bootstrapper for the hitch *testing* virtualenv. It contains just one
dependency (click), and so will not interfere with other packages on
your system python.

Your hitch testing virtualenv contains all of the packages needed
to test your application, but none of the packages that your application
needs to run. It is kept separate from your application python
environment because of the principle of isolation.

Your tests should set up a python environment themselves.

See also: :doc:`why_should_my_tests_set_up_their_own_python_environments`.
