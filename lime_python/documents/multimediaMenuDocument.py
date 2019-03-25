from lime_python.base.mediaType import MediaType
from lime_python.base.document import Document
from lime_python.utils.header import Header
from lime_python.utils.scope import Scope


class _MultimediaMenuDocument(Document):

    MIME_TYPE = 'application/vnd.lime.document-select+json'

    def __init__(self, scope=Scope.Transient, header=None, options=[]):

        self.Scope = scope
        self.Header = header
        self.Options = options

    @property
    def Scope(self):
        return self.__Scope

    @Scope.setter
    def Scope(self, scope):
        if not isinstance(scope, Scope):
            raise ValueError('"Scope" must be a Scope')
        self.__Scope = scope

    @property
    def Header(self):
        return self.__Header

    @Header.setter
    def Header(self, header):
        if header is not None and not isinstance(header, Header):
            if isinstance(header, Document):
                header = Header(header)
            elif not isinstance(header, str):
                raise ValueError('"Header" must be a Header or string')
        self.__Header = header

    @property
    def Options(self):
        return self.__Options

    @Options.setter
    def Options(self, options):
        if not isinstance(options, list):
            raise ValueError('"Options" must be a list of Options')
        for o in options:
            if not isinstance(o, _MultimediaMenuDocument.Option):
                raise ValueError('All items must be Options')
        self.__Options = options

    @property
    def Total(self):
        return len(self.Options)

    def GetOptionsJson(self):
        return [x.ToJson() for x in self.Options]

    def GetHeaderType(self):
        if self.Header is not None:
            return self.Header.GetMediaType()
        return None

    def GetHeaderJson(self):
        if self.Header is not None:
            return self.Header.ToJson()
        return None

    def ToJson(self):
        json = {
            'scope': self.Scope.value
        }

        if isinstance(self.Header, str):
            json.update({'text': self.Header})
        else:
            json.update({'header': self.GetHeaderJson()})

        json.update({'options': self.GetOptionsJson()})

        return json

    class Option:
        def __init__(self, order=None, label=None, value=None, text=None):

            self.Order = order
            self.Label = label
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
        def Label(self):
            return self.__Label

        @Label.setter
        def Label(self, label):
            if label is not None and not isinstance(label, Document):
                raise ValueError('"Label" must be a Document')
            self.__Label = label

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
            json = {}
            if isinstance(self.Order, int):
                json.update({'order': self.Order})
            if self.Text is not None:
                json.update({'text': self.Text})
            elif self.Label is not None:
                json.update({
                    'label': {
                        'type': str(self.GetLabelMediaType()),
                        'value': self.GetLabelDocumentJson()
                    }
                })
            if isinstance(self.Value, Document) \
                    or isinstance(self.Value, dict):
                json.update({
                    'value': {
                        'type': str(self.GetValueMediaType()),
                        'value': self.GetValueDocumentJson()
                    }
                })

            return json


class MultimediaMenuDocument(_MultimediaMenuDocument):

    Type = MediaType.Parse(_MultimediaMenuDocument.MIME_TYPE)
