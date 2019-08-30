
from datetime import datetime
from unittest import TestCase

from pyfixit2 import Guide
from pyfixit2 import Image
from pyfixit2 import Step
from pyfixit2 import flag

class GuideTest(TestCase):
   @classmethod
   def setUpClass(cls):
      cls.wallstreet = Guide(5)
   
   def test_category(self):
      self.assertEqual('PowerBook G3 Wallstreet', self.wallstreet.category.name)
   
   def test_url(self):
      self.assertEqual(
         'http://www.ifixit.com/Guide/Replacing+PowerBook+G3+Wallstreet+Processor/5/1',
         self.wallstreet.url)
   
   def test_title(self):
      self.assertEqual(
         'Replacing PowerBook G3 Wallstreet Processor',
         self.wallstreet.title)
   
   def test_image(self):
      self.assertEqual(Image(14), self.wallstreet.image)
      # Guides without main images tend to get deleted or image-ified quickly,
      # so it's hard to have a working test.
      #self.assertEqual(Guide(14729).image, None)
   
   def test_locale(self):
      self.assertEqual('en', self.wallstreet.locale)
   
   def test_introduction(self):
      self.assertEqual(
         "The G3 processor is not soldered to the logic board, and installing a replacement is very easy.",
         str(self.wallstreet.introduction))
   
   def test_conclusion(self):
      self.assertEqual(
         "To reassemble your device, follow these instructions in reverse order.",
         str(self.wallstreet.conclusion))
   
   def test_subject(self):
      self.assertEqual('', self.wallstreet.subject)
   
   def test_modified_date(self):
      self.assertEqual(
         datetime(2013, 8, 22, 22, 49, 39),
         self.wallstreet.modifiedDate)
   
   def test_created_date(self):
      self.assertEqual(
         datetime(2009, 0o6, 0o4, 0o6, 52, 12),
         self.wallstreet.createdDate)
   
   def test_published_date(self):
      self.assertEqual(
         datetime(2009, 0o6, 0o4, 0o6, 52, 12),
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
      self.assertEqual('replacement', self.wallstreet.type)
   
   def test_public(self):
      self.assertEqual(True, self.wallstreet.public)
   
   def test_revision(self):
      self.assertEqual(173550, self.wallstreet.revision)
   
   def test_difficulty(self):
      self.assertEqual('Easy', self.wallstreet.difficulty)
   
   def test_prerequisites(self):
      guides = [
         Guide(1),
         Guide(2),
         Guide(3),
      ]
      
      # We don't care about deep equality, so let's just check the length and
      # the ids of the guides.
      self.assertEqual(len(guides), len(self.wallstreet.prerequisites))
      for (g1, g2) in zip(guides, self.wallstreet.prerequisites):
         self.assertEqual(g1.id, g2.id)
   
   def test_flags(self):
      # This guide should have multiple flags for a long time to come.
      guide = Guide(6060)
      flags = [
         flag.GUIDE_GRAMMAR_ERRORS,
         flag.GUIDE_LOUSY_PICTURES,
         flag.GUIDE_USER_CONTRIBUTED,
      ]
      
      self.assertEqual(len(flags), len(guide.flags))
      for (f1, f2) in zip(flags, guide.flags):
         self.assertEqual(f1, f2)

