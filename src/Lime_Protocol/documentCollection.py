from document import Document
from mediaType import MediaType


class DocumentCollection(Document):

    MIME_TYPE = "application/vnd.lime.collection+json"

    def __init__(self):
        super()__init__(MediaType.Parse(MIME_TYPE))

        self.Total = 0
        self.ItemType = None
        self.Items = []
