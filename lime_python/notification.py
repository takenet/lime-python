from envelope import Envelope
from reason import Reason
from enum import Enum


class Event(Enum):
    Failed = 'failed'
    Accepted = 'accepted'
    Validated = 'validated'
    Authorized = 'authorized'
    Dispatched = 'dispatched'
    Received = 'received'
    Consumed = 'consumed'


class Notification(Envelope):

    def __init__(self, id=None, event=None, reason=None):
        super().__init__(id)

        self.Event = event
        self.Reason = reason

    @property
    def Event(self):
        return self.__Event

    @Event.setter
    def Event(self, event):
        if event is not None and not isinstance(event, Event):
            raise ValueError('"Event" must be a Event')
        self.__Event = event

    @property
    def Reason(self):
        return self.__Reason

    @Reason.setter
    def Reason(self, reason):
        if reason is not None and not isinstance(reason, Reason):
            raise ValueError('"Reason" must be a Reason')
        self.__Reason = reason

    def ToJson(self):
        return {
            **super().ToJson(),
            **{
                'event': self.Event,
                'reason': self.Reason.ToJson()
            }
        }
