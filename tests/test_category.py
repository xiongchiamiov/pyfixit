# -*- coding: utf-8 -*-
from unittest import TestCase

from category import Category

class CategoryTest(TestCase):
   @classmethod
   def setUpClass(cls):
      cls.wallstreet = Category('PowerBook G3 Wallstreet')
   
   def test_name(self):
      self.assertEqual('PowerBook G3 Wallstreet', self.wallstreet.name)
   
   def test_categories(self):
      categories = [Category('PowerBook G3 Series')]
      
      # We don't care about deep equality, so let's just check the length and
      # the names of the categories.
      self.assertEqual(len(categories), len(self.wallstreet.categories))
      for (c1, c2) in zip(categories, self.wallstreet.categories):
         self.assertEqual(c1.name, c2.name)
   
   def test_description(self):
      self.assertEqual(
         'Model M4753 / 233, 250, 266, 292, or 300 MHz G3 processor',
         self.wallstreet.description)
   
   def test_locale(self):
      self.assertEqual('en', self.wallstreet.locale)
   
   def test_title(self):
      self.assertEqual('PowerBook G3 Wallstreet Repair', self.wallstreet.title)

