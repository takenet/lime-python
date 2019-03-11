from ..reason import Reason


class LimeException(Exception):

    def __init__(self, reason, innerException=None, reasonDescription=None):
        if reasonDescription is not None:
            reason = Reason(reason, reasonDescription)
        self.Reason = reason
        super().__init__(reason, innerException)
