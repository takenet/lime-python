from lime_python.utils.limeException import LimeException
from lime_python.base.mediaType import MediaType


def GetBaseByClassName(className):
    """
    Returns a base class of the given class name

    Parameters:
        className (str)
    """

    from lime_python.base.mediaType import MediaType
    from lime_python.base.document import Document
    from lime_python.base.identity import Identity
    from lime_python.base.node import Node
    from lime_python.base.envelope import Envelope
    from lime_python.base.message import Message
    from lime_python.base.notification import Notification, NotificationEvent
    from lime_python.base.command import Command, CommandMethod, CommandStatus

    BASE_TYPES = {
        MediaType.__name__.lower(): MediaType,
        Document.__name__.lower(): Document,
        Identity.__name__.lower(): Identity,
        Node.__name__.lower(): Node,
        Envelope.__name__.lower(): Envelope,
        Message.__name__.lower(): Message,
        Notification.__name__.lower(): Notification,
        NotificationEvent.__name__.lower(): NotificationEvent,
        Command.__name__.lower(): Command,
        CommandMethod.__name__.lower(): CommandMethod,
        CommandStatus.__name__.lower(): CommandStatus
    }
    try:
        return BASE_TYPES[className]
    except KeyError:
        return None
