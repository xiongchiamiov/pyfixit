# -*- coding: utf-8 -*-
from unittest import TestCase

from pyfixit import Category
from pyfixit import Guide
from pyfixit import Image
from pyfixit import flag

class CategoryTest(TestCase):
   @classmethod
   def setUpClass(cls):
      cls.wallstreet = Category('PowerBook G3 Wallstreet')
   
   def test_name(self):
      self.assertEqual('PowerBook G3 Wallstreet', self.wallstreet.name)
   
   def test_ancestors(self):
      ancestors = [
         Category('PowerBook G3 Series'),
         Category('PowerBook'),
         Category('Mac Laptop'),
         Category('Mac'),
         Category('Root')
      ]
      
      # We don't care about deep equality, so let's just check the length and
      # the names of the categories.
      self.assertEqual(len(ancestors), len(self.wallstreet.ancestors))
      for (c1, c2) in zip(ancestors, self.wallstreet.ancestors):
         self.assertEqual(c1.name, c2.name)
   
   def test_contents(self):
      self.assertEqual("""
[title|PowerBook G3 Wallstreet Repair]\n\n[summary]Model M4753 / 233, 250, 266, 292, or 300 MHz G3 processor[/summary]\n\n[summary_image|10301]\n\n[info | device\n|introduced_date = 05/06/1998\n]\n\n== Troubleshooting ==\n\nTrack down a number of hardware problems using the [[PowerBook G3 Wallstreet Troubleshooting|PowerBook G3 Wallstreet troubleshooting guide]].\n\n== Upgrades ==\n\nThere are a number of components in the PowerBook G3 Wallstreet that can be cost effectively upgraded.\n\n* '''Memory:''' The Wallstreet has two RAM slots. You can place a 256 MB chip in each one for half gigabyte of memory. Browse our Wallstreet [link|/Mac-Parts/PowerBook-G3-Wallstreet#0-RAM|RAM] selection for a chip that suits your need for speed. You must use a low profile chip in the lower slot, but the upper slot can be whatever you choose. Don't forget to install it using our free iFixit [guide|6|PowerBook G3 Wallstreet RAM installation instructions].\n* '''Hard Drive:''' With our tools and instructions, you can [guide|4|install] your new hard drive yourself!\n* '''Optical Drive:''' Wallstreets are not inherently able to play DVDs. They require a special DVD decoder that fits into the PC card slot. Even if you have the decoder, you can only watch DVDs in OS 9. It will not work in OS X or classic because Apple never developed the hardware for it.\n\n== Identification and Background ==\n\nThe new PowerBooks came in three screen sizes; a 12\", 13.3\", and 14.1\". It also came at three CPU speeds; 233MHz, 250MHz, and 292MHz.\n\nUse the [link|/info/ID-your-Mac|laptop identification system] to help you identify your machine. PowerBooks tend to look very similar, and it's important to know which machine you have before ordering any replacement parts.\n\n== Additional Information ==\n\n* [[Troubleshoot|iFixit: List of Troubleshooting Guides]]\n* [[DIY Laptop Upgrades|iFixit: DIY Laptop Upgrades]]\n* [http://en.wikipedia.org/wiki/PowerBook|Wikipedia: PowerBook]\n* [http://mactracker.dreamhosters.com/|Mactracker: Application with Apple Product Specs]\n* [http://www.everymac.com/|EveryMac: Online Apple Product Specs]
         """.strip(),
         str(self.wallstreet.contents))
   
   def test_description(self):
      self.assertEqual(
         'Model M4753 / 233, 250, 266, 292, or 300 MHz G3 processor',
         self.wallstreet.description)
   
   def test_guides(self):
      guides = [
         Guide(9),
         Guide(4),
         Guide(2),
         Guide(5),
         Guide(6),
         Guide(8),
         Guide(14),
         Guide(15),
         Guide(1),
         Guide(16),
         Guide(7),
         Guide(17),
         Guide(12),
         Guide(13),
         Guide(11),
         Guide(10),
      ]
      
      # We don't care about deep equality, so let's just check the length and
      # the ids of the guides.
      self.assertEqual(len(guides), len(self.wallstreet.guides))
      for (c1, c2) in zip(guides, self.wallstreet.guides):
         self.assertEqual(c1.id, c2.id)

   def test_flags(self):
      # This category should have multiple flags for a long time to come.
      category = Category('Epson_Stylus_C84')
      flags = [
         flag.WIKI_NO_AREA,
         flag.WIKI_NO_IMAGE,
         flag.WIKI_NO_SUMMARY,
         flag.WIKI_STUB,
      ]
      
      self.assertEqual(len(flags), len(category.flags))
      for (f1, f2) in zip(sorted(flags), sorted(category.flags)):
         self.assertEqual(f1, f2)
   
   def test_image(self):
      self.assertEqual(Image(10301), self.wallstreet.image)
   
   def test_locale(self):
      self.assertEqual('en', self.wallstreet.locale)
   
   def test_title(self):
      self.assertEqual('PowerBook G3 Wallstreet Repair', self.wallstreet.title)

