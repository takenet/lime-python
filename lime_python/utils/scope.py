from enum import Enum


class Scope(Enum):
    Transient = 'transient'
    Persistent = 'persistent'
    Immediate = 'immediate'
