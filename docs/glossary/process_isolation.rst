Process Isolation
=================

Hitch also runs all of the services it requires itself. It starts
them at the beginning of a test and shuts them down at the end.

It can start all of the processes your sofware relies upon together
- databases, webservers, etc.

At the end of the test it tries to shut down these processes and
their children 'nicely' (usually by sending a SIGTERM signal).
