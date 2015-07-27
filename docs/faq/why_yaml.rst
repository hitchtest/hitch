Why YAML?
=========

YAML is a markup language for presenting structured data. It is
a more readable version of JSON.

Hitch uses YAML as a declarative description language for integration
tests.

While python could be used to write integration tests instead,
YAML is more suitable as it lets your tests adhere to the following
two principles more easily:

* https://en.wikipedia.org/wiki/Rule_of_least_power - YAML is a *less* powerful language than python, so using it instead will keep your tests simpler.
* https://en.wikipedia.org/wiki/Separation_of_concerns - YAML provides a 'language barrier' that lets you maintain a strict separation of concerns between the code which describes your tests and the code which runs them.

For more powerful and customized behavior, you can write python code in the test engine.

The use of YAML and Jinja2 in Hitch was inspired somewhat by Ansible: https://en.wikipedia.org/wiki/Ansible_%28software%29
