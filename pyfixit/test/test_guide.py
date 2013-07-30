# -*- coding: utf-8 -*-
from datetime import datetime
from unittest import TestCase

from pyfixit import Guide
from pyfixit import Image
from pyfixit import Step

class GuideTest(TestCase):
   @classmethod
   def setUpClass(cls):
      cls.wallstreet = Guide(5)
   
   def test_category(self):
      self.assertEqual('PowerBook G3 Wallstreet', self.wallstreet.category.name)
   
   def test_url(self):
      self.assertEqual(
         'http://www.ifixit.com/Guide/Installing+PowerBook+G3+Wallstreet+Processor/5/1',
         self.wallstreet.url)
   
   def test_title(self):
      self.assertEqual(
         'Installing PowerBook G3 Wallstreet Processor',
         self.wallstreet.title)
   
   def test_image(self):
      self.assertEqual(Image(14), self.wallstreet.image)
      # Guides without main images tend to get deleted or image-ified quickly,
      # so it's hard to have a working test.
      #self.assertEqual(Guide(14729).image, None)
   
   def test_locale(self):
      self.assertEqual('en', self.wallstreet.locale)
   
   def test_subject(self):
      self.assertEqual('Processor', self.wallstreet.subject)
   
   def test_created_date(self):
      self.assertEqual(
         datetime(2009, 06, 04, 06, 52, 12),
         self.wallstreet.createdDate)
   
   def test_published_date(self):
      self.assertEqual(
         datetime(2009, 06, 04, 06, 52, 12),
         self.wallstreet.publishedDate)
   
   def test_steps(self):
      steps = [
         Step(1, 1),
         Step(1, 2),
         Step(1, 3),
         Step(1, 4),
         Step(1, 5),
         Step(1, 6),
         Step(2, 7),
         Step(2, 8),
         Step(3, 9),
         Step(3, 10),
         Step(3, 11),
         Step(5, 14),
      ]
      # We test for deep equality in StepTest.
      self.assertEqual(len(steps), len(self.wallstreet.steps))
      for (s1, s2) in zip(steps, self.wallstreet.steps):
         self.assertEqual(s1.guideid, s2.guideid)
         self.assertEqual(s1.stepid, s2.stepid)
   
   def test_type(self):
      self.assertEqual('installation', self.wallstreet.type)
   
   def test_public(self):
      self.assertEqual(True, self.wallstreet.public)
   
   def test_revision(self):
      self.assertEqual(42928, self.wallstreet.revision)
   
   def test_difficulty(self):
      self.assertEqual('Easy', self.wallstreet.difficulty)

