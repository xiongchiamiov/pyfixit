# -*- coding: utf-8 -*-

class WikiText(object):
   """A bit of marked-up text.
   
   :var string raw: The text including markup. Ex: ``'''bold'''``.
   :var string rendered: The rendered text. Ex: ``<strong>bold</strong>``.
   """
   def __init__(self, raw, rendered):
      self.raw = raw
      self.rendered = rendered
   
   def __str__(self):
      return self.raw
   
   def __repr__(self):
      return '<WikiText: %s>' % self.raw

