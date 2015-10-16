DRY
===

DRY means "don't repeat yourself". A lack of repetition is a primary signifier of good, maintainable code.

A good way of cleaning up code is to look for repetitive patterns and de-duplicate them.

Since tests are also code, the same rules apply. Test code should be non-repetitive and tests themselves
should be non-repetitive. Tests should regularly be refactored by looking for repetition and removing
it by parameterizing your test cases.

Hitch provides the use of Jinja2 as a templating language to let you generate lots of similar tests
without writing a lot of duplicated test cases. See :doc:`howto/parameterize_test_cases` for a guide
on how to use it.

See also: `Don't Repeat Yourself Wikipedia Page <https://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`_
