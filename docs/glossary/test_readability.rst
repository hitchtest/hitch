Test Readability
================

Test readability is the idea that a test should be easily read by programmers
and non programmers alike.

Hitch takes the approach that readability should be a by-product of simplicity,
careful design and :doc:`/glossary/loose_coupling` and that readability is
a factor indicating a high :doc:`/glossary/test_quality`.

Test readability should mean that:

* Tests are written in a 'dumb' language rather than a turing complete programming language.
* Implementation details of the test should not be visible in the test itself.

Test readability does *not* mean that:

* Tests are written in full English sentences (English is usually far too imprecise a language to write tests in anyway).
* The tests do not use complex terminology - if it is relevant to the domain then it is relevant to the test.

Example of a readable, executable test written in the :doc:`/glossary/hitch_test_description_language`:

.. code-block:: yaml

    - name: Sign up, create reminder and wait for email reminder to arrive in python
      scenario:
        - Load website
        - Click: register
        - Fill form:
            id_username: django
            id_email: django@reinhardt.com
            id_password1: jazzguitar
            id_password2: jazzguitar
        - Click submit
        - Click: create
        - Fill form:
            id_description: Remind me about upcoming gig.
            id_when: 30 days
        - Click: create
        - Wait for email:
            Containing: Confirm E-mail Address
        - Confirm emails sent: 1
        - Time travel:
            Days: 30
        - Wait for email:
            Containing: Remind me about upcoming gig.


See also:

* :doc:`/howto/refactor_your_tests`
