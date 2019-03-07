class Reason:

    def __init__(self):
        self.Code = None  # Int
        self.Description = None  # String

    def __str__(self):
        return '%s (Code %d)' % (self.Description, self.Code)
