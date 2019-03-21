from lime_python.base.mediaType import MediaType
from lime_python.base.document import Document
from datetime import datetime
from functools import reduce


class _PaymentInvoiceDocument(Document):

    MIME_TYPE = 'application/vnd.lime.invoice+json'

    def __init__(self, currency, dueTo, items=[]):
        super().__init__(MediaType.Parse(_PaymentInvoiceDocument.MIME_TYPE))

        self.Items = items
        self.DueTo = dueTo
        self.Currency = currency
        self.__Created = datetime.now()

    @property
    def Items(self):
        return self.__Items

    @Items.setter
    def Items(self, items):
        for i in items:
            if not isinstance(i, _PaymentInvoiceDocument.Item):
                raise ValueError('"Items" must be a list of Item')
        self.__Items = items

    @property
    def DueTo(self):
        return self.__DueTo

    @DueTo.setter
    def DueTo(self, dueTo):
        if not isinstance(dueTo, datetime):
            raise ValueError('"DueTo" must be a datetime')
        self.__DueTo = dueTo

    @property
    def Currency(self):
        return self.__Currency

    @Currency.setter
    def Currency(self, currency):
        if not isinstance(currency, str):
            raise ValueError('"Currency" must be a string')
        self.__Currency = currency

    @property
    def Total(self):
        total = reduce((lambda x, y: x.Total + y.Total), self.Items)
        if (isinstance(total, _PaymentInvoiceDocument.Item)):
            total = total.Total
        return total

    def GetItemsJson(self):
        return [x.ToJson() for x in self.Items]

    def ToJson(self):
        return {
            'created': self.__Created.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'dueTo': self.DueTo.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'currency': self.Currency,
            'total': self.Total,
            'items': self.GetItemsJson()
        }

    class Item:

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


class PaymentInvoiceDocument(_PaymentInvoiceDocument):

    Type = MediaType.Parse(_PaymentInvoiceDocument.MIME_TYPE)
