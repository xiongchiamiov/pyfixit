# -*- coding: utf-8 -*-
from unittest import TestCase

from line import Line

class LineTest(TestCase):
   @classmethod
   def setUpClass(cls):
      cls.fetched = Line(5, 14, 23)
      cls.fetchedWrong = Line(5, 11, 23)
      data = {
         "bullet": "black",
         "level": 0,
         "lineid": 23,
         "text_raw": "Use a spudger, the tips of your fingers, or a flat non-metal tool to pry up the processor's right side.",
         "text_rendered": "Use a spudger, the tips of your fingers, or a flat non-metal tool to pry up the processor's right side."
      }
      cls.fed = Line(5, 14, 23, data)
      cls.fedWrong = Line(5, 11, 23, data)
   
   def test_bullet(self):
      self.assertEqual('black', self.fetched.bullet)
      self.assertEqual('black', self.fed.bullet)
   
   def test_level(self):
      self.assertEqual(0, self.fetched.level)
      self.assertEqual(0, self.fed.level)
   
   def test_text(self):
      pass

