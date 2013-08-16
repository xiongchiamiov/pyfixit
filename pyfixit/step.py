# -*- coding: utf-8 -*-
import requests

from base import Base
from constants import API_BASE_URL
from line import Line

class Step(Base):
   def __init__(self, guideid, stepid, data=None):
      self.guideid = guideid
      self.stepid = stepid
      
      # Usually we're going to have a blob of data, since a GET of a guide
      # includes all the data of its steps.
      if data:
         self._update(data)
      
   def refresh(self):
      # There's no GET endpoint for steps, so get the parent guide and loop
      # through its steps until we find the right one.
      response = requests.get('%s/guides/%s' % (API_BASE_URL, self.guideid))
      attributes = response.json()
      
      for step in attributes['steps']:
         if step['stepid'] == self.stepid:
            self._update(step)
            return
      raise Exception('Step with id %s not found in guide %s.' \
                      % (self.stepid, self.guideid))
   
   def _update(self, data):
      '''
      Update the step using the blob of json-parsed data directly from the API.
      '''
      self.orderby = data['orderby']
      self.revision = data['revisionid']
      self.title = data['title']
      self.lines = [Line(self.guideid, self.stepid, line['lineid'], data=line)
                    for line in data['lines']]

