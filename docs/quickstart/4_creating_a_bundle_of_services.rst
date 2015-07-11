4: Creating a bundle of services
================================

To do most forms of integration testing requires services. The example application,
Django-RemindMe-Tests requires not only Django, but also Celery, Redis, Postgresql,
Selenium and a Mock SMTP server to all be running concurrently while a test is
in progress.

Each one of these operates independently, logs messages independently, have their
own set of prerequisites and stop independently.

A module called hitchserve handles running these services and doing all of the
boilerplate required (multithreading, reacting to events, stopping, killing),
as well as providing a clean, generic API to allow the configuration, set up
and launching of specific services.

Your app will also have its own bundle of services to run. To run this bundle,
however, your app needs to set up its own bundle first. To do this, first
install hitchserve::

  $ hitch install hitchserve

Then, add the following lines to your test engine, so it looks something like
this:

.. code-block:: python

    from hitchserve import ServiceBundle
    from subprocess import call
    import hitchpython
    import hitchtest
    from os import path

    PROJECT_DIRECTORY = path.abspath(path.join(path.dirname(__file__), '..'))

    class YourProjectTestExecutionEngine(hitchtest.ExecutionEngine):
        def set_up(self):
            # From previous tutorial step
            pydir = path.join(PROJECT_DIRECTORY, "py")
            python_package = hitchpython.PythonPackage(python_version=self.settings['python_version'], directory=pydir)
            python_package.build()
            python_package.verify()
            call([python_package.pip, "install", "-r", "requirements.txt"])

            # Define the service bundle, prior to defining its contents
            self.services = ServiceBundle(
                project_directory=PROJECT_DIRECTORY,    # The directory containing the project to be tested
                startup_timeout=10,                     # How long to wait for the services to start before giving up and throwing an error.
                shutdown_timeout=5                      # How long to wait for the services to stop before killing them.
            )

            # [ We will be putting service definitions here in the next stage of the tutorial ]

            # Actually start the services
            self.services.startup(interactive=False)    # interactive = False means that hitchserve takes control of logging.

        def pause(self):
            if hasattr(self, 'services'):
                # hasattr(self, 'services') allows self.pause() to be run prior to the service bundle being defined as well as after.
                self.services.start_interactive_mode()  # hitchserve yields control of screen output so that ipython can take over.
            hitchtest.ipython_embed()
            if hasattr(self, 'services'):
                self.services.stop_interactive_mode()   # hitchserve takes back control of screen output and starts logging again.

        def tear_down(self):
            if hasattr(self, 'services'):
                self.services.shutdown()                # hitchserve shuts down all of its services (of which there are currently none).


