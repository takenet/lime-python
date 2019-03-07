from envelope import Envelope
from mediaType import MediaType


class Message(Envelope):

    def __init__(self, id=None):

        if id is not None:
            super().__init__(id)

        self.Content = None  # Document

    def Type(self):
        if self.Content is not None:
            return self.Content.GetMediaType()
        else:
            return None

    def GetDocument(self):
        return self.Content
