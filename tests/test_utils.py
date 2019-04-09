from lime_python import *
import pytest


"""
Test all util classes of lime-python module.

Tests:
    Header
    LimeException
    PaymentItem
    ReasonCode
    Reason
    Scope
    StringUtils
"""


def test_header():

    expectedJson = {
        'type': 'text/plain',
        'value': 'keep me alive'
    }

    header = Header(PlainTextDocument('keep me alive'))

    assert expectedJson == header.ToJson()

    expectedJson = {
        'type': 'application/vnd.lime.web-link+json',
        'value': {
            'uri': 'http://take.net',
            'title': 'take',
            'text': 'take'
        }
    }

    header = Header(WebLinkDocument('http://take.net', 'take', 'take'))

    assert expectedJson == header.ToJson() == \
        Header.FromJson(expectedJson).ToJson() == \
        Header.FromJson(header.ToJson()).ToJson()


def test_limeexception():

    limeException = LimeException()

    assert isinstance(limeException, Exception)

    limeException = LimeException('Error message')

    assert isinstance(limeException, Exception)


def test_paymentitem():

    expectedJson = {
        'quantity': 3.0,
        'unit': 3.0,
        'currency': 'BRL',
        'description': 'bolsa',
        'total': 9.0
    }

    item = PaymentItem(3, 3, 'BRL', 'bolsa')

    assert expectedJson == item.ToJson() == \
        PaymentItem.FromJson(expectedJson).ToJson() == \
        PaymentItem.FromJson(item.ToJson()).ToJson()

    expectedJson = {
        'quantity': 1.0,
        'unit': 10.85,
        'currency': 'BRL',
        'description': 'açai 500ml',
        'total': 10.85
    }

    item = PaymentItem(1, 10.85, 'BRL', 'açai 500ml')

    assert expectedJson == item.ToJson() == \
        PaymentItem.FromJson(expectedJson).ToJson() == \
        PaymentItem.FromJson(item.ToJson()).ToJson()


def test_paymentmethod():
    expectedJson = {
        'name': 'credit card'
    }

    method = PaymentMethod('credit card')

    assert expectedJson == method.ToJson() == \
        PaymentMethod.FromJson(expectedJson).ToJson() == \
        PaymentMethod.FromJson(method.ToJson()).ToJson()

    expectedJson = {
        'name': 'money'
    }

    method = PaymentMethod('money')

    assert expectedJson == method.ToJson() == \
        PaymentMethod.FromJson(expectedJson).ToJson() == \
        PaymentMethod.FromJson(method.ToJson()).ToJson()


def test_reasoncode():

    assert ReasonCode.GENERAL_ERROR.value == 1
    assert ReasonCode.SESSION_ERROR.value == 11
    assert ReasonCode.SESSION_REGISTRATION_ERROR.value == 12
    assert ReasonCode.SESSION_AUTHENTICATION_FAILED.value == 13
    assert ReasonCode.SESSION_UNREGISTER_FAILED.value == 14
    assert ReasonCode.SESSION_INVALID_ACTION_FOR_STATE.value == 15
    assert ReasonCode.SESSION_NEGOTIATION_TIMEOUT.value == 16
    assert ReasonCode.SESSION_NEGOTIATION_INVALID_OPTIONS.value == 17
    assert ReasonCode.SESSION_INVALID_SESSION_MODE_REQUESTED.value == 18
    assert ReasonCode.VALIDATION_ERROR.value == 21
    assert ReasonCode.VALIDATION_EMPTY_DOCUMENT.value == 22
    assert ReasonCode.VALIDATION_INVALID_RESOURCE.value == 23
    assert ReasonCode.VALIDATION_INVALID_STATUS.value == 24
    assert ReasonCode.VALIDATION_INVALID_IDENTITY.value == 25
    assert ReasonCode.VALIDATION_INVALID_RECIPIENTS.value == 26
    assert ReasonCode.VALIDATION_INVALID_METHOD.value == 27
    assert ReasonCode.VALIDATION_INVALID_URI.value == 27
    assert ReasonCode.AUTHORIZATION_ERROR.value == 31
    assert ReasonCode.AUTHORIZATION_UNAUTHORIZED_SENDER.value == 32
    assert ReasonCode.AUTHORIZATION_DESTINATION_ACCOUNT_NOT_FOUND.value == 33
    assert ReasonCode.AUTHORIZATION_QUOTA_THRESHOLD_EXCEEDED.value == 34
    assert ReasonCode.AUTHORIZATION_PERMISSION_REQUIRED.value == 35
    assert ReasonCode.ROUTING_ERROR.value == 41
    assert ReasonCode.ROUTING_DESTINATION_NOT_FOUND.value == 42
    assert ReasonCode.ROUTING_GATEWAY_NOT_FOUND.value == 43
    assert ReasonCode.ROUTING_ROUTE_NOT_FOUND.value == 44
    assert ReasonCode.DISPATCH_ERROR.value == 51
    assert ReasonCode.COMMAND_PROCESSING_ERROR.value == 61
    assert ReasonCode.COMMAND_RESOURCE_NOT_SUPPORTED.value == 62
    assert ReasonCode.COMMAND_METHOD_NOT_SUPPORTED.value == 63
    assert ReasonCode.COMMAND_INVALID_ARGUMENT.value == 64
    assert ReasonCode.COMMAND_INVALID_SESSION_MODE.value == 65
    assert ReasonCode.COMMAND_NOT_ALLOWED.value == 66
    assert ReasonCode.COMMAND_RESOURCE_NOT_FOUND.value == 67
    assert ReasonCode.MESSAGE_PROCESSING_ERROR.value == 61
    assert ReasonCode.MESSAGE_UNSUPPORTED_CONTENT_TYPE.value == 71
    assert ReasonCode.GATEWAY_ERROR.value == 81
    assert ReasonCode.GATEWAY_CONTENT_TYPE_NOT_SUPPORTED.value == 82
    assert ReasonCode.GATEWAY_DESTINATION_NOT_FOUND.value == 83
    assert ReasonCode.GATEWAY_NOT_SUPPORTED.value == 84
    assert ReasonCode.GATEWAY_REQUEST_LIMIT_REACHED.value == 85
    assert ReasonCode.GATEWAY_OPERATION_TIMED_OUT.value == 86
    assert ReasonCode.GATEWAY_UNAUTHORIZED_SENDER.value == 87
    assert ReasonCode.APPLICATION_ERROR.value == 101
    assert ReasonCode.INVALID_LIST_IDENTIFIER.value == 60


def test_reason():

    expectedJson = {
        'code': 1,
        'description': 'ocorreu um erro'
    }

    reason = Reason(ReasonCode.GENERAL_ERROR, 'ocorreu um erro')

    assert expectedJson == reason.ToJson() == \
        Reason.FromJson(expectedJson).ToJson() == \
        Reason.FromJson(reason.ToJson()).ToJson()

    expectedJson = {
        'code': 11,
        'description': 'erro na sessão'
    }

    reason = Reason(ReasonCode.SESSION_ERROR, 'erro na sessão')

    assert expectedJson == reason.ToJson() == \
        Reason.FromJson(expectedJson).ToJson() == \
        Reason.FromJson(reason.ToJson()).ToJson()


def test_scope():

    assert Scope.Transient.value == 'transient'
    assert Scope.Persistent.value == 'persistent'
    assert Scope.Immediate.value == 'immediate'


def test_stringutils():

    assert StringUtils.IsNoneOrEmpty(None) is True
    assert StringUtils.IsNoneOrEmpty('') is True
    assert StringUtils.IsNoneOrEmpty(' ') is True
    assert StringUtils.IsNoneOrEmpty('something') is False
