# -*- coding: utf-8 -*-
import requests

from base import Base
from constants import API_BASE_URL
from flag import Flag
from image import Image
from wikitext import WikiText
# See also imports at the bottom of the file.

class Category(Base):
   '''A category of guides, answers, wiki pages, etc.  Often takes the form of
   a device.
   
   :var string name: The identifying name of the category. Ex: ``Powerbook G3
                     Wallstreet``.
   :var iterable ancestors: *(Lazy)* An ordered list of
                            :class:`pyfixit.category.Category` objects. The
                            first is this category's parent, followed by its
                            grandparent, up until the root category.
   :var WikiText contents: *(Lazy)* A :class:`pyfixit.wikitext.WikiText` of
                           the text describing this category.
   :var iterable guides: *(Lazy)* An iterable of the
                         :class:`pyfixit.guide.Guide` objects under this
                         category.
   :var string description: *(Lazy)* A short description of the category.
   :var iterable flags: *(Lazy)* A list of :class:`pyfixit.flag.Flag` objects,
                        each containing an informational note about the
                        category.
   :var Image image: *(Lazy)* The primary :class:`pyfixit.image.Image`
                     associated with the category.
   :var string locale: *(Lazy)* The locale of the text throughout the category.
   :var string title: *(Lazy)* The display title (which is alterable, unlike
                      the identifying name).
   '''
   def __init__(self, name):
      self.name = name
   
   def __str__(self):
      return self.name
   
   def __repr__(self):
      return '<Category %s>' % self.name
   
   def refresh(self):
      '''Refetch instance data from the API.
      '''
      response = requests.get('%s/categories/%s' % (API_BASE_URL, self.name))
      attributes = response.json()
      
      self.ancestors = [Category(name) for name in attributes['ancestors']]
      self.contents = WikiText(attributes['contents_raw'],
                               attributes['contents_rendered'])
      self.description = attributes['description']
      self.guides = []
      for guide in attributes['guides']:
         self.guides.append(Guide(guide['guideid']))
      # Unlike guides, categories return flags as a dict, keyed by flagid.
      # *Except* when it's empty, in which case we get an empty list due to
      # PHP's json_encode() not knowing the difference between an empty array
      # and an empty dict.
      flags = dict(attributes['flags']).values()
      self.flags = [Flag.from_id(flag['flagid']) for flag in flags]
      self.image = Image(attributes['image']['id'])
      self.locale = attributes['locale']
      #self.parts = attributes['parts']
      #self.solutions = attributes['solutions']
      self.title = attributes['display_title']
      #self.tools = attributes['tools']
      #self.topic_info = attributes['topic_info']

# Circular imports don't work with 'from foo import bar' syntax,
# http://stackoverflow.com/a/746067/120999
# but if we move this import down below the class definition, all is good.
from guide import Guide

