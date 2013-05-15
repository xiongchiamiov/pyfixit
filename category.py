# -*- coding: utf-8 -*-
import requests

from constants import API_BASE_URL

class Category(object):
   def __init__(self, name):
      self.name = name
   
   def __str__(self):
      return self.name
   
   def __repr__(self):
      return '<Category %s>' % self.name

   def __getattr__(self, name):
      self.refresh()
      try:
         return self.__dict__[name]
      except KeyError:
         raise AttributeError("'Category' object has no attribute '%s'" % name)
   
   def refresh(self):
      response = requests.get('%s/categories/%s' % (API_BASE_URL, self.name))
      attributes = response.json()
      
      self.categories = [Category(name) for name in attributes['categories']]
      #self.contents = WikiText(attributes['contents_raw'],
      #                         attributes['contents_rendered'])
      self.description = attributes['description']
      #self.flags = attributes['flags']
      #self.guides = attributes['guides']
      #self.image = attributes['image']
      self.locale = attributes['locale']
      #self.parts = attributes['parts']
      #self.solutions = attributes['solutions']
      self.title = attributes['title']
      #self.tools = attributes['tools']
      #self.topic_info = attributes['topic_info']

