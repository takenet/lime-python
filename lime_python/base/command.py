from lime_python.base.document import Document
from lime_python.base.envelope import Envelope
from lime_python.base.message import Message
from lime_python.utils.reason import Reason
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

    def __init__(self, id=None, fromN=None, to=None, uri=None, resource=None,
                 method=None, status=None, reason=None):
        super().__init__(id, fromN, to)

        self.Uri = uri
        self.Resource = resource
        self.Method = method
        self.Status = status
        self.Reason = reason

    @property
    def Uri(self):
        return self.__Uri

    @Uri.setter
    def Uri(self, uri):
        if uri is not None and not isinstance(uri, str):
            raise ValueError('"Uri" must be a string')
        self.__Uri = uri

    @property
    def Resource(self):
        return self.__Resource

    @Resource.setter
    def Resource(self, resource):
        if resource is not None and not isinstance(resource, Document):
            raise ValueError('"Resource" must be a Document')
        self.__Resource = resource

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, method):
        if method is not None and not isinstance(method, CommandMethod):
            raise ValueError('"Method" must be a CommandMethod')
        self.__Method = method

    @property
    def Status(self):
        return self.__Status

    @Status.setter
    def Status(self, status):
        if status is not None and not isinstance(status, CommandStatus):
            raise ValueError('"Status" must be a CommandStatus')
        self.__Status = status

    @property
    def Reason(self):
        return self.__Reason

    @Reason.setter
    def Reason(self, reason):
        if reason is not None and not isinstance(reason, Reason):
            raise ValueError('"Reason" must be a Reason')
        self.__Reason = reason

    def Type(self):
        return self.Resource.GetMediaType()

    def SetDocument(self, document):
        self.Resource = document

    def GetDocument(self):
        return self.Resource

    def GetDocumentJson(self):
        if self.Resource is not None:
            return self.Resource.ToJson()
        return None

    def ToJson(self):
        return {
            **super().ToJson(),
            **{
                'method': self.Method,
                'uri': self.Uri,
                'type': self.Type,
                'resource': self.GetDocumentJson()
            }
        }
