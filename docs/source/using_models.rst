Models Usage
============

Working with Province
---------------------

- Importing Province from a model

.. code-block:: python

  from nepali_address.models import Province

- Get all Provinces

.. code-block:: python

  all_provinces = Province.objects.all()

- Get province by name and get corresponding districts

.. code-block:: python

  province_1 = Province.objects.get(name='Province 1')

  province_1_district = province_1.get_districts()

Working with District
---------------------

- Importing District from a model

.. code-block:: python

  from nepali_address.models import District

- Get all Districts

.. code-block:: python

  all_districts = District.objects.all()

- Get district by name and get corresponding province / municipalities

.. code-block:: python

  kathmandu_district = District.objects.get(name='Kathmandu')

  province_of_kathmandu = kathmandu_district.get_province()

  municipalities_of_kathmandu = kathmandu_district.get_municipalities()

Working with Municipality
-------------------------

- Importing Municipality from a model

.. code-block:: python

  from nepali_address.models import Municipality

- Get all municipalities

.. code-block:: python

  all_municipalities = Municipality.objects.all()

- Get municipality by name and get corresponding district / province

.. code-block:: python

  ajayameru_municipality = Municipality.objects.get(name='Ajayameru Rural Municipality')

  district_of_ajayameru_municipality = ajayameru_municipality.get_district()
  
  province_of_ajayameru_municipality = ajayameru_municipality.get_province()

**You may use various model operations as well.**