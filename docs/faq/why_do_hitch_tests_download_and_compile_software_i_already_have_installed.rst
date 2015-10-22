Why do Hitch tests download and compile software I already have installed?
==========================================================================

Hitch takes a novel approach to integration testing that means that it will
often download and compile software which you *may already have installed*.

Some examples include:

* Python
* Postgresql
* Redis

This is done in order to help solve three common problems that plague
integration tests:

* :doc:`glossary/test_brittleness`
* :doc:`glossary/indeterminacy`
* :doc:`glossary/isolation`

While you *may have* postgresql installed on your computer when you ran
a hitch test, the actual version you have installed could be different
depending upon your OS, the version of your OS and the last time you
upgraded your OS.

It will also change *as you upgrade your OS*.

Since the actual version of the software installed is so often
*critically* important for chasing down obscure tear-your-hair-out bugs,
hitch takes the approach that, by default, it should download
and install critical components that your tests rely upon itself
and to let you *specify* the version as well.

Unfortunately this *will* often lead to a slower first test runs
and that software does take up extra space (it is all stored
in the folder ~/.hitchpkg if you are curious).

However, it'll save time in the long run, *especially* on complex
systems as it will mean you'll spend less time debugging the
"hair pulling problems" caused by using different versions of software
for development and production.
