Hitch Package API
=================

.. note::

    This documentation applies to the latest version of hitchtest: version 0.6.5

Hitch strives to be self-bootstrapping. To enable this, it uses the concept of a
package. A package is an object representation of a piece of software (like python
or postgres) that your software relies upon.

To use, you must initialize this object in your engine set_up method and call
the .build() command. Once it is downloaded and built, your test can use it to
run your application code.

Running .build() will make your first test run very slow (downloading and building
python or postgres will take minutes), but the subsequent test runs will be much
faster.

Running .verify() is a necessary next step that simply checks that the software
runs without complaint and is the specified version.

The main advantage of your test downloading and building its own versions of software
is that it removes a source of :doc:`/glossary/indeterminacy` in your tests. Your
tests may be reliant upon you using a specific version of postgres and upgrading it
may break your tests. Additionally, if your team mates have different versions of, say,
python installed to you, this could lead to them getting different functional test
outcomes and different bugs.

Fixing the version and decoupling from the system versions of software installed
gives you more confidence that you are running the same code in the same way.


Python Example: Build from Scratch
----------------------------------

..  note::

    :doc:`/faq/why_should_my_tests_set_up_their_own_python_environments`

.. code-block:: python

    import hitchpython

    python_package = hitchpython.PythonPackage(version="2.7.9")
    python_package.build()      # Takes about 5 minutes during the first run. Instantaneous thereafter.
    python_package.verify()

    python.package.python       # This property now contains the full path to the built python


Python Example: Using a Specified System Python
-----------------------------------------------

..  warning::

    If you use the system python, will cause the test to fail with a complaint about the version
    of python being wrong when your package manager upgrades it. This is to protect you from
    a source of obscure bugs.

    If you have versions of python installed a specific locations using, say, pyenv, this method
    can be used, but it not recommended otherwise.


If you wish to specify an installation of python instead of having your test download and install
its own, you can simply specify a bin_directory and remove the .build() step.

.. code-block:: python

    import hitchpython

    python_package = hitchpython.PythonPackage(version="2.7.6", bin_directory="/usr/bin")
    python_package.verify()

    python.package.python # this property now contains "/usr/bin/python"


Creating your own Package
-------------------------

Hitch contains some plugins for software you can use, but it is not fully comprehensive. You may
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



