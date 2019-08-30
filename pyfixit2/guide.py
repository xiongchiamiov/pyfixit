
import requests
from datetime import datetime

from .base import Base
from .category import Category
from .constants import API_BASE_URL
from .flag import Flag
from .image import Image
from .step import Step
from .wikitext import WikiText

class Guide(Base):
   '''A series of instructions for performing a task.
   
   :var int id: The identifying id for the guide. Ex: ``5``.
   :var Category category: *(Lazy)* The :class:`pyfixit.category.Category` to
                           which this guide belongs.
   :var string url: *(Lazy)* The canonical URL for viewing this guide.
   :var string title: *(Lazy)* The display title of the guide.
   :var Image image: *(Lazy)* The primary :class:`pyfixit.image.Image`
                     associated with the guide.
   :var string locale: *(Lazy)* The locale of the text displayed through the
                       guide.
   :var WikiText introduction: *(Lazy)* A :class:`pyfixit.wikitext.WikiText` of
                               the introductory text on the guide.
   :var WikiText conclusion: *(Lazy)* A :class:`pyfixit.wikitext.WikiText` of
                               the concluding text on the guide.
   :var string subject: *(Lazy)* The thing the guide's user is operating on.
                        Ex: ``Processor``.
   :var datetime modifiedDate: *(Lazy)* When the guide was last modified (UTC).
   :var datetime createdDate: *(Lazy)* When the guide was created (UTC).
   :var datetime publishedDate: *(Lazy)* When the guide was first made
                                publicly-viewable (UTC).
   :var iterable steps: *(Lazy)* An ordered list of :class:`pyfixit.step.Step`
                        objects representing the steps to follow.
   :var string type: *(Lazy)* The sort of guide. Ex: ``installation``.
   :var boolean public: *(Lazy)* Whether everyone can view the guide. If a
                        guide is not public, only the author and administrative
                        users can view it.
   :var int revision: *(Lazy)* The revisionid associated with this version of
                      the step in the database, suitable for determining
                      equality of objects not modified after being pulled from
                      the API. Ex: ``42928``.
   :var string difficulty: *(Lazy)* An estimate of the difficulty of the guide.
                           Choices: Very easy, Easy, Moderate, Difficult, Very
                           difficult.
   :var iterable prerequisites: *(Lazy)* A collection of guides that must be
                                completed prior to starting this guide.
   :var iterable flags: *(Lazy)* A list of :class:`pyfixit.flag.Flag` objects,
                        each containing an informational note about the guide.
   '''
   def __init__(self, guideid):
      self.id = guideid
   
   def refresh(self):
      '''Refetch instance data from the API.
      '''
      response = requests.get('%s/guides/%s' % (API_BASE_URL, self.id))
      attributes = response.json()
      
      self.category = Category(attributes['category'])
      self.url = attributes['url']
      
      self.title = attributes['title']
      if attributes['image']:
         self.image = Image(attributes['image']['id'])
      else:
         self.image = None
      self.locale = attributes['locale']
      self.introduction = WikiText(attributes['introduction_raw'],
                                   attributes['introduction_rendered'])
      self.conclusion = WikiText(attributes['conclusion_raw'],
                                 attributes['conclusion_rendered'])
      #self.tools = attributes['tools']
      #self.parts = attributes['parts']
      self.subject = attributes['subject']
      self.modifiedDate = datetime.utcfromtimestamp(attributes['modified_date'])
      self.createdDate = datetime.utcfromtimestamp(attributes['created_date'])
      self.publishedDate = datetime.utcfromtimestamp(attributes['published_date'])
      #self.documents = attributes['documents']
      author = attributes['author']
      #self.author = User(author['userid'], name=author['text'])
      #self.timeRequired = attributes['timeRequired']
      self.steps = [Step(step['guideid'], step['stepid'], data=step) for step in attributes['steps']]
      self.type = attributes['type']
      self.public = attributes['public']
      self.revision = attributes['revisionid']
      self.difficulty = attributes['difficulty']
      self.prerequisites = [Guide(guide['guideid']) for guide in attributes['prerequisites']]
      #                     attributes['prereq_modified_date']
      #self.summary = attributes['summary']
      self.flags = [Flag.from_id(flag['flagid']) for flag in attributes['flags']]

   @staticmethod
   def all(guideids=None, filter=None, order=None):
      '''
      Fetch all guides.
      
      :param iterable guideids: Only return Guides corresponding to these ids.
      :param string filter: Only return guides of this type.  Choices:
                            installation, repair, disassembly, teardown,
                            technique, maintenance.
      :param string order: Instead of ordering by guideid, order alphabetically.
                           Choices: ASC, DESC.
      :rtype: generator of :class:`pyfixit.guide.Guide` objects.
      '''
      parameters = []
      if guideids:
         parameters.append('guideids=%s' % ','.join(map(str, guideids)))
      if filter:
         parameters.append('filter=%s' % filter)
      if order:
         parameters.append('order=%s' % order)
      parameters = '&'.join(parameters)
      
      offset = 0
      limit = 5 # Tune this to balance memory vs. frequent network trips.
      guideJSONs = []
      while True:
         if not guideJSONs:
            url = '%s/guides?offset=%s&limit=%s&%s' \
                  % (API_BASE_URL, offset, limit, parameters)
            response = requests.get(url)
            guideJSONs = response.json()
            # Are we at the end of pagination?
            if not guideJSONs:
               return
            offset += limit
         yield Guide(guideJSONs.pop(0)['guideid'])
   
