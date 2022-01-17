Understanding Models
====================

Three models namely Province, District and Municipality are provided for use.

Province
--------

#. contains one field
    #. name - Charfield

District
--------

#. contains two field
    #. name - Charfield
    #. province - ForeignKey to Province

Municipality
------------

#. contains two field
    #. name - Charfield
    #. district - ForeignKey to District