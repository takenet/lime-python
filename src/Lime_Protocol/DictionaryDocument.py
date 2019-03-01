from Document import Document
from MediaType import MediaType


class DictionaryDocument(Document):

    def __init__(self, mediaType, json=None):
        super().__init__(mediaType)
        if json is not None:
            self._json = json
            if mediaType.IsJson() is False:
                raise ValueError('The media type is not a valid json type')
        else:
            self._json = {}

    def Add(self, key, value):
        self._json.update({key: value})

    def Clear(self):
        self._json.clear()

    def Contains(self, item):
        return item in self._json

    def Remove(self, key, value=None):
        if value is None:
            del self._json[key]
        else:
            self._json[key].remove(value)

    def TryGetValue(self, key):
        if self._json.__contains__(key):
            return True, self._json[key]
        else:
            return False, None

    def Keys(self):
        return self._json.keys()

    def Values(self):
        return self._json.values()
