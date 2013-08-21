# -*- coding: utf-8 -*-

class Base(object):
   '''Base object defining common behavior for all API objects.
   
   Objects inheriting from this class should implement a ``refresh()`` method
   that fetches any data it has been waiting to lazily-load.
   '''
   def __getattr__(self, name):
      self.refresh()
      try:
         return self.__dict__[name]
      except KeyError:
         raise AttributeError("'%s' object has no attribute '%s'" % \
                              (self.__class__.__name__, name))

