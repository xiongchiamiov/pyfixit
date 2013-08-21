# -*- coding: utf-8 -*-
import requests

from base import Base
from constants import API_BASE_URL
from wikitext import WikiText

class Line(Base):
   '''One line of text in a step.
   
   :var int guideid: The id of the :class:`pyfixit.guide.Guide` owning this
                     step. Ex: ``5``.
   :var int stepid: The id of the :class:`pyfixit.step.Step` owning this step.
                    Ex: ``14``.
   :var int lineid: This line's id. Ex: ``23``.
   :var string bullet: The color or type of the step's bullet. Ex: ``black``.
   :var int level: The number of levels in this step is indented. Ex: ``0``.
   :var string text: A :class:`pyfixit.wikitext.WikiText` of the step's text.
   '''
   def __init__(self, guideid, stepid, lineid, data=None):
      self.guideid = guideid
      self.stepid = stepid
      self.lineid = lineid
      
      # Usually we're going to have a blob of data, since a GET of a guide
      # includes all the data of its steps, and their lines.
      if data:
         self._update(data)
      
   def refresh(self):
      '''Refetch instance data from the API.
      '''
      # There's no GET endpoint for steps, so get the parent guide and loop
      # through its steps until we find the right one.
      response = requests.get('%s/guides/%s' % (API_BASE_URL, self.guideid))
      attributes = response.json()
      
      for step in attributes['steps']:
         if step['stepid'] == self.stepid:
            for line in step['lines']:
               if line['lineid'] == self.lineid:
                  self._update(line)
                  return
      raise Exception('Line with id %s not found in step %s in guide %s.' \
                      % (self.lineid, self.stepid, self.guideid))
   
   def _update(self, data):
      '''Update the line using the blob of json-parsed data directly from the
      API.
      '''
      self.bullet = data['bullet']
      self.level = data['level']
      self.text = WikiText(data['text_raw'],
                           data['text_rendered'])

