from lime_python.documents.plainTextDocument import PlainTextDocument
from lime_python.base.mediaType import MediaType
from lime_python.base.document import Document
from lime_python.base.node import Node


class _RedirectDocument(Document):

    MIME_TYPE = 'application/vnd.lime.redirect+json'

    def __init__(self, address=None, context=None):
        super().__init__(MediaType.Parse(_RedirectDocument.MIME_TYPE))

        self.Address = address
        self.Context = context

    @property
    def Address(self):
        return self.__Address

    @Address.setter
    def Address(self, address):
        if address is not None and not isinstance(address, Node):
            if isinstance(address, str):
                address = Node.Parse(address)
            else:
                raise ValueError('"Address" must be a Node')
        self.__Address = address

    @property
    def Context(self):
        return self.__Context

    @Context.setter
    def Context(self, context):
        if context is not None and not isinstance(context, Document):
            if isinstance(context, str):
                context = PlainTextDocument(context)
            else:
                raise ValueError('"Context" must be a Document')
        self.__Context = context

    def GetContextMediaType(self):
        if self.Context is not None:
            return self.Context.GetMediaType()
        return None

    def GetContextJson(self):
        if self.Context is not None:
            return self.Context.ToJson()
        return None

    def ToJson(self):
        json = {}
        if self.Address is not None:
            json.update({'address': str(self.Address)})
        if self.Context is not None:
            json.update({
                'context': {
                    'type': str(self.GetContextMediaType()),
                    'value': self.GetContextJson()
                }
            })

        return json


class RedirectDocument(_RedirectDocument):

    Type = MediaType.Parse(_RedirectDocument.MIME_TYPE)
