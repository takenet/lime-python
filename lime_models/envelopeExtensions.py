from jsonDocument import JsonDocument
from notification import Notification
from mediaType import MediaType
from message import Message
from copy import copy
import jsonpickle


class EnvelopeExtensions:

    COMMAND_MIME_TYPE = 'application/vnd.lime.command+json'
    MESSAGE_MIME_TYPE = 'application/vnd.lime.message+json'
    NOTIFICATION_MIME_TYPE = 'application/vnd.lime.notification+json'

    CommandMediaType = MediaType.Parse(COMMAND_MIME_TYPE)
    MessageMediaType = MediaType.Parse(MESSAGE_MIME_TYPE)
    NotificationMediaType = MediaType.Parse(NOTIFICATION_MIME_TYPE)

    @staticmethod
    def ToDocument(envelope, mediaType):
        if envelope is None:
            raise TypeError
        if mediaType is None:
            raise TypeError
        dictionary = jsonpickle.encode(envelope)
        return JsonDocument(mediaType, dictionary)

    @staticmethod
    def ToEnvelope(jsonDocument, mediaType):
        if mediaType == EnvelopeExtensions.CommandMediaType:
            envelopeType = type(Command())
        elif mediaType == EnvelopeExtensions.MessageMediaType:
            envelopeType = type(Message())
        elif mediaType == EnvelopeExtensions.NotificationMediaType:
            envelopeType = type(Notification())
        else:
            raise ValueError('Unknown envelope media type')
        return jsonpickle.decode(jsonDocument.GetJson())

    @staticmethod
    def ShallowCopy(envelope):
        return copy(envelope)

    @staticmethod
    def GetSender(envelope):
        if envelope.Pp is not None:
            return envelope.Pp
        else:
            return envelope.From
