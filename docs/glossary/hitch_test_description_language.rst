Hitch Test Description Language
===============================

The hitch test description language is a YAML-based language for describing
tests which are executable. Example:

.. code-block:: yaml

  - name: First scenario
    tags:
      - registration
      - email
      - firefox
    scenario:
      - Step 1
      - Step 2

  - name: Second scenario
    tags:
      - registration
      - email
      - firefox
    preconditions:
      property1: a
      property2: b
    scenario:
      - Step 1
      - Step 2



.. warning::

    This part is not implemented yet, but it is coming soon.

The hitch test description language is a restricted *subset* of YAML from the
project `DumbYAML <https://github.com/crdoconnor/dumbyaml>`. It does this
to prevent confusing and surprising effects caused by the more complex YAML
features and YAML's implicit typing.

E.g. the following data, whether represented in a test step, preconditions or
test settings::

  - 3.5
  - -1
  - yes
  - false

Will be sent to your python engine code as the following list::

    ["3.5", "-1", "yes", "false", ].

See :doc:`/api/engine_api` for documentation and a more extensive overview.
