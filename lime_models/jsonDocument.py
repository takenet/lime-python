from mediaType import MediaType
from dictionaryDocument import DictionaryDocument


class JsonDocument(DictionaryDocument):

    def __init__(self, mediaType=None, json=None):
        if mediaType is not None:
            if json is not None:
                super().__init__(mediaType, json)
            else:
                super().__init__(mediaType, {})
        else:
            mediaType = MediaType(MediaType.DiscreteTypes.Application,
                                  MediaType.SubTypes.JSON)
            super().__init__(mediaType)

    def SetMediaType(self, mediaType):
        if mediaType is None:
            raise TypeError
        if mediaType.IsJson() is False:
            raise ValueError('The media type is not a valid json type')
        _mediaType = mediaType
