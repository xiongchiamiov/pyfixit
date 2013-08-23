User Guide
==========

Installation
------------

The easiest method is to use `pip`_::

   [$]> pip install pyfixit

.. _pip: http://www.pip-installer.org/en/latest/

Basic Usage
-----------

PyFixit requires no setup; merely import the classes you want and construct
them::

   >>> from pyfixit import Guide
   >>> guide = Guide(5)
   >>> guide.title
   u'Installing PowerBook G3 Wallstreet Processor'

An attempt is made to reduce the number of API calls; thus, many attributes are
lazily-fetched on request.  To avoid this, use the ``refresh()`` method on an
object::

   >>> from pyfixit import Guide
   >>> guide = Guide(5)
   >>> guide.title           # Triggers API call.
   u'Installing PowerBook G3 Wallstreet Processor'
   >>> guide.difficulty      # Already in memory!
   u'Easy'
   
   >>> guide = Guide(13682)
   >>> guide.refresh()      # Triggers API call.
   >>> guide.title          # Already in memory!
   u'Oculus Rift Teardown'

``refresh()`` can be called at any time to fetch updates to the object.

Example Application
-------------------

The `ifixit-repairability-scores`_ project uses PyFixit to extract
repairability scores from iFixit's teardowns.

.. _ifixit-repairability-scores: https://github.com/xiongchiamiov/ifixit-repairability-scores

