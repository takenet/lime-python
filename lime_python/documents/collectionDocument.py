from lime_python.base.document import Document
from lime_python.base.mediaType import MediaType


class _CollectionDocument(Document):

    MIME_TYPE = "application/vnd.lime.collection+json"

    def __init__(self, itemType, items=[]):
        super().__init__(MediaType.Parse(_CollectionDocument.MIME_TYPE))

        self.ItemType = itemType
        self.Items = items

    @property
    def ItemType(self):
        return self.__ItemType

    @ItemType.setter
    def ItemType(self, itemType):
        if itemType is not None and not isinstance(itemType, Document):
            raise ValueError('"ItemType" must be a MediaType')

    @property
    def Items(self):
        return self.__Items

    @Items.setter
    def Items(self, items):
        if not isinstance(items, list):
            raise ValueError(
                '"Items" must be a list of Document')
        for i in items:
            if not isinstance(i, Document):
                raise ValueError('All Items must be a Document')

        self.__Items = items

    @property
    def Total(self):
        return len(self.Items)

    def GetDocumentsJson(self):
        return [x.ToJson() for x in self.Items]

    def ToJson(self):
        return {
            'itemType': str(self.ItemType),
            'items': self.GetDocumentsJson()
        }


class CollectionDocument(_CollectionDocument):

    Type = MediaType.Parse(_CollectionDocument.MIME_TYPE)
