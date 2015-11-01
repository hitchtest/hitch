How to upgrade Hitch
====================

By default, hitch uses the same versions of software and plugins that it used
when you first set it up.

However, new bug fixes and features are being made available all the - bug fixes and
features that you may want to take advantage of.

When to upgrade
---------------

The best times to upgrade are:

* Before installing and using a new plugin with 'hitch install'.
* Every two weeks (say, at the beginning of a sprint).
* If you run into a bug in hitch and you have not upgraded in a while.
* When most, if not all of the tests on your project are passing (so that you can more easily distinguish between bugs in your project and bugs in hitch).

Upgrade the bootstrapper
------------------------

Although the bootstrapper does very little and should change very little,
there are occasionally bugfixes included. Using your system python,
On Linux, run the following command::

    $ sudo pip install --upgrade hitch

On Mac::

    $ pip install --upgrade hitch


Upgrade your project's test environment
---------------------------------------

The vast majority of your code is installed in the :doc:`/glossary/hitch_directory`
directory in your project. The plugin versions you are currently using are all
specified in :doc:`/glossary/hitchreqs.txt`.

To upgrade all plugins to their latest versions, run::

    $ hitch upgrade

hitchreqs.txt should now have a new list of package versions.

Once you are done, re-run all of the tests again::

    $ hitch test .

If everything passes, you can commit the new hitchreqs.txt to source control.


What if something goes wrong during upgrade?
--------------------------------------------

While every effort is taken to ensure that the latest versions of hitch
and its plugins are more stable than the last, there is always the possibility
that bugs can creep in during upgrade.

If something goes wrong during upgrade, you can do the following:

1. If you see an error message related to deprecation, change your code to accomodate and re-run the tests.

2. If you see an inexplicable error, you can try running the following commands, which should rebuild your local hitch environment from scratch::

    $ hitch clean
    $ hitch init
    $ hitch test .

3. You can try running the following commands, which should destroy your ~/.hitchpkg directory as well, allowing for it to be rebuilt::

    $ hitch cleanpkg
    $ hitch clean
    $ hitch init
    $ hitch test .

4. If none of the above fix your problem, you've discovered a bug in the framework itself. Please raise an issue.

5. You can *roll back* your changes reverting your hitchreqs.txt to the state it was before running hitch upgrade (e.g. with git checkout) and running::

    $ hitch init


I've upgraded. What about the rest of my team?
----------------------------------------------

Once one person has upgraded and committed a new hitchreqs.txt to source
control, the rest of the team can follow the same steps, with one
minor difference - instead of running "hitch upgrade", they should
run::

    $ hitch init

To bring their environment into alignment with the latest hitchreqs.txt
versions.

If you had to run "hitch clean" or "hitch cleanpkg", they probably
will as well.

Note that your continuous integration environment should *always*
run this command before running any tests.
