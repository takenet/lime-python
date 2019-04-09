class PaymentMethod:
    """
    Representation of a payment method

    Parameters:
        name (str)
    """

    def __init__(self, name):
        self.Name = name

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, name):
        if not isinstance(name, str):
            raise ValueError('"Name" must be a string')
        self.__Name = name

    def ToJson(self):
        return {
            'name': self.Name
        }

    @staticmethod
    def FromJson(inJson):
        if isinstance(inJson, str):
            inJson = json.loads(inJson)
        try:
            return PaymentMethod(inJson['name'])
        except KeyError:
            raise ValueError(
                'The given json is not a PaymentMethod')
