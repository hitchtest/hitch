Hitch Package API
=================

.. note::

    This documentation applies to the latest version of hitchtest.

The :doc:`/glossary/hitch_package` API is an API which allows tests to download and install
their own software to use in the ~/.hitchpkg directory. It allows testers to easily specify exact
versions of software to test with and test with multiple versions.

Note that the :doc:`/glossary/hitch_package` API is not yet stable, so building packages on top of
it is not recommended yet.

The following documented, tested :doc:`/glossary/hitch_plugin`s are currently using the package
API to download and install software you can use to test your applications with:

* :doc:`/plugins/hitchpython`
* :doc:`/plugins/hitchredis`
* :doc:`/plugins/hitchpostgres`

The following undocumented plugins are also using the package API:

* :doc:`/plugins/hitchmysql`
* :doc:`/plugins/hitchrabbit`
* :doc:`/plugins/hitchelasticsearch`
* :doc:`/plugins/hitchmemcache`
