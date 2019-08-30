
from re import match
from unittest import TestCase

from pyfixit2 import Image
from pyfixit2 import Line
from pyfixit2 import Step

class StepTest(TestCase):
   @classmethod
   def setUpClass(cls):
      cls.fetched = Step(5, 14)
      cls.fetchedWrong = Step(1, 14)
      data = {
         "guideid": 5,
         "lines": [
            {
               "bullet": "black",
               "level": 0,
               "lineid": 23,
               "text_raw": "Use a spudger, the tips of your fingers, or a flat non-metal tool to pry up the processor's right side.",
               "text_rendered": "Use a spudger, the tips of your fingers, or a flat non-metal tool to pry up the processor's right side."
            },
            {
               "bullet": "black",
               "level": 0,
               "lineid": 24,
               "text_raw": "Remove the processor by sliding it up and to the right.",
               "text_rendered": "Remove the processor by sliding it up and to the right."
            },
            {
               "bullet": "icon_note",
               "level": 0,
               "lineid": 25,
               "text_raw": "The processor and RAM can be removed as a unit. It is not necessary to remove the RAM from the processor.",
               "text_rendered": "The processor and RAM can be removed as a unit. It is not necessary to remove the RAM from the processor."
            },
            {
               "bullet": "icon_reminder",
               "level": 0,
               "lineid": 26,
               "text_raw": "There are two tabs on the left side of the processor that fit into slots on the metal framework. Make sure these tabs are in the slots.",
               "text_rendered": "There are two tabs on the left side of the processor that fit into slots on the metal framework. Make sure these tabs are in the slots."
            }
         ],
         "media": {
         "data": [
            {
               "id": 14,
               "large": "https://d3nevzfk7ii3be.cloudfront.net/igi/whhqVo1IJxLAghCg.large",
               "medium": "https://d3nevzfk7ii3be.cloudfront.net/igi/whhqVo1IJxLAghCg.medium",
               "mini": "https://d3nevzfk7ii3be.cloudfront.net/igi/whhqVo1IJxLAghCg.mini",
               "original": "https://d3nevzfk7ii3be.cloudfront.net/igi/whhqVo1IJxLAghCg",
               "standard": "https://d3nevzfk7ii3be.cloudfront.net/igi/whhqVo1IJxLAghCg.standard",
               "thumbnail": "https://d3nevzfk7ii3be.cloudfront.net/igi/whhqVo1IJxLAghCg.thumbnail"
            }
         ],
         "type": "image"
         },
         "orderby": 1,
         "revisionid": 33880,
         "stepid": 14,
         "title": ""
      }
      cls.fed = Step(5, 14, data)
      cls.fedWrong = Step(1, 14, data)
   
   def test_fetching(self):
      # assertRaisesRegexp was introduced in 2.7/3.1, and renamed in 3.2.  I'd
      # like to support at least 2.6, though, so let's do it manually.
      with self.assertRaises(Exception) as contextManager:
         self.fetchedWrong.notAnAttribute
      self.assertTrue(match(r'Step with id \d+ not found in guide \d+.',
                            contextManager.exception.message))
      with self.assertRaises(Exception) as contextManager:
         self.fedWrong.notAnAttribute
      self.assertTrue(match(r'Step with id \d+ not found in guide \d+.',
                            contextManager.exception.message))
   
   def test_orderby(self):
      self.assertEqual(1, self.fetched.orderby)
      self.assertEqual(1, self.fed.orderby)
   
   def test_revision(self):
      self.assertEqual(33880, self.fetched.revision)
      self.assertEqual(33880, self.fed.revision)
   
   def test_title(self):
      self.assertEqual('', self.fetched.title)
      self.assertEqual('', self.fed.title)
   
   def test_lines(self):
      lines = [
         Line(5, 14, 23),
         Line(5, 14, 24),
         Line(5, 14, 25),
         Line(5, 14, 26),
      ]
      # We test for deep equality in LineTest.
      self.assertEqual(len(lines), len(self.fetched.lines))
      self.assertEqual(len(lines), len(self.fed.lines))
      for (l1, l2) in list(zip(lines, self.fetched.lines)) \
                    + list(zip(lines, self.fed.lines)):
         self.assertEqual(l1.guideid, l2.guideid)
         self.assertEqual(l1.stepid, l2.stepid)
         self.assertEqual(l1.lineid, l2.lineid)

   def test_media(self):
      # TODO: Test a step with multiple images.
      self.assertEqual([Image(14)], self.fetched.media)
      self.assertEqual([Image(14)], self.fed.media)
   
