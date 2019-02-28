from Utils.StringUtils import StringUtils
from urllib.parse import urlparse
import validators


class LimeUri:

    LIME_URI_SCHEME = 'lime'
    _absoluteUri = None

    def __init__(self, uriPath):
        if StringUtils.IsNoneOrEmpty(uriPath):
            raise TypeError
        if validators.url(uriPath):
            _absoluteUri = urlparse(uriPath)
            if _absoluteUri.scheme != LIME_URI_SCHEME:
                raise ValueError('Invalid URI scheme. \
                    Expected is "%s"' % LIME_URI_SCHEME)