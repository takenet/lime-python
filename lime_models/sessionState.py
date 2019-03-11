from enum import Enum


class SessionState(Enum):
    New = 'new'
    Negotiating = 'negotiating'
    Authenticating = 'authenticating'
    Established = 'established'
    Finishing = 'finishing'
    Finished = 'finished'
    Failed = 'failed'
