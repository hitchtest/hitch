Whiplash driven development
===========================

Whiplash driven development is an ultra-productive style of :doc:`/glossary/acceptance_test_driven_development`
where:

1. The developer runs a single acceptance test to develop against, running it in whiplash mode.
2. This runs the test once.
3. Thereafter, the test is immediately re-run after a code change is detected (i.e. when the save button in the text editor/IDE is clicked).
4. If a previous test run was in progress when that happens, it is *aborted* as soon as the filesystem change is detected and the test is re-run.
5. Sounds are used to signal the start of a test (e.g. gunshot), a passed test (happy sound) or failed test (sad sound).
6. After a test run is completed (successfully or not), the test is paused and a debugging console is opened.
7. Acceptance tests are ideally designed to take under 60 seconds to pass and designed to :doc:`/glossary/fail_fast`.

The goals of whiplash driven development are:

* To minimize :doc:`/glossary/requirements_angst`.
* To take *all repetitive behavior* out of the hands of the developer - e.g. running commands (test runs), setting up environments, clicking on buttons.
* Automatically provide debugging tools and logs at the point of failure so the developer can more easily track down the cause of failures.
* To minimize or eliminate :doc:`/glossary/code_fear` by providing the necessary feedback as quickly as possible.
* To make refactoring and development feel more like a game (with sound effects).
* To remove enough distractions so that the developer can focus all of their concentration on writing code, and thus enter 'the zone' more often.



Tools
-----

* `patrols <https://github.com/crdoconnor/patrol>`_ can be used to detect file system changes and re-run hitch tests.
* `patrols <https://github.com/crdoconnor/kaching>`_ can be used to make sound effects during the beginning of set_up, on_success or on_failure.
* A testing tool like hitch is needed to write realistic high level acceptance tests with.
* A powerful machine is usually a prerequisite for doing whiplash driven development.
