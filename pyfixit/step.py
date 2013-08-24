# -*- coding: utf-8 -*-
import requests

from base import Base
from constants import API_BASE_URL
from image import Image
from line import Line

class Step(Base):
   '''One step in a guide.
   
   :var int guideid: The id of the :class:`pyfixit.guide.Guide` owning this
                     step. Ex: ``5``.
   :var int stepid: This step's id. Ex: ``14``.
   :var int orderby: This step's location in its guide relative to the other
                     steps. Lower numbers come first. Counting starts at 0 and
                     should not duplicate or skip over any natural numbers. Ex:
                     ``0``.
   :var int revision: The revisionid associated with this version of the step
                      in the database, suitable for determining equality of
                      objects not modified after being pulled from the API. Ex:
                      ``33880``.
   :var string title: The title of this step. May be an empty string.
   :var iterable lines: An iterable of the :class:`pyfixit.line.Line` objects
                        composing this step.
   :var iterable media: *(Optional)* A list of :class:`pyfixit.image.Image`
                        objects illustrating the step.
   '''
   def __init__(self, guideid, stepid, data=None):
      self.guideid = guideid
      self.stepid = stepid
      
      # Usually we're going to have a blob of data, since a GET of a guide
      # includes all the data of its steps.
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
            self._update(step)
            return
      raise Exception('Step with id %s not found in guide %s.' \
                      % (self.stepid, self.guideid))
   
   def _update(self, data):
      '''Update the step using the blob of json-parsed data directly from the
      API.
      '''
      self.orderby = data['orderby']
      self.revision = data['revisionid']
      self.title = data['title']
      self.lines = [Line(self.guideid, self.stepid, line['lineid'], data=line)
                    for line in data['lines']]
      # TODO: Support video.
      if data['media']['type'] == 'image':
         self.media = []
         for image in data['media']['data']:
            self.media.append(Image(image['id']))

