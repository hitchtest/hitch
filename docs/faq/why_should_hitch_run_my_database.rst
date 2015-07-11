Why should Hitch run my database?
=================================

Hitch does not require you to let it run your database, or, indeed, any other
service for you, but there are several reasons why it might be a good idea.

Time Travel
-----------

If Hitch runs your database and you use hitchserve's time_travel method
to mock moving forward in time, your database will move forward too. Thus,
any queries that you run will also pick up the new time.

:doc:`/glossary/isolation`
--------------------------

If Hitch runs your database, the data files are kept isolated from other
tests and other databases installed on your system. This protects your tests
from modifications to the system DB environment and vice versa.


Version fixing
--------------

Hitch explicitly fixes the version of all of the software you use. This helps
remove a source of test :doc:`/glossary/indeterminacy` from your test scripts.
