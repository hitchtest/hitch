How is Hitch extensible?
========================

Hitch is an integration testing framework built upon python. While there is a lot of in-built
functionality, you will find at some point that the included portions of hitch are not sufficient
to mimic realistic scenarios.

Easy step definition
====================

While Hitch contains a myriad of in-built steps to perform common tasks like clicking on buttons
and receiving emails, it probably won't do everythingthat you need. For this reason you will need to
occasionally define your own steps. 

  - Click: my-button
  - Do some fancy thing
  - Click:

Loose :doc:`/glossary/coupling`
===============================

Hitch is built with loose coupling in mind at every level.



Installed from PyPi into a Virtualenv
=====================================

Hitch packages itself as a 
