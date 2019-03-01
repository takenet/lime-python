from enum import Enum


class EnvelopeType(Enum):

    Message = 'message'
    Notification = 'notification'
    Command = 'command'
    Session = 'session'
