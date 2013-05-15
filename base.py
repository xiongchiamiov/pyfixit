# -*- coding: utf-8 -*-

class Base(object):
   def __getattr__(self, name):
      self.refresh()
      try:
         return self.__dict__[name]
      except KeyError:
         raise AttributeError("'%s' object has no attribute '%s'" % \
                              (self.__class__.__name__, name))

