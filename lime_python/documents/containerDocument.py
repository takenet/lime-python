from lime_python.base.document import Document
from lime_python.base.mediaType import MediaType


class _ContainerDocument(Document):

    MIME_TYPE = "application/vnd.lime.container+json"

    def __init__(self, value=None):
        super().__init__(MediaType.Parse(_ContainerDocument.MIME_TYPE))
        self.Value = value

    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, value):
        if value is not None and not isinstance(value, Document):
            raise ValueError('"Value" must be a Document')
        self.__Value = value

    def GetDocument(self):
        return self.Value

    def GetDocumentJson(self):
        if self.Value is not None:
            return self.Value.ToJson()
        return None

    def SetDocument(self, document):
        self.Value = document

    def ValueType(self):
        if self.Value is not None:
            return self.Value.GetMediaType()
        return None

    def ToJson(self):
        return {
            'type': str(self.ValueType()),
            'value': self.GetDocumentJson()
        }


class ContainerDocument(_ContainerDocument):

    Type = MediaType.Parse(_ContainerDocument.MIME_TYPE)
