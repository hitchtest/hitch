Pgid
====

A pgid is a process group id. This is an id given
to groups of processes in UNIX and controls the distribution
of signals.

In Hitch, each service has its own PGID so that
SIGINT/SIGTERM/SIGx messages received by the execution
engine (e.g. when the user hits ctrl-C) are not
passed directly on to services until they have been
handled correctly.
