Roadmap
=======

This is a non-exhaustive list of features which are planned for the future, in no particular order:

* Service plugins for lots more popular databases, web frameworks, task queues and more - even in PHP, Java, Ruby, etc. and tutorials to use them.
* Use of py.test's assert statement.
* Tests that repeat themselves with % pass/failure and a threshold for passing (default 100%), for those annoying integration tests that only fail sometimes due to race conditions.
* Configurable mid-steps - running an engine method between each test step - e.g. to pause mid-step when using tests for demonstrations or take screenshots.
* Tools to let you stop and start services mid-test, e.g. to test how they behave when receiving different UNIX signals, or to mock scenarios where services are restarted.
* Step skipping 
* Bisect - tools to be able to figure out which commit caused a test failure during long test runs.
* Mock REST server
* CPU/Memory/I/O tracking for services.
* Artefact generation - a seamless way of creating artefacts from tests such as screenshots, CPU/Memory/I/O usage reports, code coverage reports, etc.
