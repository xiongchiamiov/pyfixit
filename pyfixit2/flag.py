

class Flag(object):
   """A way of identifying a common bit of information about a guide or wiki.
   
   You almost certainly want to use :func:`from_id` instead of this
   constructor.
   
   :var string title: The title of the flag. Ex: ``Grammar Police``.
   :var string text: The text describing the flag. Ex: ``Embrace your inner
                     English teacher and help improve this guide's grammar!``.
   """
   def __init__(self, title, text):
      self.title = title
      self.text = text
   
   @staticmethod
   def from_id(id):
      """Fetch a pre-created singleton flag.

      :var string id: The flag's id, as seen on
                      http://www.ifixit.com/Info/Flags.
      """
      return globals()[id]
   
   def __str__(self):
      return self.title
   
   def __repr__(self):
      return '<Flag: %s>' % self.title

# Guide Flags

GUIDE_IN_PROGRESS = Flag(
   'In Progress',
   'This guide is a work in progress. Reload periodically to see the latest changes!'
)

GUIDE_USER_CONTRIBUTED = Flag(
   'User-Contributed Guide',
   'An awesome member of our community made this guide. It is not managed by iFixit staff.'
)

GUIDE_STARRED = Flag(
   'Featured Guide',
   'This guide has been found to be exceptionally cool by the iFixit staff.'
)

GUIDE_FEATURED_STUDENT = Flag(
   'Featured Student Guide',
   'This guide has been the hard work of our awesome students and is found to be exceptionally cool by the iFixit staff.'
)

GUIDE_MISSING_STEPS = Flag(
   'Missed a Step',
   "Oops! This guide is currently missing some important steps."
)

GUIDE_MISSING_IMAGES = Flag(
   'Needs More Images',
   "A few more images would make this guide's procedures crystal clear."
)

GUIDE_GRAMMAR_ERRORS = Flag(
   'Grammar Police',
   "Embrace your inner English teacher and help improve this guide's grammar!"
)

GUIDE_LOUSY_PICTURES = Flag(
   'Needs Better Images',
   "Better photos will improve this guide. Help out by taking, editing, or uploading new ones!"
)

GUIDE_MARKUP_PROBLEMS = Flag(
   'Markup Mishap',
   "This guide needs better markups. Help out by correcting or making some markup annotations."
)

GUIDE_INCORRECT_BULLETS = Flag(
   'Bullets!',
   "Better coordination with markups and the color/type of bullets will help make this guide more clear!"
)

GUIDE_UNNECESSARY_STEPS = Flag(
   'Step Trimmer',
   "This guide has unnecessary steps. Trim them to be more concise!"
)

GUIDE_MISSING_PREREQUISITES = Flag(
   'Missing Prerequisites',
   "This guide is missing information on how to start the process. Make a prerequisite guide!"
)

GUIDE_INCORRECT_PREREQUISITES = Flag(
   'Mismatched Prerequisites',
   "This guide does not have a proper prerequisite guide. Help match it to its ideal partner by finding it or writing one!"
)

GUIDE_INCONSISTENT_IMAGES = Flag(
   'Inconsistent Images',
   "Updating the images on this guide to be more consistent with the prerequisites would increase its awesomeness."
)

GUIDE_INCORRECT_TEXT = Flag(
   'Confusing Text',
   "Some of this guide's text is confusing, duplicated, or off-topic. Clarify it by editing!"
)

GUIDE_INCORRECT_TOOLS = Flag(
   'Incorrect Tools',
   "Help make this guide better by using the correct tools in images and/or text."
)

GUIDE_IMPROPER_ACTION = Flag(
   'Action Shots',
   "Be an action hero! This guide needs images that better demonstrate how to perform specific actions."
)

GUIDE_PREREQ_ONLY = Flag(
   'Prerequisite Only',
   "Please note that this guide is only a prerequisite for other guides."
)

GUIDE_DELETE = Flag(
   'Request Guide Deletion',
   "This guide will be reviewed by admins for deletion."
)

STUDENT_OWNED = Flag(
   'Student Guide',
   "This guide is being worked on by hardworking students."
)

INTRODUCTION_ISSUES = Flag(
   'Better Introduction',
   "Improve this guide by completing or revising its introduction."
)

GUIDE_SPLIT_PREREQ = Flag(
   'Slice and Dice',
   "The steps in this guide should be split up and made into a series of prerequisite guides."
)

GUIDE_PATAGONIA = Flag(
   'Patagonia Sponsored',
   "Patagonia and iFixit are collaborating to provide guides for Patagonia's most popular apparel repairs."
)

GUIDE_ARCHIVED = Flag(
   'Archived Guide',
   "This guide is retained solely for historical purposes. Use the updated version of the guide to perform your repair."
)

DANGER = Flag(
   'Potentially Dangerous',
   "Injury may result if this procedure is not followed properly. Use caution and follow all warnings."
)

GUIDE_INCORRECT_PROCEDURE = Flag(
   'Scenic Route',
   "This guide's procedure isn't the most efficient way to get the job done, but still may be useful in some circumstances."
)

# Wiki Flags

WIKI_PRIVATE = Flag(
   'Unpublished',
   "This wiki will not appear in search results, but can still be viewed by anyone!"
)

WIKI_IN_PROGRESS = Flag(
   'In Progress',
   "This wiki is unfinished."
)

WIKI_STUB = Flag(
   'Stub',
   "This page is a stub. Help make iFixit better by adding information to it!"
)

WIKI_DEVICE_STUB = Flag(
   'Device Stub',
   "This device wiki is a stub. Help iFixit by adding information to it!"
)

WIKI_DEVICE_INCOMPLETE = Flag(
   'Incomplete Repair Manual',
   "This device repair manual is incomplete. Help iFixit by adding more information about the device and step-by-step repair guides!"
)

WIKI_STUB = Flag(
   'Page Stub',
   "This wiki page is a stub. Help iFixit by adding information to it!"
)

WIKI_DOCS_NEEDED = Flag(
   'Documentation Needed',
   "This stub helps to identify areas that haven't been well documented. Help iFixit by finding poorly documented areas and identifying them with this stub!"
)

WIKI_NO_SUMMARY = Flag(
   'No Summary',
   "This wiki does not have a summary. Help iFixit by writing one!"
)

WIKI_NO_IMAGE = Flag(
   'No Image',
   "This wiki is missing a device image. Help iFixit by uploading one!"
)

WIKI_NO_AREA = Flag(
   'No Category',
   "This page hasn't yet been categorized. Our admins will be around to organize this content soon!"
)

WIKI_IMPROPER_FORMATTING = Flag(
   'Improper Formatting',
   "This wiki does not meet iFixit's formatting guidelines."
)

WIKI_INCORRECT_TEXT = Flag(
   'Incorrect Text',
   "This wiki has information which is deemed incorrect, misleading, or unclear."
)

WIKI_GRAMMAR_ERRORS = Flag(
   'Grammatical Errors',
   "This wiki has grammatical errors or does not meet iFixit's writing guidelines."
)

WIKI_BAD_IMAGE = Flag(
   'Unsatisfactory Image',
   "This wiki has a low-quality photo. Please help iFixit by either re-editing or re-taking the photo!"
)

WIKI_DUPLICATE_DEVICE = Flag(
   'Duplicate Device',
   "This device page is a duplicate with another device. Please merge this content into the canonical device."
)

WIKI_DELETE = Flag(
   'Request Page Deletion',
   "This page is being considered by moderators for deletion."
)

WIKI_STUDENT_OWNED = Flag(
   'Student Wiki',
   "This wiki is being worked on by students."
)

WIKI_TEACHER_OWNED = Flag(
   'Teacher Wiki',
   "This wiki should only be edited by teachers."
)

WIKI_MIRO_OWNED = Flag(
   'Unbelievably Awesome',
   "Miro's profile is so awesome it may blow your mind."
)

WIKI_DONATE_DEVICE = Flag(
   'Donate Device',
   "iFixit kindly requests this device to be donated for the technical writing project."
)

WIKI_DICTIONARY = Flag(
   'Business Dictionary',
   "This wiki helps define a term used in the Repair Business Toolkit."
)

