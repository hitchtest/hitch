How to test command line applications
=====================================

.. note::

    This tutorial assumes that you have the :doc:`glossary/hitch_plugin` :doc:`plugins/hitchcli`
    installed and its step library is set up.

    If you followed the quickstart tutorial and said yes to testing a command line app, this should already be done for you.


Running a command
-----------------

To run a command you use the step "run"::

    - run: mycommand --myoptions


Waiting for some text to appear
-------------------------------

To wait for some text to appear, use the step 'expect', e.g.::

    - expect: Continue?


Typing
------

To 'mock type' a line of text, use the step 'send keys'::

    - send keys: Y


Ctrl-[key]
----------

Unless you want to use ctrl-[key] in which case use::

    - send control: C

For control-C, or::

    - send control: D


Waiting for a command to finish
-------------------------------

To wait for a command to finish successfully, use the step "finish"::

    - finish

If you want to verify that it finished with a specific non-zero exit code (e.g. 1), add the property 'with code'::

    - finish:
        with code: 1

If you want the command to finish and you don't care which code it exits with, use 'any' in place of 1::

    - finish:
        with code: any

Sending an exit signal to a command
-----------------------------------

If you want to SIGTERM, SIGINT, SIGKILL or any other valid unix signal, use the following step::

    - send signal: SIGTERM


Change directory
----------------

If you want to change directory before running a command, use::

    - cd: ../newdirectory
