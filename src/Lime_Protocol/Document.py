# Document Class
# Gabriel R Santos (@chr0m1ng)

from Utils.StringUtils import StringUtils
from MediaType import MediaType


class Document:

    _mediaType = None

    def __init__(MediaType mediaType):

        if mediaType is None:
            raise TypeError

        _mediaType = mediaType

    def GetMediaType(self):
        return _mediaType
