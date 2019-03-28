from enum import Enum


class Scope(Enum):
    """
    Enum of the available menu scopes

    Value:
        Transient (str)
        Persistent (str)
        Immediate (str)
    """
    Transient = 'transient'
    Persistent = 'persistent'
    Immediate = 'immediate'
