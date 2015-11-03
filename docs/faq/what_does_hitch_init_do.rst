What does hitch init do?
========================

The "hitch init" command creates a :doc:`/glossary/hitch_directory`
in the current directory if one does not already exist. Inside this
directory it installs a :doc:`/glossary/virtualenv` with the "hitchtest" package
and dependencies, or, if a :doc:`/glossary/hitchreqs.txt` is found,
all of the packages
specified in "hitchreqs.txt"

This virtualenv contains only the packages required to run tests.
It does *not* contain the packages required to actually run your app.
The tests themselves will take care of setting those up in a separate
virtualenv.

See also:

* :doc:`/faq/what_does_the_init_script_do`
