Logs
====

Hitch has several different types of logs.

It has the following types of logs for *each* service:

* Setup stdout
* Setup stderr
* Process stdout
* Process stderr
* Poststart stdout
* Poststart stderr

Additionally, it has:

* Test stdout
* Test stderr

for the test itself (e.g. if you use a print statement during the test).

All of the logs are aggregated and presented to the user by the
:doc:`service_engine`.
