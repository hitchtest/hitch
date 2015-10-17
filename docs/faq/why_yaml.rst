Why YAML?
=========

The :doc:`/glossary/hitch_test_description_language` is built upon YAML -
a markup language for presenting structured data.
All tests are subset of YAML.

Hitch also provides you with the popular templating tool
Jinja2 to let you *generate* a lot of very similar
test cases without copying and pasting.


Why write tests with YAML instead of Python?
--------------------------------------------

The hitch test description language is an *intentionally dumb language*
with a restricted feature set.

It is *not* a full programming language like python. You cannot use
conditionals, loops, etc. It is just a simple sequence of steps and
some data. It's essentialy just configuration, in other words.

This may feel like handcuffs to a good programmer, but there's a good
reason for it: less powerful languages are easier to understand.

This means that it becomes easier to maintain, and easier to keep
free from bugs and also even means that you can show it to customers
or product managers/owners. With some training they may even be
able to write in it (it's really no more complicated than handling
a spreadsheet).

Jinja2 adds additional complexity, but it helps you to prevent your
test suite from becoming repetitive. See: :doc:`/glossary/DRY`.

Again, using Jinja2 is not a powerful language (more powerful
than YAML but less powerful than python/java/ruby/etc.) and should be
something that somebody who uses advanced features on a spreadsheet
could pick up in a day.


Why YAML instead of Gherkin?
----------------------------

Some readers may be familiar with Gherkin, which follows the same
pattern. It is another intentionally dumb (i.e. non turing complete)
language.




Related reading
---------------

* https://en.wikipedia.org/wiki/Rule_of_least_power
* https://en.wikipedia.org/wiki/Separation_of_concerns

The use of YAML and Jinja2 in Hitch was inspired somewhat by Ansible: https://en.wikipedia.org/wiki/Ansible_%28software%29
