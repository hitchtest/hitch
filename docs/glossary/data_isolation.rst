Data Isolation
==============

For the files which those packages interact with, hitch directs
those packages to store the data in the .hitch directory by default.

Thus all state that your tests rely upon - whether it is python
virtualenvs or the postgres data directory - is stored in that
directory and that directory only.

Deleting that directory with "hitch clean" and running "hitch
init" and "hitch test" again ensures a clean slate when running
any tests.
