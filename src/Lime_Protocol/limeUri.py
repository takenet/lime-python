from utils.stringUtils import StringUtils
from urllib.parse import urlparse
import validators


class LimeUri:

    LIME_URI_SCHEME = 'lime'

    def __init__(self, uriPath):
        self._absoluteUri = None
        self.Path = None
        if StringUtils.IsNoneOrEmpty(uriPath):
            raise TypeError
        if validators.url(uriPath):
            self._absoluteUri = urlparse(uriPath)
            if self._absoluteUri.scheme != LIME_URI_SCHEME:
                raise ValueError('Invalid URI scheme. \
                    Expected is "%s"' % LIME_URI_SCHEME)
        else:
            raise ValueError('Invalid URI format')

        self.Path = uriPath.rstrip('/')

    def IsRelative(self):
        return self._absoluteUri is None

    def ToUri(self, authority=None):
        if self._absoluteUri is None:
            raise ValueError('The URI path is relative')
        if authority is None:
            return self._absoluteUri
        else:
            baseUri = LimeUri.GetBaseUri(authority)
            return urlparse(baseUri + self.Path)

    def __hash__(self):
        return hash(str(self).lower())

    def __eq__(self, limeUri):
        return limeUri is not None and \
            self.Path.lower() == limeUri.lower()

    def __str__(self):
        return self.Path

    @staticmethod
    def Parse(value):
        return LimeUri(value)

    @staticmethod
    def GetBaseUri(authority):
        return urlparse('%s://%s/' % (LimeUri.LIME_URI_SCHEME, authority))
