from lime_python.base.envelope import Envelope
from lime_python.utils.reason import Reason as NotificationReason
from lime_python.utils.reason import ReasonCode
from enum import Enum


class NotificationEvent(Enum):
    Failed = 'failed'
    Accepted = 'accepted'
    Validated = 'validated'
    Authorized = 'authorized'
    Dispatched = 'dispatched'
    Received = 'received'
    Consumed = 'consumed'


class Notification(Envelope):

    def __init__(self, id=None, to=None, fromN=None, event=None, reason=None):
        super().__init__(id, fromN, to)

        self.Event = event
        self.Reason = reason

    @property
    def Event(self):
        return self.__Event

    @Event.setter
    def Event(self, event):
        if event is not None and not isinstance(event, NotificationEvent):
            raise ValueError('"Event" must be a NotificationEvent')
        self.__Event = event

    @property
    def Reason(self):
        return self.__Reason

    @Reason.setter
    def Reason(self, reason):
        if reason is not None and not isinstance(reason, NotificationReason):
            raise ValueError('"Reason" must be a Reason')
        self.__Reason = reason

    def ToJson(self):
        return {
            **super().ToJson(),
            **{
                'event': self.Event.value,
                'reason': self.Reason.ToJson()
            }
        }
