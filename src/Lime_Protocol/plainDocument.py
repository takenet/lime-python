from utils.stringUtils import StringUtils
from document import Document
from mediaType import MediaType


class PlainDocument(Document):

    def __init__(self, mediaType, value=None):
        super().__init__(mediaType)
        if StringUtils.IsNoneOrEmpty(mediaType.Suffix) is False:
            raise ValueError(
                'Invalid media type. The suffix value should be empty')
        self.Value = value

    def __str__(self):
        return str(self.Value)
