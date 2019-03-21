from lime_python.base.mediaType import MediaType as MT


class Document:

    def __init__(self, mediaType):

        self.MediaType = mediaType

    @property
    def MediaType(self):
        return self.__MediaType

    @MediaType.setter
    def MediaType(self, mediaType):
        if not isinstance(mediaType, MT):
            raise ValueError('"MediaType" must be a MediaType')
        self.__MediaType = mediaType

    def GetMediaType(self):
        if self.MediaType is not None:
            return self.MediaType
        return None

    def ToJson(self):
        return {
            'type': self.GetMediaType()
        }
