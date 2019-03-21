from lime_python.base.mediaType import MediaType
from lime_python.base.document import Document
from lime_python.utils.header import Header


class _ListDocument(Document):
    MIME_TYPE = 'application/vnd.lime.list+json'

    def __init__(self, header=None, items=[]):
        super().__init__(MediaType.Parse(_ListDocument.MIME_TYPE))

        self.Header = header
        self.Items = items

    @property
    def Header(self):
        return self.__Header

    @Header.setter
    def Header(self, header):
        if header is not None and not isinstance(header, Header):
            if isinstance(header, Document):
                header = Header(header)
            else:
                raise ValueError('"Header" must be a Header')
        self.__Header = header

    @property
    def Items(self):
        return self.__Items

    @Items.setter
    def Items(self, items):
        if not isinstance(items, list):
            raise ValueError('"Items" must be a list of Document')
        for i in items:
            if not isinstance(i, Document):
                raise ValueError('All Items must be a Document')
        self.__Items = items

    @property
    def Total(self):
        if self.Items is not None:
            return len(self.Items)
        return None

    def GetHeaderDocument(self):
        if self.Header is not None:
            return self.Header
        return None

    def SetHeaderDocument(self, document):
        self.Header = Header(document)

    def GetHeaderJson(self):
        if self.Header is not None:
            return self.Header.ToJson()
        return None

    def GetItems(self):
        if self.Items is not None:
            return self.Items
        return None

    def GetItemsJson(self):
        if self.Items is not None:
            return [
                {
                    'type': str(x.GetMediaType()),
                    'value': x.ToJson()
                }
                for x in self.Items
            ]
        return None

    def ToJson(self):
        return {
            'header': self.GetHeaderJson(),
            'items': self.GetItemsJson()
        }


class ListDocument(_ListDocument):

    Type = MediaType.Parse(_ListDocument.MIME_TYPE)
