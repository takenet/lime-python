from lime_python.base.document import Document
from lime_python.base.mediaType import MediaType


class PlainTextDocument(Document):

    def __init__(self, value=None):
        super().__init__(MediaType.TextPlain)
        self.Value = value

    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, value):
        if not isinstance(value, str):
            raise ValueError('"Value" must be a string')
        self.__Value = value

    @property
    def Type(self):
        return MediaType.TextPlain

    def __str__(self):
        if self.Value is not None:
            return str(self.Value)
        return 'None'

    def ToJson(self):
        return str(self.Value)  # For plain/text we only need the text itself
