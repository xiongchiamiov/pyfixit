PyFixit User Guide
==================

Installation
------------

TODO

Basic Usage
-----------

PyFixit requires no setup; merely import the classes you want and construct
them::

   >>> from pyfixit import Guide
   >>> guide = Guide(5)
   >>> guide.title
   'Installing PowerBook G3 Wallstreet Processor'

An attempt is made to reduce the number of API calls; thus, many attributes are
lazily-fetched on request.  To avoid this, use the ``refresh()`` method on an
object::

   >>> from pyfixit import Guide
   >>> guide = Guide(5)
   >>> guide.title           # Triggers API call.
   'Installing PowerBook G3 Wallstreet Processor'
   >>> guide.difficulty      # Already in memory!
   'Easy'
   
   >>> guide = Guide(13682)
   >>> guide.refresh()      # Triggers API call.
   >>> guide.title          # Already in memory!
   'Oculus Rift Teardown'

``refresh()`` can be called at any time to fetch updates to the object.

Example Application
-------------------

The `ifixit-repairability-scores`_ project uses PyFixit to extract
repairability scores from iFixit's teardowns.

.. _ifixit-repairability-scores: https://github.com/xiongchiamiov/ifixit-repairability-scores

