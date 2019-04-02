from lime_python.documents.plainTextDocument import PlainTextDocument
from lime_python.base.mediaType import MediaType
from lime_python.base.document import Document


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
        if isinstance(value, str):
            value = PlainTextDocument(value)
        if value is not None and not isinstance(value, Document) and\
                not isinstance(value, dict):
            raise ValueError('"Value" must be a Document, dict or str')
        self.__Value = value

    def GetDocument(self):
        return self.Value

    def GetDocumentJson(self):
        if self.Value is not None:
            if isinstance(self.Value, dict):
                return self.Value
            return self.Value.ToJson()
        return None

    def SetDocument(self, document):
        self.Value = document

    def ValueType(self):
        if self.Value is not None:
            if isinstance(self.Value, dict):
                return MediaType.ApplicationJson
            return self.Value.GetMediaType()
        return None

    def ToJson(self):
        return {
            'type': str(self.ValueType()),
            'value': self.GetDocumentJson()
        }


class ContainerDocument(_ContainerDocument):
    """
    Representation of a LIME container document

    Parameters:
        value (Document, dict or str)
    """

    Type = MediaType.Parse(_ContainerDocument.MIME_TYPE)
