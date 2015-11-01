Why YAML?
=========

The :doc:`/glossary/hitch_test_description_language` is built upon YAML -
a markup language for presenting structured data.

Hitch also integrates the popular templating tool
Jinja2 to let you *generate* a lot of very similar
test cases in YAML without copying and pasting.


Why write tests with YAML instead of Python?
--------------------------------------------

The hitch test description language is an *intentionally dumb language*
with a restricted feature set.

It is *not* a full programming language like python**. You cannot use
conditionals, loops, etc. It is just a simple sequence of steps and
some data. It is essentially just configuration, in fact.

This may feel like handcuffs to a good programmer, but there's a good
reason for it: less powerful languages are easier to understand and
since tests are just series of steps, you do not *need* a powerful
language to describe them.

Less powerful, easier to understand languages also have the following benefits:

* They are easier to maintain
* They are easier to keep free from bugs.
* You can *template* them and they are *still* relatively easy to understand, maintain and keep bug free.

Easier to understand also means that advanced programming skills are
not necessary to write them. Some training and understanding is
required - it's certainly not written English (for good reason),
but it's more like learning how to use a spreadsheet rather than
learning how to program in a turing complete language like python.

Jinja2 adds additional complexity, but it helps you to prevent your
test suite from becoming repetitive. See: :doc:`/glossary/DRY`.

Again, Jinja2 is not a powerful language. It is more powerful
than YAML but less powerful than python/java/ruby/etc. and should be
something that a non programmer could pick up and use productively
with a minimum of training.

Related reading
---------------

* https://en.wikipedia.org/wiki/Rule_of_least_power
* https://en.wikipedia.org/wiki/Separation_of_concerns

The use of YAML and Jinja2 in Hitch was inspired somewhat by Ansible: https://en.wikipedia.org/wiki/Ansible_%28software%29

