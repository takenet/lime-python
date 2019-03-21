from lime_python.base.document import Document


class Header:
    def __init__(self, value=None):
        self.Value = value

    @property
    def Value(self):
        return self.__Value

    @Value.setter
    def Value(self, value):
        if value is not None and not isinstance(value, Document):
            raise ValueError('"Value" must be a Document')
        self.__Value = value

    def GetMediaType(self):
        if self.Value is not None:
            return self.Value.GetMediaType()
        return None

    def GetValueJson(self):
        if self.Value is not None:
            return self.Value.ToJson()
        return None

    def ToJson(self):
        return {
            'type': str(self.GetMediaType()),
            'value': self.GetValueJson()
        }
