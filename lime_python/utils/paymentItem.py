class PaymentItem:

    def __init__(self, quantity, unit, currency, description):
        self.Quantity = quantity
        self.Unit = unit
        self.Currency = currency
        self.Description = description

    @property
    def Quantity(self):
        return self.__Quantity

    @Quantity.setter
    def Quantity(self, quantity):
        try:
            quantity = float(quantity)
            self.__Quantity = quantity
        except:
            raise ValueError('"Quantity" must be a float')

    @property
    def Unit(self):
        return self.__Unit

    @Unit.setter
    def Unit(self, unit):
        try:
            unit = float(unit)
            self.__Unit = unit
        except:
            raise ValueError('"Unit" must be a float')

    @property
    def Currency(self):
        return self.__Currency

    @Currency.setter
    def Currency(self, currency):
        if not isinstance(currency, str):
            raise ValueError('"Currency" must be a string')
        self.__Currency = currency

    @property
    def Description(self):
        return self.__Description

    @Description.setter
    def Description(self, description):
        if not isinstance(description, str):
            raise ValueError('"Description" must be a string')
        self.__Description = description

    @property
    def Total(self):
        return self.Quantity * self.Unit

    def ToJson(self):
        return {
            'quantity': self.Quantity,
            'unit': self.Unit,
            'currency': self.Currency,
            'total': self.Total,
            'description': self.Description
        }
