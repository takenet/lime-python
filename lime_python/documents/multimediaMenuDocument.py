from lime_python.documents.plainTextDocument import PlainTextDocument
from lime_python.base.mediaType import MediaType
from lime_python.base.document import Document
from lime_python.utils.header import Header as HD
from lime_python.utils.scope import Scope as SCP


class _MultimediaMenuDocument(Document):

    MIME_TYPE = 'application/vnd.lime.document-select+json'

    def __init__(self, scope=None, header=None, options=[]):

        self.Scope = scope
        self.Header = header
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
    def Header(self):
        return self.__Header

    @Header.setter
    def Header(self, header):
        if isinstance(header, str):
            header = HD(header)
        if header is not None and not isinstance(header, HD):
            if isinstance(header, Document):
                header = HD(header)
            else:
                raise ValueError(
                    '"Header" must be a Header, Document or string')
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
            'options': self.GetOptionsJson()
        }
        if self.Scope is not None:
            json.update({'scope': self.Scope.value})
        if self.Header is not None:
            json.update({'header': self.GetHeaderJson()})

        return json

    class Option:
        """
        Representation of a multimedia menu's option

        Parameters:
            order (int)
            label (Document or str)
            value (Document or dict)
        """

        def __init__(self, order=None, label=None, value=None):

            self.Order = order
            self.Label = label
            self.Value = value

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
            if isinstance(label, str):
                label = PlainTextDocument(label)
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
            elif self.Label is not None:
                json.update({
                    'label': {
                        'type': str(self.GetLabelMediaType()),
                        'value': self.GetLabelDocumentJson()
                    }
                })
            if self.Value is not None:
                json.update({
                    'value': {
                        'type': str(self.GetValueMediaType()),
                        'value': self.GetValueDocumentJson()
                    }
                })

            return json


class MultimediaMenuDocument(_MultimediaMenuDocument):
    """
    Representation of a LIME multimedia menu document

    Parameters:
        scope (Scope)
        header (Header)
        options ([Option])
    """

    Type = MediaType.Parse(_MultimediaMenuDocument.MIME_TYPE)
