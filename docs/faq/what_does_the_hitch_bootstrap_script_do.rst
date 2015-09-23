What does the hitch bootstrap script do?
========================================

The hitch bootstrap script is a simple script that you install by:

  $ pip install hitch

This is a very simple script with no dependencies that has been tested
on python 2.6, 2.7, 3.3 and 3.4.

It does the following 4 things:

* Initializes the .hitch directory - containing the virtualenv used for running the hitch tests (separate from the virtualenv used for running your application).

* Deletes the .hitch directory (hitch clean).

* Triggers test runs (hitch test [arguments] will run the command .hitch/virtualenv/bin/hitchtest [arguments]).

* Upgrades all the packages specified in hitchreqs.txt (the software installed in the virtualenv used to run your tests).
