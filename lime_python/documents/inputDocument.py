from lime_python.documents.plainTextDocument import PlainTextDocument
from lime_python.base.mediaType import MediaType as MT
from lime_python.base.document import Document
from enum import Enum


class Rule(Enum):
    Type = 'type'
    Text = 'text'


class Validation:
    def __init__(self, rule, mediaType=None):

        self.MediaType = mediaType
        self.Rule = rule

    @property
    def Rule(self):
        return self.__Rule

    @Rule.setter
    def Rule(self, rule):
        if not isinstance(rule, Rule):
            raise ValueError('"Rule" must be a Rule')
        if rule == Rule.Type:
            if self.MediaType is None:
                raise TypeError('"MediaType" cannot be None to Rule.Type')
        self.__Rule = rule

    @property
    def MediaType(self):
        return self.__MediaType

    @MediaType.setter
    def MediaType(self, mediaType):
        if mediaType is not None and not isinstance(mediaType, MT):
            raise ValueError('"MediaType" must be MediaType')
        self.__MediaType = mediaType

    def ToJson(self):
        json = {
            'rule': self.Rule.value
        }
        if self.MediaType is not None:
            json.update({'type': str(self.MediaType)})

        return json


class _InputDocument(Document):

    MIME_TYPE = 'application/vnd.lime.input+json'

    def __init__(self, label=None, validation=None):
        super().__init__(MT.Parse(_InputDocument.MIME_TYPE))

        self.Label = label
        self.Validation = validation

    @property
    def Label(self):
        return self.__Label

    @Label.setter
    def Label(self, label):
        if isinstance(label, str):
            label = PlainTextDocument(label)
        if label is None or isinstance(label, PlainTextDocument):
            self.__Label = label
        else:
            raise ValueError('"Label" must be a PlainTextDocument')

    @property
    def Validation(self):
        return self.__Validation

    @Validation.setter
    def Validation(self, validation):
        if validation is not None and not isinstance(validation, Validation):
            raise ValueError('"Validation" must be a Validation')
        self.__Validation = validation

    def GetLabelDocumentJson(self):
        if self.Label is not None:
            return self.Label.ToJson()
        return None

    def GetLabelMediaType(self):
        if self.Label is not None:
            return self.Label.GetMediaType()
        return None

    def GetValidation(self):
        return self.Validation

    def GetValidationJson(self):
        if self.Validation is not None:
            return self.Validation.ToJson()
        return None

    def SetValidation(self, validation):
        self.Validation = validation

    def ToJson(self):
        return {
            'label': {
                'type': str(self.GetLabelMediaType()),
                'value':
                self.GetLabelDocumentJson()
            },
            'validation': self.GetValidationJson()
        }


class InputDocument(_InputDocument):

    Type = MT.Parse(_InputDocument.MIME_TYPE)
