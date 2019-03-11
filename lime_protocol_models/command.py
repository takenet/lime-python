from envelope import Envelope
from envelopeId import EnvelopeId
from message import Message
from enum import Enum


class CommandMethod(Enum):

    Get = 'get'
    Set = 'set'
    Delete = 'delete'
    Subscribe = 'subscribe'
    Unsubscribe = 'unsubscribe'
    Observe = 'observe'
    Merge = 'merge'


class CommandStatus(Enum):
    Pending = 'pending'
    Success = 'success'
    Failure = 'failure'


class Command(Envelope):

    Uri = None

    def __init__(self, id=None):
        if id is not None:
            super().__init__(id)
        else:
            super().__init__(EnvelopeId.NewId())

        self.Uri = None  # LimeUri
        self.Resource = None  # Document
        self.Method = None  # CommandMethod
        self.Status = None  # CommandStatus
        self.Reason = None  # Reason

    def Type(self):
        return self.Resource.GetMediaType()

    def GetDocument(self):
        return self.Resource
