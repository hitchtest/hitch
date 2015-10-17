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

See :doc:`api/engine_api` for documentation and a more extensive overview.
