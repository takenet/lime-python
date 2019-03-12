# Document Class
# Gabriel R Santos (@chr0m1ng)

from utils.stringUtils import StringUtils
from mediaType import MediaType
from jsonpickle import encode


class Document:

    def __init__(self, mediaType):

        if mediaType is None:
            raise TypeError

        self._mediaType = mediaType

    def GetMediaType(self):
        return self._mediaType

    def ToJson(self):
        return encode(self)
