How to use Hitch with Continuous Integration
============================================

Hitch is designed to be simple to configure and simple to deploy
on both test driven development environments and continuous integration servers.

It is also largely self contained meaning that the amount of configuration
you need to do on your CI systems to get them to work with hitch should be
very limited. For instance:

* Hitch takes care of installing system packages required to run your tests (apt-get install / yum install).
* Hitch will run your tests with XVFB if specified, meaning your CI server doesn't have to be configured to take care of that.
* Hitch will download and deploy any code it needs into self contained directories.

You can create settings files for the different environments where you run your tests. It's recommended
that you have at least one 'tdd.settings' for test driven development on your laptop and a 'ci.settings'
for doing continuous integration regression tests on your CI server.

See here for examples:

* https://github.com/hitchtest/django-remindme-tests/blob/master/ci.settings
* https://github.com/hitchtest/django-remindme-tests/blob/master/tdd.settings

The following two examples assume that you already have a ci.settings file with settings appropriate
for your CI environment and that your tests are in a directory in your repo called tests.

Jenkins
-------

On your jenkins machine you should first log in as root and do steps #1 and #2 from :doc:`/faq/what_does_the_init_script_do`

You should then ensure that the jenkins user can sudo without a password.

Once that's done, create a job for your project using the web interface.

The job should then be configured to run the following three commands::

    cd tests
    hitch init
    hitch test . --settings ci.settings

That should be all that's required.


Travis
------

.. note::

    Although it says python 3.4 below, your code will be tested with the version of python you
    specified in your tests (assuming you are testing python code at all).
    python 3.4 will *only* be used to run the bootstrap script.

Your .travis.yml file should look something like this::

    before_install:
      - sudo apt-get update -qq
      - sudo apt-get install -qq python python-dev python-setuptools python-virtualenv python3 python3-dev automake libtool
    language: python
    python:
      - "3.4"
    install:
      - "pip install hitch"
      - "cd tests"
      - "hitch init"
    script:
      - "hitch test . --settings ci.settings"

.. note::

    Test runs using Travis may be very slow (> ~30 minutes) due to the virtual machine being used to
    run your tests being destroyed and rebuilt from scratch each time.
