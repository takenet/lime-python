from lime_python.base.mediaType import MediaType
from lime_python.base.document import Document
from lime_python.utils.header import Header
from lime_python.utils.scope import Scope as SCP


class _MenuDocument(Document):

    MIME_TYPE = 'application/vnd.lime.select+json'

    def __init__(self, scope=None, text=None, options=[]):
        super().__init__(MediaType.Parse(_MenuDocument.MIME_TYPE))

        self.Scope = scope
        self.Text = text
        self.Options = options

    @property
    def Scope(self):
        return self.__Scope

    @Scope.setter
    def Scope(self, scope):
        if isinstance(scope, str):
            scope = SCP(scope)
        if scope is not None and not isinstance(scope, SCP):
            raise ValueError('"Scope" must be a Scope')
        self.__Scope = scope

    @property
    def Text(self):
        return self.__Text

    @Text.setter
    def Text(self, text):
        if not isinstance(text, str):
            raise ValueError('"Text" must be a string')
        self.__Text = text

    @property
    def Options(self):
        return self.__Options

    @Options.setter
    def Options(self, options):
        if not isinstance(options, list):
            raise ValueError('"Options" must be a list of Options')
        for o in options:
            if not isinstance(o, _MenuDocument.Option):
                raise ValueError('All items must be Options')
        self.__Options = options

    @property
    def Total(self):
        return len(self.Options)

    def GetOptionsJson(self):
        return [x.ToJson() for x in self.Options]

    def ToJson(self):
        json = {
            'options': self.GetOptionsJson()
        }

        if self.Scope is not None:
            json.update({'scope': self.Scope.value})
        if self.Text is not None:
            json.update({'text': self.Text})

        return json

    class Option:
        """
        Representation of a menu's option

        Parameters:
            order (int)
            value (Document or dict)
            text (str)
        """

        def __init__(self, order=None, value=None, text=None):

            self.Order = order
            self.Value = value
            self.Text = text

        @property
        def Order(self):
            return self.__Order

        @Order.setter
        def Order(self, order):
            if order is not None and not isinstance(order, int):
                raise ValueError('"Order" must be a integer')
            self.__Order = order

        @property
        def Value(self):
            return self.__Value

        @Value.setter
        def Value(self, value):
            if value is not None and not (isinstance(value, dict) or
                                          isinstance(value, Document)):
                raise ValueError('"Value" must be a Document or Dict')
            self.__Value = value

        @property
        def Text(self):
            return self.__Text

        @Text.setter
        def Text(self, text):
            if text is not None and not isinstance(text, str):
                raise ValueError('"Text" must be a string')
            self.__Text = text

        def GetLabelDocumentJson(self):
            if self.Label is not None:
                return self.Label.ToJson()
            return None

        def GetLabelMediaType(self):
            if self.Label is not None:
                return self.Label.GetMediaType()
            return None

        def GetValueMediaType(self):
            if self.Value is not None:
                if isinstance(self.Value, dict):
                    return MediaType.ApplicationJson
                return self.Value.GetMediaType()
            return None

        def GetValueDocumentJson(self):
            if self.Value is not None:
                if isinstance(self.Value, dict):
                    return self.Value
                return self.Value.ToJson()
            return None

        def ToJson(self):
            json = {
                'text': self.Text
            }
            if isinstance(self.Order, int):
                json.update({'order': self.Order})
            if self.Value is not None:
                json.update({
                    'type': str(self.GetValueMediaType()),
                    'value': self.GetValueDocumentJson()
                })

            return json


class MenuDocument(_MenuDocument):
    """
    Representation of a LIME menu document

    Parameters:
        scope (Scope or str)
        text (str)
        options ([Option])
    """

    Type = MediaType.Parse(_MenuDocument.MIME_TYPE)
