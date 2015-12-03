Hitch Test Description Language
===============================

The hitch test description language is a `StrictYAML <https://github.com/crdoconnor/strictyaml>` based
language for describing executable high level functional tests. Example:

.. code-block:: yaml

  - name: First scenario
    tags:
      - registration
      - email
      - firefox
    preconditions:
      property1: a
      property2: b
    scenario:
      - Step 1
      - Step 2: 
      - Step 3:
          parameter1: a
          parameter2: b
          parameter3:
            - list item 1
            - list item 2
      - Step 4


See also:

* :doc:`/api/engine_api`
* :doc:`/faq/how_does_hitch_compare_to_other_technologies`
* :doc:`/howto/parameterize_test_cases`
