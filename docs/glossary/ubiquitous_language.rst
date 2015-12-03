Ubiquitous Language
===================

An ubiquitous language is a concept from :doc:`behavior_driven_development`. It defines
a language which you can use to communicate precise requirements between stakeholders
and developers.

In order to function as a medium for communication this language should be
:doc:`stakeholder_readable`.

This often means that the ubiquitous language cannot be turing complete code
(the more powerful a language is, the less readable it tends to be,
so the less likely it can be used as an ubiquitous language) unless the product
is a library for consumption by developers.

Most projects will require the highest level acceptance tests to be :doc:`business_readable`
in order for them to be useful as a means of communication between stakeholders and
developers.

Hitch provides the framework for developers to create an ubiquitous language for their
projects.

The :doc:`hitch_test_description_language` is a metalanguage built upon YAML which allows
you to define your own vocubulary (as a series of steps or preconditions) and sub-languages.

Hitch does come with a body of :doc:`step libraries <step_library>` that define common
:doc:`stakeholder_readable` steps (e.g. 'click'), but usage of these is optional.

See also:

* :doc:`/faq/why_just_html_ids_and_classes`
* :doc:`ubiquitous_language_abandonment`
