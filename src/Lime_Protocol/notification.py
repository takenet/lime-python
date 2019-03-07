from deprecated import deprecated
from envelope import Envelope
from enum import Enum


class Event(Enum):
    Failed = 'failed'
    Accepted = 'accepted'

    @deprecated(reason='This specific event should not be sent anymore')
    Validated = 'validated'

    @deprecated(reason='This specific event should not be sent anymore')
    Authorized = 'authorized'

    Dispatched = 'dispatched'
    Received = 'received'
    Consumed = 'consumed'


class Notification(Envelope):

    def __init__(self, id=None):
        if id is None or isinstance(str, id):
            super().__init__(id)
        else:
            super().__init__(str(id))

        self.Event = None  # Event
        self.Reason = None  # Reason
