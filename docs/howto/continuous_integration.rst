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


Jenkins
-------

On your jenkins machine you should first log in as root and do steps #1 and #2 from :doc:`/faq/what_does_the_init_script_do`

Once that's done, create a job for your project.

Once you have a Jenkins project checked out, you'll need the following commands::

    cd tests
    hitch init
    hitch test . --settings ci.settings

That should be all that's required.

Note that the first run should take a while but subsequent runs will be much faster.

Travis
------

A .travis.yml file should look like this::

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

Note that test runs using Travis will be slow due to the virtual machine being used to
run your tests being destroyed and rebuilt from scratch each time.
