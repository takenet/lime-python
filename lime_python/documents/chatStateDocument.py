from lime_python.base.document import Document
from lime_python.base.mediaType import MediaType
from enum import Enum


class ChatState(Enum):
    """
    Enum of the available chat states

    Values:
        Starting (str)
        Composing (str)
        Paused (str)
        Deleting (str)
        Gone (str)
    """

    Starting = 'starting'
    Composing = 'composing'
    Paused = 'paused'
    Deleting = 'deleting'
    Gone = 'gone'


class _ChatStateDocument(Document):

    MIME_TYPE = 'application/vnd.lime.chatstate+json'

    def __init__(self, chatState=None):
        super().__init__(MediaType.Parse(_ChatStateDocument.MIME_TYPE))
        self.State = chatState

    @property
    def State(self):
        return self.__State

    @State.setter
    def State(self, chatState):
        if isinstance(chatState, str):
            chatState = ChatState(chatState)
        if chatState is not None and not isinstance(chatState, ChatState):
            raise ValueError(
                '"ChatState" must be a ChatState Model')
        self.__State = chatState

    def ToJson(self):
        return {
            'state': self.State.value
        }


class ChatStateDocument(_ChatStateDocument):
    """
    Representation of a LIME chat state Document

    Parameters:
        chatState (ChatState or str)
    """

    Type = MediaType.Parse(_ChatStateDocument.MIME_TYPE)
