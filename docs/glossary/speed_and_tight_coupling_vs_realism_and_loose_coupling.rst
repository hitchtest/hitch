Speed and Tight Coupling vs. Realism and Loose Coupling
=======================================================

Speed and tight coupling vs. realism and loose coupling is a testing trade off
for all kinds of tests - both unit tests and integration tests.

The idea is that the higher the level at which you test:

* The more realistic scenarios you will be able to replicate.
* The more environmental bugs you will be able to catch and/or reproduce.
* The slower the test will run.
* The easier it is to swap out individual components in your application without changing the test.

The lower the level at which you test:

* The less realistic scenarios you will be able to replicate.
* The fewer environmental bugs you will be able to catch and/or reproduce.
* The faster tests will run.
* The harder it is to swap out individual components in your application since they will be coupled to the test.

Very, very high level
---------------------

A very high level test could run against a set of actual servers
accurately mimicking a real world set up.

This could be used to catch almost all bugs that might occur in
production as well as perform load testing.

Very high level
---------------

A group of virtual machines set up using vagrant that mimic the production
environment configuration and set up, using the same architecture - including
load balancers, database replication, etc. ideally using the same provisioning
software (e.g. ansible/salt/puppet).

This would catch provisioning bugs, operating system issues, bugs caused by
scaling - e.g. database replication issues.

Hitch could be made to run tests at this level by running vagrant up and
command(s) to provision the servers vagrant creates before interacting
with them with the via selenium.

High level
----------

Hitch provides high level realism - running all of the required services on
one machine, downloading specific versions of software (e.g. postgres) to
match what is running in production, bypassing most system packages.

This would catch most bugs except provisioning bugs, OS issues and bugs
caused by architecture and scaling.


Medium level
------------

Django test level isolation.


Low level
---------

Unit tests catch logical bugs and language bugs (e.g. syntax errors).
