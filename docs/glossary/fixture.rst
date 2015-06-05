Fixture
=======

The word fixture has several potential meanings.

Saddle meaning
--------------

Under saddle, a fixture is a type of object which is
passed to a service which then uses it to set itself up in a
desired state.

They are defined in a variable called fixtures in each
test case class and passed to the ServiceEngine's configure
method, which passes them to the correct service.

Each fixture is associated with a service. Examples of
fixture types:

* :doc:`PostgresUser`
* :doc:`PostgresDatabase`
* :doc:`DjangoFixture`
* :doc:`DjangoSettings`



The wikipedia meaning
---------------------

"Something used to consistently test some item, device or piece of software."

See: `Test Fixture Wikipedia Page <http://en.wikipedia.org/wiki/Test_fixture>`_


Service specific meanings
-------------------------

Django also has the concept of a 'fixture', which refers to a JSON/YAML
file representing database data.

DjangoFixture is a type of saddle fixture, representing a Django
fixture.

