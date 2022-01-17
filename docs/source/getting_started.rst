Getting started
===============

Requirements
------------

* Python (3.7, 3.8, 3.9, 3.10)
* Django (2.2, 3.1, 3.2, 4.0)

These are the officially supported python and package versions.  Other versions
will probably work.  You're free to modify the tox config and see what is
possible.

Installation
------------
dj-nepali-address can be installed with pip::

  pip install dj-nepali-address

Then, your django project must be configured to use the library.  In
``settings.py``, add ``nepali_address`` to ``INSTALLED_APPS``.

.. code-block:: python

  INSTALLED_APPS = [
      ...
      'nepali_address',
      ...
  ]

Run ``python manage.py migrate`` to create the nepali_address models.

Run ``python manage.py loaddata nepali_address`` to load data in nepali_address models.