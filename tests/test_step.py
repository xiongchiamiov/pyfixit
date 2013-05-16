# -*- coding: utf-8 -*-
from unittest import TestCase

from step import Step

class StepTest(TestCase):
   @classmethod
   def setUpClass(cls):
      cls.fetched = Step(5, 14)
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
   
   def test_orderby(self):
      self.assertEqual(1, self.fetched.orderby)
      self.assertEqual(1, self.fed.orderby)
   
   def test_revision(self):
      self.assertEqual(33880, self.fetched.revision)
      self.assertEqual(33880, self.fed.revision)
   
   def test_title(self):
      self.assertEqual('', self.fetched.title)
      self.assertEqual('', self.fed.title)

