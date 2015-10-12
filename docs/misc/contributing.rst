Contributing to Hitch
=====================

Hi and welcome! Thanks for your interest in contributing to Hitch!

There's a number of things you can do to help its progress:


#1 Fill out my survey
---------------------

Who are you? What do you want? What do you need help with? I'd like to know!

Your input can help greatly in guiding the future development of Hitch.

[ survey not yet ready. check back soon. ]



#2 Run the example project on a currently untested environment
--------------------------------------------------------------

See :doc:`/tested_on` for details.

Just follow the 3 step directions on https://hitchtest.com/ to run the test on your environment.

If it works, please consider editing and adding it to https://github.com/hitchtest/hitch/blob/master/docs/tested_on.rst
or raising an issue with the details.

If it doesn't work, please raise an issue and copying and paste the output you saw.


#3 Report *any* issues you see at any time
------------------------------------------

If you're not sure if what you saw really was a bug, raise an issue anyway. Copy and paste the output.

If you're not sure if it was your fault or not, please still raise an issue. Copy and paste the output.

If it's not clear and simple and easy to understand what happened, it's *probably a bug*.




#4 Raise an issue for anything that confused you in the documentation or you thought was missing
------------------------------------------------------------------------------------------------

Writing documentation is hard. What is obvious to the documentor won't necessarily
seem obvious to the user. I'd really like to see more of these.


#5 Help out with the unixpackage project
----------------------------------------

Hitch is substantially reliant upon this project, but it still needs a lot
of (mostly sysadmin-y non-programming) work.

See https://github.com/unixpackage/unixpackage/blob/master/CONTRIBUTING.rst for details.


Contributing code
=================

Pull requests are welcome too, of course. If you submit a PR to any hitch project, please
remember to sign the CLA:

https://www.clahub.com/agreements/hitchtest/hitch

There's no cloud continuous integration but all code is thoroughly tested
before being deployed to pypi.

My ideal pull request would be:

* Small and self contained (ideally just a few lines)
* Pythonic and elegant (see Raymond Hettinger's talks for an idea of what that means)
* You've run that code at least once
* You'll amend it based upon any comments I might have

100% bug-free isn't a requirement. If I discover a problem during regression
tests and the code breaks under certain less than obvious conditions, that's
my problem. If it breaks some other part of the system that's my problem too.

If you want to get started fixing or implementing something, but you're not sure how,
raise an issue.

