Pipe
====

A pipe in saddle is a representation of a stdout or stderr
handle from a service and the stdout/sterr handle of the
test itself.

All of the output fed through these pipes is aggregated
along with saddle log messages and displayed to the user,
together, through the test's stdout pipe.
