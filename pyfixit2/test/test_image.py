
from unittest import TestCase

from pyfixit2 import Image

class ImageTest(TestCase):
   @classmethod
   def setUpClass(cls):
      cls.stack = Image(26674)
      cls.baseImage = 'https://d3nevzfk7ii3be.cloudfront.net/igi/5SKtbIbC2dYyZdbv'
   
   def test_id(self):
      self.assertEqual(26674, self.stack.id)
   
   def test_height(self):
      self.assertEqual(1200, self.stack.height)
   
   def test_width(self):
      self.assertEqual(1600, self.stack.width)
   
   def test_original(self):
      self.assertEqual(self.baseImage, self.stack.original)
   
   def test_mini(self):
      self.assertEqual(self.baseImage + '.mini', self.stack.mini)
   
   def test_thumbnail(self):
      self.assertEqual(self.baseImage + '.thumbnail', self.stack.thumbnail)
   
   def test_standard(self):
      self.assertEqual(self.baseImage + '.standard', self.stack.standard)
   
   def test_medium(self):
      self.assertEqual(self.baseImage + '.medium', self.stack.medium)
   
   def test_large(self):
      self.assertEqual(self.baseImage + '.large', self.stack.large)
   
   def test_huge(self):
      self.assertEqual(self.baseImage + '.huge', self.stack.huge)
      noHuge = Image(74895)
      with self.assertRaises(AttributeError):
         noHuge.huge
   
