Why should my tests set up their own python environments?
=========================================================

Most python testing frameworks run using the same python environment
that the application code runs in.

Hitch is different::

    $ sudo pip install hitch

The *bootstrap* script should ideally installed using the system python.
This is a very small script with just one dependency.

This script sets up virtual environment to run the test code in::

    $ hitch init

This runs using your system python3. This is the environment all of your
testing code will run in.

Your tests will set up *another* environment to run your code in:

.. code-block:: python

    import hitchpython

    python_package = hitchpython.PythonPackage(version="2.7.9")
    python_package.build()      # Takes about 5 minutes during the first run. Instantaneous thereafter.
    python_package.verify()

This not only ensures that the packages required to run your tests do
not interfere with the packages required to run your code, it lets you be
be specific about the version of python your test runs with.

Hitch is designed to test at as high a level as possible and to isolate
all possible sources of bugs and test :doc:`/glossary/indeterminacy`.

The specific version and environment of python you test with is such
a potential source of bugs.

Thus, to ensure the stability and repeatability of the test, this environment
should ideally be brought under the test's control.

You can even download and create multiple versions of python to test your
application in - for instance, if you want to test your app using python 2.7.9
and python 3.4.3. You can even easily test your code in every single version
of python.
