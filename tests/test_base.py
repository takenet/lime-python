from lime_python import *
import pytest


"""
Test all base classes of lime-python module.

Tests:
    CommandMethod
    CommandStatus
    Command
    Document
    Envelope
    Identity
    MediaType
    Message
    Node
    NotificationEvent
    Notification
"""


def test_commandmethod():

    assert CommandMethod.Get.value == 'get'
    assert CommandMethod.Set.value == 'set'
    assert CommandMethod.Merge.value == 'merge'
    assert CommandMethod.Delete.value == 'delete'
    assert CommandMethod.Subscribe.value == 'subscribe'
    assert CommandMethod.Unsubscribe.value == 'unsubscribe'
    assert CommandMethod.Observe.value == 'observe'


def test_commandstatus():

    assert CommandStatus.Success.value == 'success'
    assert CommandStatus.Failure.value == 'failure'


def test_command():

    expectedJson = {
        "id":  "1",
        "to": "postmaster@broadcast.msging.net",
        "method": "set",
        "uri": "/lists",
        "type": "application/vnd.iris.distribution-list+json",
        "resource": {
            "identity":  "list@broadcast.msging.net"
        }
    }
    cmd = Command('1',
                  to='postmaster@broadcast.msging.net',
                  method=CommandMethod.Set,
                  uri='/lists',
                  mediaType='application/vnd.iris.distribution-list+json',
                  resource=Identity.Parse('list@broadcast.msging.net'))

    assert expectedJson == cmd.ToJson() == \
        Command.FromJson(expectedJson).ToJson() == \
        Command.FromJson(cmd.ToJson()).ToJson()

    expectedJson = {
        "id": "1",
        "from": "postmaster@broadcast.msging.net/#hmgirismsging2",
        "to": "my-contact@msging.net/default",
        "method": "set",
        "status": "success"
    }

    cmd = Command('1',
                  'postmaster@broadcast.msging.net/#hmgirismsging2',
                  'my-contact@msging.net/default',
                  method=CommandMethod.Set,
                  status=CommandStatus.Success)

    assert expectedJson == cmd.ToJson() == \
        Command.FromJson(expectedJson).ToJson() == \
        Command.FromJson(cmd.ToJson()).ToJson()

    expectedJson = {
        "id": "1",
        "from": "postmaster@broadcast.msging.net/#hmgirismsging2",
        "to": "my-contact@msging.net/default",
        "method": "set",
        "status": "failure",
        "reason": {
            "code": 60,
            "description": "Invalid list identifier"
        }
    }

    cmd = Command('1',
                  'postmaster@broadcast.msging.net/#hmgirismsging2',
                  'my-contact@msging.net/default',
                  method=CommandMethod.Set,
                  status=CommandStatus.Failure,
                  reason=Reason(ReasonCode(60), 'Invalid list identifier'))

    assert expectedJson == cmd.ToJson() == \
        Command.FromJson(expectedJson).ToJson() == \
        Command.FromJson(cmd.ToJson()).ToJson()

    expectedJson = {
        "id": "2",
        "to": "postmaster@scheduler.msging.net",
        "method": "set",
        "uri": "/schedules",
        "type": "application/vnd.iris.schedule+json",
        "resource": {
            "message": {
                "id": "ad19adf8-f5ec-4fff-8aeb-2e7ebe9f7a67",
                "to": "553100001111@0mn.io",
                "type": "text/plain",
                "content": "Scheduled Message"
            }
        }
    }

    cmd = Command('2',
                  to='postmaster@scheduler.msging.net',
                  method='set',
                  uri='/schedules',
                  mediaType='application/vnd.iris.schedule+json',
                  resource=Message('ad19adf8-f5ec-4fff-8aeb-2e7ebe9f7a67',
                                   to='553100001111@0mn.io',
                                   content=PlainTextDocument(
                                       'Scheduled Message')))

    assert expectedJson == cmd.ToJson() == \
        Command.FromJson(expectedJson).ToJson() == \
        Command.FromJson(cmd.ToJson()).ToJson()


def test_document():

    expectedJson = {
        'type': 'application/vnd.iris.schedule+json'
    }

    doc = Document('application/vnd.iris.schedule+json')

    assert expectedJson == doc.ToJson() == \
        Document.FromJson(expectedJson).ToJson() == \
        Document.FromJson(doc.ToJson()).ToJson()


def test_envelope():

    expectedJson = {
        'id': '1',
        'to': 'postmaster@scheduler.msging.net'
    }

    env = Envelope('1', to='postmaster@scheduler.msging.net')

    assert expectedJson == env.ToJson() == \
        Envelope.FromJson(expectedJson).ToJson() == \
        Envelope.FromJson(env.ToJson()).ToJson()


def test_identity():

    expected = 'postmaster@scheduler.msging.net'

    iden = Identity.Parse('postmaster@scheduler.msging.net')

    assert expected == str(iden)

    expected = 'gabriel@take.net'

    iden = Identity('gabriel', 'take.net')

    assert expected == str(iden)

    expected = Identity.Parse('lana@take.net')

    iden = Identity('lana', 'take.net')

    other = Identity('lana')

    assert expected == iden
    assert expected != other


def test_mediaType():

    expected = 'text/plain'
    other = MediaType(MediaType.DiscreteTypes.Text, MediaType.SubTypes.Plain)
    another = MediaType('text', 'plain')

    m = MediaType.Parse('text/plain')

    assert expected == str(other) == str(m) == str(another) \
        == str(MediaType.TextPlain)
    assert other == m == MediaType.TextPlain

    other = 'application/vnd.lime.media-link+json'

    m = MediaType(MediaType.DiscreteTypes.Application,
                  'vnd.lime.media-link',
                  MediaType.SubTypes.JSON)

    assert other == str(m)


def test_message():

    expectedJson = {
        "id": "65603604-fe19-479c-c885-3195b196fe8e",
        "from": "551199991111@0mn.io/182310923192",
        "to": "mycontact@msging.net",
        "type": "text/plain",
        "content": "Hello World"
    }

    m = Message('65603604-fe19-479c-c885-3195b196fe8e',
                '551199991111@0mn.io/182310923192',
                'mycontact@msging.net',
                PlainTextDocument('Hello World'))

    assert expectedJson == m.ToJson() == \
        Message.FromJson(expectedJson).ToJson() == \
        Message.FromJson(m.ToJson()).ToJson()

    expectedJson = {
        "id": "123e4567-e89b-12d3-a456-426655440000",
        "to": "551100001111@0mn.io",
        "type": "text/plain",
        "content": "Hello, how can I help you?"
    }

    m = Message("123e4567-e89b-12d3-a456-426655440000",
                to="551100001111@0mn.io",
                content=PlainTextDocument("Hello, how can I help you?"))

    assert expectedJson == m.ToJson() == \
        Message.FromJson(expectedJson).ToJson() == \
        Message.FromJson(m.ToJson()).ToJson()

    expectedJson = {
        "id": "65603604-fe19-479c-c885-3195b196fe8e",
        "from": "551199991111@0mn.io/182310923192",
        "to": "mycontact@msging.net",
        "type": "application/vnd.lime.input+json",
        "content": {
            'label': {
                'type': 'text/plain',
                'value': 'Send me your location now'
            },
            'validation': {
                'rule': 'type',
                'type': 'application/vnd.lime.location+json'
            }
        }
    }

    m = Message("65603604-fe19-479c-c885-3195b196fe8e",
                '551199991111@0mn.io/182310923192',
                "mycontact@msging.net",
                content=InputDocument('Send me your location now',
                                      Validation(Rule.Type,
                                                 LocationDocument.Type)))

    assert expectedJson == m.ToJson() == \
        Message.FromJson(expectedJson).ToJson() == \
        Message.FromJson(m.ToJson()).ToJson()


def test_node():

    expected = 'postmaster@scheduler.msging.net/az'

    iden = Node.Parse('postmaster@scheduler.msging.net/az')

    assert expected == str(iden)

    expected = 'gabriel@take.net/az'

    iden = Node('gabriel', 'take.net', 'az')

    assert expected == str(iden)

    expected = Node.Parse('lana@take.net/az')

    iden = Node('lana', 'take.net', 'az')

    other = Node('lana')

    assert expected == iden
    assert expected != other


def test_notificationevent():

    assert NotificationEvent.Failed.value == 'failed'
    assert NotificationEvent.Accepted.value == 'accepted'
    assert NotificationEvent.Validated.value == 'validated'
    assert NotificationEvent.Authorized.value == 'authorized'
    assert NotificationEvent.Dispatched.value == 'dispatched'
    assert NotificationEvent.Received.value == 'received'
    assert NotificationEvent.Consumed.value == 'consumed'


def test_notification():

    expectedJson = {
        "id": "65603604-fe19-479c-c885-3195b196fe8e",
        "from": "551199991111@0mn.io/182310923192",
        "to": "mycontact@msging.net",
        "event": "received"
    }

    n = Notification('65603604-fe19-479c-c885-3195b196fe8e',
                     'mycontact@msging.net',
                     '551199991111@0mn.io/182310923192',
                     NotificationEvent.Received)

    assert expectedJson == n.ToJson() == \
        Notification.FromJson(expectedJson).ToJson() == \
        Notification.FromJson(n.ToJson()).ToJson()

    expectedJson = {
        "id": "65603604-fe19-479c-c885-3195b196fe8e",
        "from": "postmaster@msging.net/server1",
        "to": "mycontact@msging.net",
        "event": "failed",
        "reason": {
            "code": 42,
            "description": "Destination not found"
        }
    }

    n = Notification('65603604-fe19-479c-c885-3195b196fe8e',
                     'mycontact@msging.net',
                     'postmaster@msging.net/server1',
                     NotificationEvent.Failed,
                     Reason(ReasonCode(42), 'Destination not found'))

    assert expectedJson == n.ToJson() == \
        Notification.FromJson(expectedJson).ToJson() == \
        Notification.FromJson(n.ToJson()).ToJson()
