Pgid
====

A pgid is a process group id. This is an id given
to groups of processes in UNIX.

In saddle, each service has its own PGID so that
SIGINT messages received by the harness (e.g. when
the user hits ctrl-C) are not passed directly on to
services.