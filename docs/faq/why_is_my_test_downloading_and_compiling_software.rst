Why is my test downloading and compiling software?
--------------------------------------------------

Hitch often downloads and compiles the software it uses to run your
test with for two main reasons - 1) it allows you to specify the version
of software you are testing with in your test, 2) it allows you to
test your code with multiple versions of software. For example, you
can easily write tests with hitch that test your code using python 2.6
and python 3.3 even if your system comes with python 2.7 by default.

Specifying the version of software is also an important means of
reducing integration test brittleness. Tests run on different machines
(and even different OSes) can largely be relied upon to fail or
pass together. It also somewhat prevents system software upgrades from
breaking your tests.

Lastly, specifying the version means that you can test with the exact
versions of software that you use in production, thus keeping your
tests as realistic as possible.

See also:

* :doc:`why_does_the_first_test_run_take_so_long`
