=========================
Python dummy_data Package
=========================

Create dummy data dynamically.

Simple Example
--------------

.. code:: python

    import dummy_data

    folder = dummy_data.random_structure("folder/path", 10, 2)
    dummy_data.create(folder)
