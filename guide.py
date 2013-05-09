# -*- coding: utf-8 -*-
import requests

from category import Category

API_BASE_URL = 'https://www.ifixit.com/api/1.1'

class Guide(object):
   _attributes = ['category']
   
   def __init__(self, guideid):
      self.id = guideid
      
   def __dir__(self):
      return dir(super(Guide, self)) + self._attributes
   
   def __getattr__(self, name):
      if name not in self._attributes:
         raise AttributeError("'Guide' object has no attribute '%s'" % name)
      self.refresh()
      return self.__dict__[name]
   
   def refresh(self):
      response = requests.get('%s/guides/%s' % (API_BASE_URL, self.id))
      attributes = response.json()
      
      self.category = Category(attributes['category'])
   
