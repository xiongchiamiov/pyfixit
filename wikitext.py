# -*- coding: utf-8 -*-

class WikiText(object):
   def __init__(self, raw, rendered):
      self.raw = raw
      self.rendered = rendered
   
   def __str__(self):
      return self.raw
   
   def __repr__(self):
      return '<WikiText: %s>' % self.raw

