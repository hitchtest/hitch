Why does Hitch not enforce the use of Given/When/Then?
------------------------------------------------------

The three core principles behind the :doc:`/glossary/hitch_test_description_language`
are :doc:`/glossary/DRY`, :doc:`/glossary/test_readability` and simplicity.

That is:

* The test cases should be as short as possible while still communicating everything that they need to.
* Readability and simplicity are paramount - which means dispensing with superfluous syntax and key words, and the need for custom parser engines.

Given/When/Then are key words used to signal to a person *writing* the
test the kind of pattern it should follow.

However, when the test case is finished, the meaning of the steps
should be implicit anyway, and since *all* test cases should follow
this pattern to some extent, the presence of the keywords becomes
more superfluous the more test cases you read and write.

The terms have no meaning to the :doc:`/glossary/execution_engine` and
are typically ignored.

.. note::

    You are still *able* to use the terms given, when and then in your
    test step names with hitch, you are just not forced to do so.
