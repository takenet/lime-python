# Envelope Class
# Gabriel R Santos (@chr0m1ng)
''' Base class to all communication documents'''
from copy import copy


class Envelope:
    ID_KEY = "id"
    FROM_KEY = "from"
    PP_KEY = "pp"
    TO_KEY = "to"
    METADATA_KEY = "metadata"

    def __init__(self, id=None):
        self.Id = id
        self.From = None  # Node
        self.Pp = None  # Node
        self.To = None  # Node
        self.Metadata = {}  # string : string

    # Creates a shallow copy of the current Envelop
    def MemberwiseClone(self):
        return copy(self)
