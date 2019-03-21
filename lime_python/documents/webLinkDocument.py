from lime_python.base.mediaType import MediaType
from lime_python.base.document import Document
from enum import Enum


class Target(Enum):

    Blank = 'blank'
    Self = 'self'
    SelfCompact = 'selfCompact'
    SelfTall = 'selfTall'


class _WebLinkDocument(Document):

    MIME_TYPE = 'application/vnd.lime.web-link+json'

    def __init__(self, uri, title=None, text=None,
                 previewUri=None, target=None):
        super().__init__(MediaType.Parse(_WebLinkDocument.MIME_TYPE))

        self.Uri = uri
        self.Title = title
        self.Text = text
        self.PreviewUri = previewUri
        self.Target = target

    @property
    def Uri(self):
        return self.__Uri

    @Uri.setter
    def Uri(self, uri):
        if not isinstance(uri, str):
            raise ValueError('"Uri" must be a string')
        self.__Uri = uri

    @property
    def Title(self):
        return self.__Title

    @Title.setter
    def Title(self, title):
        if title is not None and not isinstance(title, str):
            raise ValueError('"Title" must be a string')
        self.__Title = title

    @property
    def Text(self):
        return self.__Text

    @Text.setter
    def Text(self, text):
        if text is not None and not isinstance(text, str):
            raise ValueError('"Text" must be a string')
        self.__Text = text

    @property
    def PreviewUri(self):
        return self.__PreviewUri

    @PreviewUri.setter
    def PreviewUri(self, previewUri):
        if previewUri is not None and not isinstance(previewUri, str):
            raise ValueError('"PreviewUri" must be a string')
        self.__PreviewUri = previewUri

    @property
    def Target(self):
        return self.__Target

    @Target.setter
    def Target(self, target):
        if target is not None and not isinstance(target, Target):
            raise ValueError('"Target" must be a Target')
        self.__Target = target

    def ToJson(self):
        json = {
            'uri': self.Uri
        }
        if self.Title is not None:
            json.update({'title': self.Title})
        if self.Text is not None:
            json.update({'text': self.Text})
        if self.PreviewUri is not None:
            json.update({'previewUri': self.PreviewUri})
        if self.Target is not None:
            json.update({'target': self.Target})

        return json


class WebLinkDocument(_WebLinkDocument):

    Type = MediaType.Parse(_WebLinkDocument.MIME_TYPE)
