Why YAML?
=========

YAML is a markup language for presenting structured data. It is
effectively a more readable version of JSON.

It is used for configuration - for the settings file - because
it is 

It is used both for writing test scripts and for settings files.

Python developers who are new to Hitch might wonder why it uses YAML
as a test description language, rather than python itself.

Python is what is known as a turing complete language. This means
that is is very powerful and can theoretically perform any task
that any other programming language can.

This is good if you want to write powerful, capable programs.

This comes with a significant down side, however. Turing complete
languages are significantly more susceptible to technical debt
and are less readable by non-programmers.

YAML is *not* turing complete language. However, since all test
descriptions are effectively declarative and linear - step 1 is
followed by step 2, which is followed by step 3, etc. you do not
actually *need* a turing complete language to describe the test in.

Thus by using this language to describe tests, they can be kept
simple, readable and (mostly) free of technical debt.

For more powerful and customized behavior, you can still
write python code in the test engine.
