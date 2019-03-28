from lime_python.utils.paymentItem import PaymentItem
from lime_python.base.mediaType import MediaType
from lime_python.base.document import Document
from datetime import datetime
from functools import reduce


class _PaymentReceiptDocument(Document):

    MIME_TYPE = 'application/vnd.lime.payment-receipt+json'

    def __init__(self, paidOn, code, method, currency, items=[]):
        super().__init__(MediaType.Parse(_PaymentReceiptDocument.MIME_TYPE))

        self.PaidOn = paidOn
        self.Code = code
        self.Method = method
        self.Currency = currency
        self.Items = items

    @property
    def PaidOn(self):
        return self.__PaidOn

    @PaidOn.setter
    def PaidOn(self, paidOn):
        if not isinstance(paidOn, datetime):
            raise ValueError('"PaidOn" must be a datetime')
        self.__PaidOn = paidOn

    @property
    def Code(self):
        return self.__Code

    @Code.setter
    def Code(self, code):
        if not isinstance(code, str):
            raise ValueError('"Code" must be a string')
        self.__Code = code

    @property
    def Method(self):
        return self.__Method

    @Method.setter
    def Method(self, method):
        if isinstance(method, str):
            method = PaymentReceiptDocument.PaymentMethod(method)
        if not isinstance(method, PaymentReceiptDocument.PaymentMethod):
            raise ValueError('"Method" must be a PaymentMethod')
        self.__Method = method

    @property
    def Currency(self):
        return self.__Currency

    @Currency.setter
    def Currency(self, currency):
        if not isinstance(currency, str):
            raise ValueError('"Currency" must be a string')
        self.__Currency = currency

    @property
    def Items(self):
        return self.__Items

    @Items.setter
    def Items(self, items):
        for i in items:
            if not isinstance(i, PaymentItem):
                raise ValueError('"Items" must be a list of PaymentItem')
        self.__Items = items

    def GetMethodJson(self):
        if self.Method is not None:
            return self.Method.ToJson()
        return None

    def GetItemsJson(self):
        return [x.ToJson() for x in self.Items]

    @property
    def Total(self):
        total = reduce((lambda x, y: x.Total + y.Total), self.Items)
        if (isinstance(total, PaymentItem)):
            total = total.Total
        return total

    def ToJson(self):
        return {
            'paidOn': self.PaidOn.strftime('%Y-%m-%dT%H:%M:%SZ'),
            'code': self.Code,
            'method': self.GetMethodJson(),
            'currency': self.Currency,
            'total': self.Total,
            'items': self.GetItemsJson()
        }

    class PaymentMethod:

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


class PaymentReceiptDocument(_PaymentReceiptDocument):

    Type = MediaType.Parse(_PaymentReceiptDocument.MIME_TYPE)
