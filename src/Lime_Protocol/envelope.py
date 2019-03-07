# Envelope Class
# Gabriel R Santos (@chr0m1ng)
''' Base class to all communication documents'''
from copy import copy


class Envelope:

    def __init__(self, id=None):
        self.Id = id  # String
        self.From = None  # Node
        self.Pp = None  # Node
        self.To = None  # Node
        self.Metadata = {}  # String : String

    # Creates a shallow copy of the current Envelop
    def MemberwiseClone(self):
        return copy(self)