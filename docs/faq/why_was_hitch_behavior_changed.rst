Why was hitch behavior changed?
===============================

This FAQ is gives explanations for behaviors that were changed in Hitch.


Why will my tests no longer run with the default filename "settings.yml"?
-------------------------------------------------------------------------

settings.yml used to be the default hitch settings filename. If no other settings file was specified,
your test settings would be pulled from this filename. If you specified another filename on
the command line, settings would be pulled from that *instead*.

The behavior has now changed. Settings are now *always* pulled from the filename 'all.settings'
if it exists, but settings in any filename specified via --settings will always take precedence.

Settings are now taken from (in order of precedence):

* The JSON specified on the command line via --extra.
* The YAML filename specified via --settings.
* all.settings

See :doc:`/api/settings` for more information.


Why did you remove the --quiet switch?
--------------------------------------

--quiet is more appropriate as a setting, so it has been deprecated as a
command line switch and will be removed entirely in version 1.0.

You can still make your tests quietly by setting the property to true
on the command line via --extra::

  $ hitch test . --extra '{"quiet":true}'

Or by adding the setting to a specified settings file, e.g. ::

  quiet: True

See :doc:`/api/settings` for more information.
