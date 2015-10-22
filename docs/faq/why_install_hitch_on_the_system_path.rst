Why install Hitch on the system path?
=====================================

The instructions in quickstart tell you to install hitch on the system path like so::

  $ sudo pip install hitch

Or (on Mac OS X)::

  $ pip install hitch

This package *can* be installed in a virtualenv, but there is no point
to doing so, since:

* It is just a simple bootstrapper script.
* It contains none of the actual code to run tests.
* It has zero dependencies so installing it will not interfere with other system packages.
* It needs to be available on the system path so that the 'hitch' command can always be used.

See also:

* :doc:`why_should_my_tests_set_up_their_own_python_environments`.
* :doc:`how_do_i_uninstall_hitch_completely`.
