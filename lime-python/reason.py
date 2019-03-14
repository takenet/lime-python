from reasonCode import ReasonCode


class Reason:

    def __init__(self, code=None, description=None):
        self.Code = code
        self.Description = description

    @property
    def Code(self):
        return self.__Code

    @Code.setter
    def Code(self, code):
        if code is not None and not isinstance(code, ReasonCode):
            raise ValueError('"Code" must be a ReasonCode')
        self.__Code = code

    @property
    def Description(self):
        return self.__Description

    @Description.setter
    def Description(self, description):
        if description is not None and not isinstance(description, str):
            raise ValueError('"Description" must be a string')
        self.__Description = description

    def __str__(self):
        return '%s (Code %d)' % (self.Description, self.Code)

    def __repr__(self):
        return str(self)

    def ToJson(self):
        return {
            'code': self.Code,
            'description': self.Description
        }
