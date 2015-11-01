Environment Isolation
=====================

Environment isolation is a kind of :doc:`/glossary/isolation`
enforced by hitch where potential *environmental* causes of test failure
are prevented from affecting test results.

Lack of environment isolation is a common source of :doc:`/glossary/brittle_tests`.

The environment is defined here as "anything out of the test's
control".

Hitch responds to these environmental issues by failing at
the beginning of the test with a clear message (see also
:doc:`/glossary/fail_fast` and :doc:`/glossary/fail_clearly`).

Common environmental causes for test failure, which hitch
detects for include:

* Lack of reliable internet access
* Missing system packages (via unixpackage) (this is also a form of :doc:`/glossary/package_isolation`)
* Lack of memory
* 32 bit vs. 64 bit system
* Lack of available disk space
* Network ports that are already in use by another process (this is also process isolation)

See also:

* :doc:`/glossary/data_isolation`
* :doc:`/glossary/process_isolation`
* :doc:`/glossary/package_isolation`
