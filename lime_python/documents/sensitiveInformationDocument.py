from lime_python.base.mediaType import MediaType
from lime_python.base.document import Document


class _SensitiveInformationDocument(Document):

    MIME_TYPE = 'application/vnd.lime.sensitive+json'

    def __init__(self, value):
        super().__init__(
            MediaType.Parse(_SensitiveInformationDocument.MIME_TYPE))

        self.Value = value

    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, value):
        if not isinstance(value, Document):
            raise ValueError('"Value" must be a Document')
        self.__Value = value

    def GetValueMediaType(self):
        return self.Value.GetMediaType()

    def GetValueJson(self):
        return self.Value.ToJson()

    def ToJson(self):
        return {
            'type': str(self.GetValueMediaType()),
            'value': self.GetValueJson()
        }


class SensitiveInformationDocument(_SensitiveInformationDocument):

    Type = MediaType.Parse(_SensitiveInformationDocument.MIME_TYPE)
