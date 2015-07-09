Why should my tests set up their own python environments?
=========================================================

Most python testing frameworks run using the same python environment
that the application code runs in.

Hitch is different.

Hitch is designed to test at as high a level as possible and to isolate
all possible sources of bugs and test :doc:`glossary/indeterminacy`.

The specific version and environment of python you test with is such
a potential source of bugs.

Thus, to ensure the stability and repeatability of the test, this environment
should ideally be brought under the test's control.

Hitch includes a plugin (based upon pyenv) which downloads and compiles
different versions of python which you can use to test your application in.

You can even download and create multiple versions of python to test your
application in - for instance, if you want to test your app using python 2
and python 3, or even *all* different versions of python.
