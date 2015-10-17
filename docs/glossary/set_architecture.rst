SET Architecture
================

The SET architecture is a software architectural pattern followed by the Hitch
testing framework which divides responsibilities

It is comprised of:

* Service - this is the code that runs processes like databases, web servers, mock servers required for the test. They are defined in and run by the engine.
* Engine - this is the code that interprets the test and executes the steps which *interact* with the services.
* Test/Template - this is the high level test description (or templated test description).

The SET architecture is very closely related to the MVC pattern, where:

* Service is analogous to model
* Engine is analogous to controller
* Template/Test is analogous to view
