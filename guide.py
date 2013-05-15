# -*- coding: utf-8 -*-
import requests

from category import Category
from constants import API_BASE_URL

class Guide(object):
   def __init__(self, guideid):
      self.id = guideid
      
   def __getattr__(self, name):
      self.refresh()
      try:
         return self.__dict__[name]
      except KeyError:
         raise AttributeError("'Guide' object has no attribute '%s'" % name)
   
   def refresh(self):
      response = requests.get('%s/guides/%s' % (API_BASE_URL, self.id))
      attributes = response.json()
      
      self.category = Category(attributes['category'])
      self.url = attributes['url']
      
      guide = attributes['guide']
      self.title = guide['title']
      #self.image = guide['image']
      self.locale = guide['locale']
      #self.introduction = WikiText(guide['introduction_raw'],
      #                             guide['introduction_rendered'])
      #self.conclusion = WikiText(guide['conclusion_raw'],
      #                           guide['conclusion_rendered'])
      #self.tools = guide['tools']
      #self.parts = guide['parts']
      self.subject = guide['subject']
      #self.modifiedDate = guide['modified_date']
      #self.documents = guide['documents']
      author = guide['author']
      #self.author = User(author['userid'], name=author['text'])
      #self.timeRequired = guide['timeRequired']
      #self.steps = guide['steps']
      self.type = guide['type']
      self.public = guide['public']
      self.revision = guide['revisionid']
      self.difficulty = guide['difficulty']
      #self.prerequisites = guide['prerequisites'],
      #                     guide['prereq_modified_date']
      #self.summary = guide['summary']
      #self.flags = guide['flags']
   
