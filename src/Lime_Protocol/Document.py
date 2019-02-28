# Document Class
# Gabriel R Santos (@chr0m1ng)

from Utils.StringUtils import StringUtils


class Document():

    def __init__(self, mediaType):
        if mediaType is None:
            raise TypeError
        self._mediaType = mediaType

    def GetMediaType(self):
        return self._mediaType

    # TODO: Document func returns a new PlainDocument
