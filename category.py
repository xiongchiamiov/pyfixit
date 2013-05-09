# -*- coding: utf-8 -*-

class Category(object):
   def __init__(self, name):
      self.name = name
   
   def __str__(self):
      return self.name
   
   def __repr__(self):
      return '<Category %s>' % self.name

