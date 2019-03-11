from notification import Notification
from envelopeType import EnvelopeType
from session import Session
from message import Message
from command import Command


class TypeExtensions:

    @staticmethod
    def GetEnvelopeType(envelope):
        if isinstance(envelope, Notification):
            return EnvelopeType.Notification
        if isinstance(envelope, Message):
            return EnvelopeType.Message
        if isinstance(envelope, Command):
            return EnvelopeType.Command
        if isinstance(envelope, Session):
            return EnvelopeType.Session
        raise ValueError('Invalid envelope type')
