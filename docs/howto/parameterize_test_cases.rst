How to Parameterize your Test Cases with Hitch
==============================================

Test case parameterization is a way of taking an existing test case and
tweaking it to run multiple times, each in a slightly different way with
just a couple of lines.

For example:

* Taking a test case that runs a scenario on python 2.7.10 and making it also run on python 3.4.3 and 3.5.0.
* Taking a test case that runs on firefox and making it run on 4 other browsers.
* Creating a group of test cases for a particular feature that differ only slightly.

I'd recommend parameterization only *after* noticing that your test cases
have gotten somewhat repetitive. In general it is something that you should
*avoid* doing pre-emptively.

Strictly speaking it is not *necessary* to parameterize your test cases since
you can just copy and paste and tweak the things that you need. However, it's
a good idea to make your test cases :doc:`/glossary/DRY` just like any other
code to make them easier to maintain.


Example
-------

In your all.settings, put the following variable::

    python_versions:
      - 2.7.10
      - 3.4.3
      - 3.5.0

This is a list of 3 python versions. This list is made available to jinja2 (jinja2 is basically anything surrounded by { or }).

Now put a test in the same directory, with the extension .test and make it look something like this::

    {% for python_version in python_versions %}
    - name: Load website and click register (python {{ python_version }})
      preconditions:
        python_version: "{{ python_version }}"
      tags:
        - registration
        - py{{ python_version }}
      scenario:
        - Load website
        - Click: register
    {% endfor %}

This code with a for loop - will *generate* three *almost identical* test cases with the following differences:

* The name (each one will have the *same* name except with a different python version number at the end)
* One of the tags - the tags will be py3.5.0, py3.4.3 and py2.7.10 respectively. All three will have the tag "registration" though.
* The precondition "python_version" - each one of them will have the preconditions set differently.

This is what it does:

* The {% for python_version in python_versions %} and {% endfor %} surround a *block* of test description that it repeats.
* It loops 3 times because python_versions, set in all.settings, has 3 versions.
* Anything surrounded by {{ and }} in the block is set to 2.7.10, 3.4.3 and 3.5.0.

There are plenty more tricks you can play with parameterized test cases. I recommend
gaining familiarity with Jinja2 if you want to do more.

Careful, though - parameterization can help with reducing the repetitiveness of your
test cases but it can also make them less readable.
