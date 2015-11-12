SET Architecture
================

The SET architecture is a software architectural pattern followed by the Hitch
testing framework which divides responsibilities into three separate layers in order
to maintain strict :doc:`separation_of_concerns`.

It is comprised of:

* :doc:`service` - this is the code that runs processes like databases, web servers, mock servers required for the test. They are defined in and run by the engine.
* :doc:`execution_engine` - this is the code that interprets the test and executes the steps which *interact* with the services.
* :doc:`test_template` - this is the high level test description (or templated test description).

The SET architecture is very closely related to the MVC pattern, where:

* Service is analogous to model (optional - not required if not testing service oriented applications)
* Template/Test is analogous to view
* Engine is analogous to controller
