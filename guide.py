# -*- coding: utf-8 -*-
import requests

from base import Base
from category import Category
from constants import API_BASE_URL
from step import Step

class Guide(Base):
   def __init__(self, guideid):
      self.id = guideid
   
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
      self.steps = [Step(step['guideid'], step['stepid'], data=step) for step in guide['steps']]
      self.type = guide['type']
      self.public = guide['public']
      self.revision = guide['revisionid']
      self.difficulty = guide['difficulty']
      #self.prerequisites = guide['prerequisites'],
      #                     guide['prereq_modified_date']
      #self.summary = guide['summary']
      #self.flags = guide['flags']

   @staticmethod
   def all(guideids=None, filter=None, order=None):
      '''
      all(iterable, string, string) -> iterable
      
      Returns a generator of Guide objects from the list of all guides.
      
      guideids: Only return Guides corresponding to these ids.
      filter:   Only return guides of this type.  Choices: installation,
                repair, disassembly, teardown, technique, maintenance.
      order:    Instead of ordering by guideid, order alphabetically.  Choices:
                ASC, DESC.
      '''
      parameters = []
      if guideids:
         parameters.append('guideids=%s' % ','.join(map(str, guideids)))
      if filter:
         parameters.append('filter=%s' % filter)
      if order:
         parameters.append('order=%s' % order)
      parameters = '&'.join(parameters)
      
      offset = 0
      limit = 5 # Tune this to balance memory vs. frequent network trips.
      guideJSONs = []
      while True:
         if not guideJSONs:
            url = '%s/guides?offset=%s&limit=%s&%s' \
                  % (API_BASE_URL, offset, limit, parameters)
            response = requests.get(url)
            guideJSONs = response.json()
            # Are we at the end of pagination?
            if not guideJSONs:
               return
            offset += limit
         yield Guide(guideJSONs.pop(0)['guideid'])
   
