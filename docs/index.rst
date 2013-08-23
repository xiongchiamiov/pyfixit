.. pyfixit documentation master file, created by
   sphinx-quickstart on Sat Aug 17 10:10:21 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to pyfixit's documentation!
===================================

`iFixit`_ has tons of cool information on how to repair stuff.  Now you can
access all of that goodness as easy-to-use Python objects. ::

   >>> from pyfixit import Guide
   >>> guide = Guide(13682)
   >>> guide.image.thumbnail
   u'https://d3nevzfk7ii3be.cloudfront.net/igi/rJxj4HJ4tKBqvcvW.thumbnail'
   >>> for step in guide.steps:
   ...    for line in step.lines:
   ...       print '(%s) %s' % (line.bullet, line.text)
   ...
   (icon_reminder) Before we begin, we want to make it clear [snip]
   (black) While not much is known in terms of tech specs, [snip]
   [snip]

.. _iFixit: http://www.ifixit.com/

.. toctree::
   :maxdepth: 2

   user_guide
   pyfixit


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

