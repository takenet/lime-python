# IDocument Interface
# Gabriel R Santos (@chr0m1ng)

import abc


class IDocument(metaclass=abc.ABCMeta):

    # Gets the type of the media for the document
    def GetMediaType(self):
        pass
