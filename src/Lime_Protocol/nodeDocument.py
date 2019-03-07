from mediaType import MediaType as MediaTypeClass
from document import Document
from node import Node


class NodeDocument(Document):

    MIME_TYPE = 'application/vnd.lime.node'
    MediaType = MediaTypeClass.Parse(MIME_TYPE)

    def __init__(self, value=None):
        if value is not None:
            super().__init__(NodeDocument.MediaType)
            self.Value = value

    def __str__(self):
        return str(self.Value)

    @staticmethod
    def Parse(value):
        return NodeDocument(value)
