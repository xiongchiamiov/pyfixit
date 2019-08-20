
import requests

from .base import Base
from .constants import API_BASE_URL

class Image(Base):
   '''An image that has been uploaded to the site.
   
   :var int id: The id of this image. Ex: ``26674``.
   :var int height: *(Lazy)* Height in pixels. Ex: ``1200``.
   :var int width: *(Lazy)* Width in pixels. Ex: ``1600``.
   :var string original: *(Lazy, Optional)* URL to the originally-uploaded
                         image.
   :var string mini: *(Lazy, Optional)* URL to the mini size of the image.
   :var string thumbnail: *(Lazy, Optional)* URL to the thumbnail size of the
                          image.
   :var string standard: *(Lazy, Optional)* URL to the standard size of the
                         image.
   :var string medium: *(Lazy, Optional)* URL to the medium size of the image.
   :var string large: *(Lazy, Optional)* URL to the large size of the image.
   :var string huge: *(Lazy, Optional)* URL to the huge size of the image.
   '''
   def __init__(self, id):
      self.id = id
   
   def __str__(self):
      return self.name # FIXME
   
   def __repr__(self):
      return '<Image %s>' % self.id
   
   def __eq__(self, other):
      if not isinstance(other, Image):
         return false
      
      return self.id == other.id
   
   def refresh(self):
      '''Refetch instance data from the API.
      '''
      response = requests.get('%s/media/images/%s' % (API_BASE_URL, self.id))
      attributes = response.json()
      
      #self.exif = attributes['exif']
      self.height = attributes['height']
      self.width = attributes['width']
      #self.ratio = attributes['ratio']
      #self.markup = attributes['markup']
      #self.srcid = attributes['srcid']
      
      image = attributes['image']
      # Images are allowed to have different sizes, depending on the dimensions
      # of the original image.  To avoid doing a bunch of explicit 'in' checks,
      # splat the variables into scope.
      del(image['id'])
      for size in image:
         vars(self)[size] = image[size]

