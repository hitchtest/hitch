How does Hitch compare to other technologies?
=============================================

Cucumber/Behave/RSpec/Behat/Behave
----------------------------------

Cucumber, RSpec, Behat and Behave and are all keyword driven test automation
frameworks that run automated acceptance tests. They contain an interpreter
for executing high level test cases written in Gherkin.

Hitch follows a similar approach but has its own equivalent to
Gherkin: :doc:`/glossary/hitch_test_description_language`.

Unlike Gherkin it does not use its own syntax - its syntax
is built upon YAML.

Test cases written with Hitch test should usually be less verbose
and more to the point, although still ideally maintaining
readability.

Gherkin example from the Cucumber website (223 characters; English-like):

.. code-block:: gherkin

    Feature: Division
    In order to avoid silly mistakes
    Cashiers must be able to calculate a fraction

    Scenario: Regular numbers
        * I have entered 3 into the calculator
        * I press divide
        * I have entered 2 into the calculator
        * I press equal
        * The result should be 1.5 on the screen

Hitch equivalent (113 characters; not English-like):

.. code-block:: yaml

    - name: Division
      description: Cashier calculates a fraction
      scenario:
        - Enter: 3
        - Press: divide
        - Enter: 2
        - Press: equal
        - Result: 1.5

Step-to-code regular expression translation is also unnecessary in Hitch
sidestepping `potential traps like this. <https://stackoverflow.com/questions/1186547/regular-expressions-in-cucumber-steps>`_

.. note::

    This pitfall is `recognized by Cucumber in issue #1. <https://github.com/cucumber/cucumber/issues/1>`_

    The python tool behave gives you `three different parser options <https://pythonhosted.org/behave/tutorial.html#step-parameters>`_
    as a way to deal with it. There are other `suggested <http://laxmareddy.com/cucumber-step-definitions-regular-expressions-matching-steps/>`_
    `workarounds <http://chrismcmahonsblog.blogspot.sg/2013/09/magic-strings-and-regular-expressions.html>`_ too.

The above three steps are implemented as follows in Hitch:

.. code-block:: python

    def enter(self, number):
        # code that enters a number

    def press(self, key):
        # code that presses a key

    def result(self, number):
        assert displayed_result == number

More complex data can also be cleanly encoded into steps and preconditions. Anything that is valid YAML is allowed.

You can write a complex step like this:

.. code-block:: yaml

    - Send mail:
        From address: Receiver <to@todomain.com>
        To address: Sender <from@fromdomain.com>
        Body:
          From: Receiver <to@todomain.com>
          To: Sender <from@fromdomain.com>
          Subject: Test email for "HitchSMTP"
          Content: |
            http://www.google.com
            Another link: http://yahoo.com
            Another link: https://www.google.com.sg/?gfe_rd=cr&ei=2X4mVebUFYTDuATVtoHoAQ#q=long+long+long+long+long+long+url

Which would trigger a python method call equivalent to the following:

.. code-block:: python

    self.send_mail(
        from_address="Receiver <to@todomain.com>",
        to_address="To address: Sender <from@fromdomain.com>",
        body={
            "From" : "Receiver <to@todomain.com>",
            "To" : "Sender <from@fromdomain.com>",
            "Subject" : "Test email for \"HitchSMTP\""
            "Content" : (
                    "http://www.google.com\n"
                    "Another link: http://yahoo.com\n"
                    "Another link: https://www.google.com.sg/?gfe_rd=cr&ei=2X4mVebUFYTDuATVtoHoAQ#q=long+long+long+long+long+long+url"
                )
            }
        )

Where reading the data in the step code :doc:`/glossary/execution_engine` is still straightforward:

.. code-block:: python

    self.send_mail(self, from_address, to_address, body)
        content = body.get("content")


The above applies to the following packages:

* hitchtest

Hitch also provides plugins to perform many more test and development related tasks, saving on boilerplate (see :doc:`/plugins/index`).

Hitch does *not* provide:

* Bindings to write the execution engine in languages other than python. This is not roadmapped and not possible currently.
* Plugins to easily test other languages and frameworks (e.g. Java, node, Ruby, etc.). This possible but not easy currently and is roadmapped.

Docker/Docker Compose
---------------------

Docker is a lightweight virtualization technology that provides
system :doc:`/glossary/isolation` using cgroups and kernel
namespaces.

Docker can be used to develop software in, test software in and
deploy software in. By running the same container in all three
environments, development and testing can achieve a greater
degree of :doc:`/glossary/test_realism` thus avoiding many
'surprise' production bugs.

Nonetheless, the isolation and realism is not as high as "true
virtualization" (VirtualBox, Xen, VMWare) provided via kernel
emulation.

The same Docker container running on different systems
can (and probably will, for many projects eventually),
exhibit different behavior due to different versions of the
linux kernel or libc in development, testing and production
environments (TODO : verify libc differences??).

Due to the reliance on Linux kernel features for isolation,
docker also does not work on Mac OS X or BSD platforms
without running it in a heavyweight virtual machine.

Hitch can run docker containers, as it can any other
process (a plugin to make this easier is coming soon).

If you deploy docker containers in your production
environment, this is a recommended approach since it
will bring a greater level of :doc:`/glossary/test_realism`.

If you do *not* deploy docker containers in your
production environment, you may want to avoid using
docker for development and test environments.

Hitch achieves a similar, although lower level of
isolation and realism using a different approach:

* :doc:`/glossary/package_isolation`
* :doc:`/glossary/data_isolation`
* :doc:`/glossary/process_isolation`
* :doc:`/glossary/environment_isolation`

You can, for instance, run the exact same database version,
python version and redis version that you do in production
on your development machine.

[ TO DO : docker-compose and starting services bug ]

The above applies to the following packages:

* hitchserve
* hitchtest
* All hitch plugins

.. note::

    You can also run hitch *in* docker. It is regularly tested with the latest version.


Built-in Django Testing Framework
---------------------------------

Django already comes with four official classes for unit testing web apps, each of which test at a progressively higher level:

* SimpleTestCase - a low level unit tester for Django views.
* TransactionTestCase - a low level unit tester for Django views which also rolls back the database.
* TestCase - a low level unit tester which performs the above and also loads fixtures and adds django specific assertions.
* LiveServerTestCase - a higher level TransactionTestCase which runs the django web server to allow for the use of selenium.

See : https://docs.djangoproject.com/en/1.8/topics/testing/tools/ for details.

Hitch serves as an effective drop in replacement for all of these. While slower, tests written
using hitch should exhibit a greater degree of :doc:`/glossary/test_realism`, :doc:`/glossary/isolation`
and looser :doc:`/glossary/coupling`.

Practical benefits:

* You can run a celery service alongside the test.
* Hitch test maintains stricter database isolation.
* It runs all services with faketime, allowing you to mock the forward passage of time via your tests.
* Looser coupling means that if you refactor or rewrite your application code, you should only need minimal changes to your tests.
* Hitch tests can more easily be made to be :doc:`/glossary/business_readable`.


Tox, PyEnv and Virtualenv
-------------------------

Tox is a small, popular python framework that can run unit tests in multiple python environments.
It can be used to run unit tests with multiple versions of python if those versions are installed.

PyEnv is a small application which can download and compile specific versions of python and
run them alongside one another.

Virtualenv is a tool for creating a python environment where you can install an isolated
group of packages which you can use to run or test an application that depends upon them.

Hitch can supplant tox for integration tests (See : :doc:`/howto/parameterize_test_cases`).

Hitch *bundles* pyenv and uses it to build a python virtualenv(s) for you.

It does this with two lines of code:

.. code-block:: python

    # Define the version of python you want
    python_package = PythonPackage(version="3.4.3")

    # Installs python 3.4.3 into ~/.hitchpkg (if it isn't already present)
    # Creates virtualenv in .hitch folder (if it doesn't already exist)
    python_package.build()

    # Python virtualenv you can use with your project:
    python_package.python == "/path/to/your/project/tests/.hitch/py3.4.3/bin/python"
    python_package.pip == "/path/to/your/project/tests/.hitch/py3.4.3/bin/pip"


The above applies to the following packages:

* hitchpython
* python-build


.. note::

    Hitch *also* uses virtualenv to isolate *itself* and the code it runs the
    :doc:`/glossary/execution_engine` with. This is a virtualenv created with
    your system's python 3.


py.test/nose/unittest2
----------------------

py.test, nose, unittest and unittest2 are all unit test frameworks, although they
are often used to write integration tests.

See :doc:`/faq/when_should_i_use_a_unit_test_and_when_should_i_use_an_integration_test`

[ TO DO : parameterization, readability, boilerplate to handle services, isolation features, loosely coupled, muliple services ]



Robot Framework
---------------

[ TO DO ]


Other technologies?
-------------------

If you'd like to see a comparison with other technologies here or would like to correct
something said above, raising a ticket is welcome:

https://github.com/hitchtest/hitch/issues/new
