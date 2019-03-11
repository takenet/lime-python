class Reason:

    def __init__(self, code=None, description=None):
        self.Code = code  # Int
        self.Description = description  # String

    def __str__(self):
        return '%s (Code %d)' % (self.Description, self.Code)
