from Document import Document
from MediaType import MediaType as MediaTypeClass


class DocumentContainer(Document):

    MIME_TYPE = "application/vnd.lime.container+json"

    MediaType = MediaTypeClass.Parse(MIME_TYPE)

    def __init__(self):
        super()__init__(MediaType)
        self.Value = None

    def Type(self):
        return self.GetMediaType()

    def GetDocument(self):
        return self.Value
