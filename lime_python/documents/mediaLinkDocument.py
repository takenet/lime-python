from lime_python.base.mediaType import MediaType as MT
from lime_python.base.document import Document


class _MediaLinkDocument(Document):

    MIME_TYPE = 'application/vnd.lime.media-link+json'

    def __init__(self, mimeType=None, size=None, aspectRatio=None, uri=None,
                 title=None, text=None, previewType=None, previewUri=None):
        super().__init__(MT.Parse(_MediaLinkDocument.MIME_TYPE))

        self.MimeType = mimeType
        self.Size = size
        self.AspectRatio = aspectRatio
        self.Uri = uri
        self.Title = title
        self.Text = text
        self.PreviewType = previewType
        self.PreviewUri = previewUri

    @property
    def MimeType(self):
        return self.__MimeType

    @MimeType.setter
    def MimeType(self, mimeType):
        if mimeType is not None and not isinstance(mimeType, MT):
            raise ValueError('"MimeType" must be a MimeType')
        self.__MimeType = mimeType

    @property
    def Size(self):
        return self.__Size

    @Size.setter
    def Size(self, size):
        if size is not None and not isinstance(size, float):
            raise ValueError('"Size" must be a float')
        self.__Size = size

    @property
    def AspectRatio(self):
        return self.__AspectRatio

    @AspectRatio.setter
    def AspectRatio(self, aspectRatio):
        if aspectRatio is not None and not isinstance(aspectRatio, str):
            raise ValueError('"AspectRatio" must be a string')
        self.__AspectRatio = aspectRatio

    @property
    def Uri(self):
        return self.__Uri

    @Uri.setter
    def Uri(self, uri):
        if uri is not None and not isinstance(uri, str):
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
    def PreviewType(self):
        return self.__PreviewType

    @PreviewType.setter
    def PreviewType(self, previewType):
        if previewType is not None and not isinstance(previewType, str):
            raise ValueError('"PreviewType" must be a string')
        self.__PreviewType = previewType

    @property
    def PreviewUri(self):
        return self.__PreviewUri

    @PreviewUri.setter
    def PreviewUri(self, previewUri):
        if previewUri is not None and not isinstance(previewUri, str):
            raise ValueError('"PreviewUri" must be a string')
        self.__PreviewUri = previewUri

    def ToJson(self):
        json = {
            'uri': self.Uri
        }
        if self.MimeType is not None:
            json.update({'type': self.MimeType})
        if self.Text is not None:
            json.update({'text': self.Text})
        if self.Size is not None:
            json.update({'size': self.Size})
        if self.AspectRatio is not None:
            json.update({'aspectRatio': self.AspectRatio})
        if self.Title is not None:
            json.update({'title': self.Title})
        if self.PreviewType is not None:
            json.update({'previewType': self.PreviewType})
        if self.PreviewUri is not None:
            json.update({'previewUri': self.PreviewUri})

        return json


class MediaLinkDocument(_MediaLinkDocument):

    Type = MT.Parse(_MediaLinkDocument.MIME_TYPE)
