# -*- coding: utf-8 -*-
import requests
from datetime import datetime

from base import Base
from category import Category
from constants import API_BASE_URL
from image import Image
from step import Step

class Guide(Base):
   def __init__(self, guideid):
      self.id = guideid
   
   def refresh(self):
      response = requests.get('%s/guides/%s' % (API_BASE_URL, self.id))
      attributes = response.json()
      
      self.category = Category(attributes['category'])
      self.url = attributes['url']
      
      self.title = attributes['title']
      if attributes['image']:
         self.image = Image(attributes['image']['id'])
      else:
         self.image = None
      self.locale = attributes['locale']
      #self.introduction = WikiText(attributes['introduction_raw'],
      #                             attributes['introduction_rendered'])
      #self.conclusion = WikiText(attributes['conclusion_raw'],
      #                           attributes['conclusion_rendered'])
      #self.tools = attributes['tools']
      #self.parts = attributes['parts']
      self.subject = attributes['subject']
      #self.modifiedDate = attributes['modified_date']
      self.createdDate = datetime.utcfromtimestamp(attributes['created_date'])
      self.publishedDate = datetime.utcfromtimestamp(attributes['published_date'])
      #self.documents = attributes['documents']
      author = attributes['author']
      #self.author = User(author['userid'], name=author['text'])
      #self.timeRequired = attributes['timeRequired']
      self.steps = [Step(step['guideid'], step['stepid'], data=step) for step in attributes['steps']]
      self.type = attributes['type']
      self.public = attributes['public']
      self.revision = attributes['revisionid']
      self.difficulty = attributes['difficulty']
      #self.prerequisites = attributes['prerequisites'],
      #                     attributes['prereq_modified_date']
      #self.summary = attributes['summary']
      #self.flags = attributes['flags']

   @staticmethod
   def all(guideids=None, filter=None, order=None):
      '''
      Fetch all guides.
      
      :param iterable guideids: Only return Guides corresponding to these ids.
      :param string filter: Only return guides of this type.  Choices:
                            installation, repair, disassembly, teardown,
                            technique, maintenance.
      :param string order: Instead of ordering by guideid, order alphabetically.
                           Choices: ASC, DESC.
      :rtype: generator of :class:`pyfixit.guide.Guide` objects.
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
   
