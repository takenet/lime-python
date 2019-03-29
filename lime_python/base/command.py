from lime_python.utils.reason import Reason, ReasonCode
from lime_python.base.mediaType import MediaType
from lime_python.base.envelope import Envelope
from lime_python.base.message import Message
from enum import Enum


class CommandMethod(Enum):
    """
    Enum of the available command's methods

    Values:
        Get (str)
        Set (str)
        Delete (str)
        Subscribe (str)
        Unsubscribe (str)
        Observe (str)
        Merge (str)
    """

    Get = 'get'
    Set = 'set'
    Delete = 'delete'
    Subscribe = 'subscribe'
    Unsubscribe = 'unsubscribe'
    Observe = 'observe'
    Merge = 'merge'


class CommandStatus(Enum):
    """
    Enum of the available command's status

    Values:
        Pending (str)
        Success (str)
        Failure (str)
    """

    Pending = 'pending'
    Success = 'success'
    Failure = 'failure'


class Command(Envelope):
    """
    Representation of a LIME Command

    Parameters:
        id (str)
        fromN (Node)
        to (Node)
        uri (str)
        resource (Document)
        method (CommandMethod)
        status (CommandStatus)
        reason (Reason)
    """

    def __init__(self, id=None, fromN=None, to=None, uri=None, resource=None,
                 method=None, status=None, reason=None, mediaType=None):
        super().__init__(id, fromN, to)

        self.Uri = uri
        self.Resource = resource
        self.Method = method
        self.Status = status
        self.Reason = reason
        self.Type = mediaType

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
        self.__Resource = resource

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, method):
        if isinstance(method, str):
            method = CommandMethod(method)
        if method is not None and not isinstance(method, CommandMethod):
            raise ValueError('"Method" must be a CommandMethod')
        self.__Method = method

    @property
    def Status(self):
        return self.__Status

    @Status.setter
    def Status(self, status):
        if isinstance(status, str):
            status = CommandStatus(status)
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

    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self, mediaType):
        if isinstance(mediaType, str):
            mediaType = MediaType.Parse(mediaType)
        if mediaType is not None and not isinstance(mediaType, MediaType):
            raise ValueError('"Type" must be a str or MediaType')
        self.__Type = mediaType

    def GetResourceJson(self):
        if self.Resource is not None:
            try:
                return self.Resource.ToJson()
            except:
                return str(self.Resource)
        return None

    def ToJson(self):
        json = {
            **super().ToJson(),
            'method': self.Method.value
        }
        if self.Uri is not None:
            json.update({'uri': self.Uri})
        if self.Status is not None:
            json.update({'status': self.Status.value})
        if self.Type is not None:
            json.update({'type': str(self.Type)})
        if self.Resource is not None:
            resourceName = type(self.Resource).__name__.lower()
            json.update({
                'resource': {
                    resourceName: self.GetResourceJson()
                }
            })
        if self.Reason is not None:
            json.update({'reason': self.Reason.ToJson()})

        return json
