3: Building a python environment for your application
=====================================================

To test a python application, you first need to give your application a
python environment of its own to test with.

Hitch assumes that it will set up this environment for you.

.. note::

    :doc:`/faq/why_should_my_tests_set_up_their_own_python_environments`


Prerequisites
-------------

On Ubuntu/Debian::

  $ sudo apt-get install automake libtool patch libreadline6 libreadline6-dev zlib1g-dev make build-essential libssl-dev libbz2-dev libreadline-dev libsqlite3-dev llvm

On Fedora/Red Hat/Centos::

  $ sudo yum install python-devel automake libtool patch readline-devel zlib-devel libxml2 libxml2-devel gcc-make openssl-devel bzip2-libs zlib-devel bzip2-devel sqlite-devel llvm

On Arch::

  $ sudo pacman -S m4 base-devel automake readline zlib libxml2 gcc make openssl bzip2 zlib sqlite3 wget curl llvm

On Mac OS X::

  $ brew install libtool automake npm readline

  $ brew link readline


Install Plugin
--------------

In your tests directory (where the .hitch directory is), run::

  $ hitch install hitchpython


Using hitchpython in your tests
-------------------------------

Now you can use the hitchpython module in your tests::

  In [1]: import hitchpython

  In [2]: from os import path

  In [3]: pydir = path.join(PROJECT_DIRECTORY, "py")

  In [4]: python_package = hitchpython.PythonPackage(python_version=self.settings['python_version'], directory=pydir)

  In [5]: python_package.build()
  [ This might take a few minutes. Now is a great time to grab a coffee. ]

  In [6]: python_package.verify()

  In [7]: python_package.python
  Out[7]: /your/project/directory/py/bin/python

If the build step fails for a reason you don't understand, please, please, please raise an issue here: http://github.com/hitch/hitchpython/issues

This gives your project its own version of python, which you can use straight away, but you probably
also want to install some packages in it too::

  In [8]: from subprocess import call

  In [9]: call([python_package.pip, "install", "-r", path.join(PROJECT_DIRECTORY, "requirements.txt")])

Now, you can copy these lines of code to the set_up method in your test.

Note that this will take a while to run the first time that you run it. Downloading and compiling
python is not quick. Once it is built, however, subsequent test runs will be much quicker as they will
not attempt to download and rebuild python if it is already there.

pip install requirements.txt should be run each time so that if you change a version of package
your app depends upon in requirements.txt, the test will actually install it and test to see if it
runs correctly.
