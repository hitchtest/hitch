Hitch Package
=============

A hitch package is a software package downloaded and built by hitch to test
software that uses it.

Hitch downloads and installs a lot of its own software in order to provide
:doc:`isolation` and minimize on :doc:`brittle_tests`.

Examples of hitch packages:

* PostgresPackage
* PythonPackage
* MemcachePackage
* RedisPackage
* MySQLPackage
* RabbitPackage
* ElasticPackage

Hitch packages are downloaded into the ~/.hitchpkg directory and compiled
on the first test run of a test that relies upon it.

Hitch Packages are shared between projects. If one project uses postgres
9.3.9, for example, it will only be downloaded and built once.

Note that project specific environments - like the postgres data directory
or python virtualenvs are not kept in ~/.hitchpkg, they are kept in
the .hitch directory for that project unless specified otherwise.

See Alse: :doc:`hitch_plugin`
