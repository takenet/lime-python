from lime_python.base.mediaType import MediaType
from lime_python.base.envelope import Envelope
from lime_python.base.document import Document


class Message(Envelope):

    def __init__(self, id=None, fromN=None, to=None, content=None):
        super().__init__(id, fromN, to)
        self.Content = content

    @property
    def Content(self):
        return self.__Content

    @Content.setter
    def Content(self, content):
        if content is not None and not isinstance(content, Document) and \
                not isinstance(content, dict):
            raise ValueError('"Content" must be a Document')
        self.__Content = content

    @property
    def Type(self):
        if self.Content is not None:
            if isinstance(self.Content, dict):
                return MediaType.ApplicationJson
            return self.Content.GetMediaType()
        else:
            return None

    def SetDocument(self, document):
        self.Content = document

    def GetDocument(self):
        if self.Content is not None:
            return self.Content
        return None

    def GetDocumentJson(self):
        if self.Content is not None:
            if isinstance(self.Content, dict):
                return self.Content
            return self.Content.ToJson()
        return None

    def ToJson(self):
        return {
            **super().ToJson(),
            **{
                'type': str(self.Type),
                'content': self.GetDocumentJson()
            }
        }
