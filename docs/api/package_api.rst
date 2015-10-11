Hitch Package API
=================

.. note::

    This documentation applies to the latest version of hitchtest.

Hitch strives to be self-bootstrapping. To enable this, it uses the concept of a
"hitch package". A hitch package is an object representation of a piece of software
(like python or postgres) that your software relies upon.

To use, you must initialize this object in your engine set_up method and call
the .build() command. Once it is downloaded and built, your test can use it to
run your application code.

Running .build() will make your first test run very slow (downloading and compiling
python/postgres/mysql will take minutes), but the subsequent test runs will be much
faster.

Running .verify() is a necessary next step that checks that the software
runs without complaint and is the specified version.

The main advantage of your test downloading and building its own versions of software
is that it removes a source of :doc:`/glossary/indeterminacy` in your tests. Your
tests may be reliant upon you using a specific version of postgres and upgrading it
may break your tests. Additionally, if your team mates have different versions of, say,
python installed to you, this could lead to them getting different functional test
outcomes and different bugs.

Fixing the version and decoupling your tests from the system versions of software
installed should give you more confidence that you are running the same code in the
same way on all of the machines you test your code on. You can use it to
match your versions of software to versions you have running in production and gain
extra confidence that your code will run the same way in both environments.

Another benefit is that you can trivially run the same tests with more than one
version of the software. For example, you could run the same scenarios on your application
and only change the version of python your code is run with - say, from 2.7.10
to 3.5.0.

Using Hitch Packages in Hitch Plugins
-------------------------------------

Hitch currently has plugins that package and install all of the following software:

* MySQL
* Postgresql
* Python
* Elastic Search
* Redis
* RabbitMQ
* Memcache


Creating your own Package
-------------------------

..  note::

    Please note that the following API is not 100% stable yet.


..  note::

    Also note that I take requests. If there's a package you really need, feel free to raise an issue.
    If there is sufficient demand I will build it.

Hitch contains some the above for software you can use, but it is not fully comprehensive. You may
wish to create your own packages. To do this, you subclass the HitchPackage class.

.. code-block:: python

    from hitchtest import HitchPackage, utils

    ISSUES_URL = "http://github.com/yourgithub/thispackage/issues"

    class YourSoftwarePackage(HitchPackage):
        name = "Your software"

        VERSIONS = ["1.0", "1.1",]

        def __init__(self, version, directory=None, bin_directory=None):
            super(YourSoftwarePackage, self).__init__()
            self.version = self.check_version(version, self.VERSIONS, ISSUES_URL)

            if directory is None:
                self.directory = join(self.get_build_directory(), "yoursoftware-{}".format(self.version))
            else:
                self.directory = directory
            self.bin_directory = bin_directory

        def verify(self):
            version_output = check_output([self.maincommand, "--version"]).decode('utf8')
            if self.version not in version_output:
                raise RuntimeError("YourSoftware version needed is {}, output is: {}.".format(self.version, version_output))

        def build(self):
            # download and compile here
            self.bin_directory = installed_bin_directory

        @property
        def maincommand(self):
            if self.bin_directory is None:
                raise RuntimeError("bin_directory not set.")
            return join(self.bin_directory, "maincommand")

Examples of existing package API code you can use for inspiration:

* https://github.com/hitchtest/hitchpostgres/blob/master/hitchpostgres/postgres_package.py
* https://github.com/hitchtest/hitchredis/blob/master/hitchredis/redis_package.py
* https://github.com/hitchtest/hitchrabbit/blob/master/hitchrabbit/rabbit_package.py
* https://github.com/hitchtest/hitchelastic/blob/master/hitchelastic/elastic_package.py
* https://github.com/hitchtest/hitchmemcache/blob/master/hitchmemcache/memcache_package.py
* https://github.com/hitchtest/hitchmysql/blob/master/hitchmysql/mysql_package.py
