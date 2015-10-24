What about python 2?
====================

This hitch framework only runs in python 3.

The bootstrapper (which runs fine in python 2 and 3) installs hitch
in its own isolated virtualenv in the .hitch directory.

This means that the code you write in the :doc:`/glossary/engine.py` and any
code it imports must be python 3 code.


My code only runs in python 2. Can I test it with hitch?
--------------------------------------------------------

Yes. You can test your code in any version of python 2 from 2.6.6 to 2.7.10
and any version of python 3 from 3.2 to 3.5.0 and any combination of those
versions.
