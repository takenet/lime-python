from datetime import datetime
from lime_python import *
import pytest


"""
Test all document classes of lime-python module.

Tests:
    ChatState
    ChatStateDocument
    CollectionDocument
    ContainerDocument
    InputDocument
    ListDocument
    LocationDocument
    MediaLinkDocument
    MenuDocument
    MultimediaMenuDocument
    PaymentInvoiceDocument
    PaymentReceiptDocument
    PlainTextDocument
    RedirectDocument
    ResourceDocument
    SensitiveInformationDocument
    WebLinkDocument
"""


def test_chatstate():

    assert ChatState.Starting.value == 'starting'
    assert ChatState.Composing.value == 'composing'
    assert ChatState.Paused.value == 'paused'
    assert ChatState.Deleting.value == 'deleting'
    assert ChatState.Gone.value == 'gone'


def test_chatstatedocument():

    expectedJson = {
        'state': 'composing'
    }

    state = ChatStateDocument('composing')

    assert expectedJson == state.ToJson()

    expectedJson = {
        'state': 'paused'
    }

    state = ChatStateDocument(ChatState.Paused)

    assert expectedJson == state.ToJson()

    with pytest.raises(ValueError):
        state = ChatStateDocument('unexpected value')


def test_collectiondocument():

    expectedJson = {
        'itemType': 'text/plain',
        'items': [
            'Text 1',
            'Text 2',
            'Text 3'
        ]
    }

    collection = CollectionDocument(PlainTextDocument.Type, [
        PlainTextDocument('Text 1'),
        PlainTextDocument('Text 2'),
        PlainTextDocument('Text 3')
    ])

    assert expectedJson == collection.ToJson()

    expectedJson = {
        'itemType': 'application/vnd.lime.container+json',
        'items': [
            {
                'type': 'application/vnd.lime.media-link+json',
                'value': {
                    'text': 'Welcome to our store!',
                    'type': 'image/jpeg',
                    'uri': 'http://somesite.com/someimage.jpg'
                }
            },
            {
                'type': 'application/vnd.lime.select+json',
                'value': {
                    'text': 'Choose what you need',
                    'options': [
                        {
                            'order': 1,
                            'text': 'See our stock'
                        },
                        {
                            'order': 2,
                            'text': 'Follow an order'
                        }
                    ]
                }
            }
        ]
    }

    mediaLink = MediaLinkDocument('image/jpeg',
                                  uri='http://somesite.com/someimage.jpg',
                                  text='Welcome to our store!')

    select = MenuDocument(text='Choose what you need',
                          options=[
                              MenuDocument.Option(1, text='See our stock'),
                              MenuDocument.Option(2, text='Follow an order')
                          ])

    collection = CollectionDocument(ContainerDocument.Type,
                                    [
                                        ContainerDocument(mediaLink),
                                        ContainerDocument(select)
                                    ])

    assert expectedJson == collection.ToJson()

    expectedJson = {
        'itemType': 'application/json',
        'items': [
            {
                'key1': 'value1'
            },
            {
                'key1': 'value1',
                'key22': 'value2'
            }
        ]
    }

    collection = CollectionDocument(MediaType.ApplicationJson,
                                    [
                                        {
                                            'key1': 'value1'
                                        },
                                        {
                                            'key1': 'value1',
                                            'key22': 'value2'
                                        }
                                    ])

    assert expectedJson == collection.ToJson()


def test_containerdocument():

    expectedJson = {
        'type': 'application/json',
        'value': {
            'key1': 'value1',
            'key2': 'value2'
        }
    }

    container = ContainerDocument({
        'key1': 'value1',
        'key2': 'value2'
    })

    assert expectedJson == container.ToJson()

    expectedJson = {
        'type': 'text/plain',
        'value': 'there is a house in new orleans'
    }

    container = ContainerDocument(
        PlainTextDocument('there is a house in new orleans'))

    sameContainer = ContainerDocument('there is a house in new orleans')

    assert expectedJson == container.ToJson()


def test_inputdocument():

    expectedJson = {
        'label': {
            'type': 'text/plain',
            'value': 'What is your name?'
        },
        'validation': {
            'rule': 'text'
        }
    }

    inp = InputDocument('What is your name?',
                        Validation('text'))

    assert expectedJson == inp.ToJson()

    expectedJson = {
        'label': {
            'type': 'text/plain',
            'value': 'Send your location please!'
        },
        'validation': {
            'rule': 'type',
            'type': 'application/vnd.lime.location+json'
        }
    }

    inp = InputDocument('Send your location please!',
                        Validation(Rule.Type, LocationDocument.Type))

    assert expectedJson == inp.ToJson()


def test_listdocument():

    expectedJson = {
        'header': {
            'type': 'application/vnd.lime.web-link+json',
            'value': {
                'title': 'Classic T-Shirt Collection',
                'text': 'See all our colors',
                'previewUri': 'http://something.com/arara.png',
                'uri': 'http://something.com',
                'target': 'selfTall'
            }
        },
        'items': [
            {
                'type': 'application/vnd.lime.web-link+json',
                'value': {
                    'title': 'Classic White T-Shirt',
                    'text': '100% Cotton, 200% Comfortable',
                    'previewUri': 'http://something.com/arara.jpg',
                    'uri': 'http://something.com',
                    'target': 'selfTall'
                }
            },
            {
                'type': 'application/vnd.lime.web-link+json',
                'value': {
                    'title': 'Classic Blue T-Shirt',
                    'text': '100% Cotton, 200% Comfortable',
                    'previewUri': 'http://something.com/arara.png',
                    'uri': 'http://something.com',
                    'target': 'selfTall'
                }
            },
            {
                'type': 'application/vnd.lime.web-link+json',
                'value': {
                    'title': 'Classic Black T-Shirt',
                    'text': '100% Cotton, 200% Comfortable',
                    'previewUri': 'http://something.com/arara.png',
                    'uri': 'http://something.com',
                    'target': 'selfTall'
                }
            }
        ]
    }

    header = Header(
        WebLinkDocument(
            'http://something.com',
            'Classic T-Shirt Collection',
            'See all our colors',
            'http://something.com/arara.png',
            Target.SelfTall
        )
    )

    items = [
        WebLinkDocument(
            'http://something.com',
            'Classic White T-Shirt',
            '100% Cotton, 200% Comfortable',
            'http://something.com/arara.jpg',
            Target.SelfTall
        ),
        WebLinkDocument(
            'http://something.com',
            'Classic Blue T-Shirt',
            '100% Cotton, 200% Comfortable',
            'http://something.com/arara.png',
            Target.SelfTall
        ),
        WebLinkDocument(
            'http://something.com',
            'Classic Black T-Shirt',
            '100% Cotton, 200% Comfortable',
            'http://something.com/arara.png',
            Target.SelfTall
        )
    ]

    listD = ListDocument(header, items)

    assert expectedJson == listD.ToJson()


def test_locationdocument():

    expectedJson = {
        "latitude": -19.918899,
        "longitude": -43.959275,
        "altitude": 853,
        "text": "Take's place"
    }

    location = LocationDocument("Take's place",
                                -19.918899,
                                -43.959275,
                                853)

    assert expectedJson == location.ToJson()


def test_medialinkdocument():

    expectedJson = {
        'type': 'audio/mp3',
        'uri': 'http://somesite.com/someaudio.mp3',
        'size': 3124123
    }

    medialink = MediaLinkDocument(MediaType.Parse('audio/mp3'),
                                  '3124123',
                                  uri='http://somesite.com/someaudio.mp3')

    assert expectedJson == medialink.ToJson()

    expectedJson = {
        'title': 'pdf_open_parameters.pdf',
        'uri': 'https://somesite.com/somepdf.pdf',
        'type': 'application/pdf',
        'size': 5540
    }

    medialink = MediaLinkDocument(MediaType.Parse('application/pdf'),
                                  5540,
                                  uri='https://somesite.com/somepdf.pdf',
                                  title='pdf_open_parameters.pdf')

    assert expectedJson == medialink.ToJson()

    expectedJson = {
        'uri': 'http://somesite.com/somegif.gif',
        'type': 'image/gif'
    }

    medialink = MediaLinkDocument(MediaType.Parse('image/gif'),
                                  uri='http://somesite.com/somegif.gif')

    assert expectedJson == medialink.ToJson()

    expectedJson = {
        'title': 'Cat',
        'text': 'Here is a cat image for you!',
        'type': 'image/jpeg',
        'uri': 'http://somesite.com/someimage.jpg',
        'aspectRatio': '1:1',
        'size': 227791.0,
        'previewUri': 'https://somesite.com/someimage',
        'previewType': 'image/jpeg'
    }

    medialink = MediaLinkDocument(MediaType.Parse('image/jpeg'),
                                  227791,
                                  '1:1',
                                  'http://somesite.com/someimage.jpg',
                                  'Cat',
                                  'Here is a cat image for you!',
                                  MediaType.Parse('image/jpeg'),
                                  'https://somesite.com/someimage')

    assert expectedJson == medialink.ToJson()

    expectedJson = {
        'uri': 'http://somesite.com/somevideo.mp4',
        'type': 'video/mp4'
    }

    medialink = MediaLinkDocument(MediaType.Parse('video/mp4'),
                                  uri='http://somesite.com/somevideo.mp4')

    assert expectedJson == medialink.ToJson()


def test_menudocument():

    expectedJson = {
        'scope': 'immediate',
        'text': 'Choose an option',
        'options': [
            {
                'text': 'First option'
            },
            {
                'order': 2,
                'text': 'Second option'
            },
            {
                'order': 3,
                'text': 'Third option',
                'type': 'application/json',
                'value': {
                    'key1': 'value1',
                    'key2': 2
                }
            }
        ]
    }

    menu = MenuDocument(Scope.Immediate,
                        'Choose an option',
                        [
                            MenuDocument.Option(text='First option'),
                            MenuDocument.Option(2,
                                                text='Second option'),
                            MenuDocument.Option(3,
                                                text='Third option',
                                                value={
                                                    'key1': 'value1',
                                                    'key2': 2
                                                })
                        ])

    assert expectedJson == menu.ToJson()

    expectedJson = {
        'text': 'Do you wanna cook crystal meth?',
        'options': [
            {
                'order': 1,
                'text': 'yes'
            },
            {
                'order': 2,
                'text': 'no',
                'type': 'text/plain',
                'value': 'call 911'
            }
        ]
    }

    menu = MenuDocument(text='Do you wanna cook crystal meth?',
                        options=[
                            MenuDocument.Option(1, text='yes'),
                            MenuDocument.Option(2,
                                                PlainTextDocument('call 911'),
                                                'no')
                        ])

    assert expectedJson == menu.ToJson()


def test_multimediamenudocument():

    expectedJson = {
        'header': {
            'type': 'application/vnd.lime.media-link+json',
            'value': {
                'title': 'Welcome to mad hatter',
                'text': 'Here we have the best hats for your head.',
                'type': 'image/jpeg',
                'uri': 'http://somesite.com/somepic.png',
                'aspectRatio': '1:1'
            }
        },
        'options': [
            {
                'label': {
                    'type': 'application/vnd.lime.web-link+json',
                    'value': {
                        'text': 'Go to our site',
                        'uri': 'https://somesite.com'
                    }
                }
            },
            {
                'label': {
                    'type': 'text/plain',
                    'value': 'Show stock'
                },
                'value': {
                    'type': 'application/json',
                    'value': {
                        'action': 'show-items'
                    }
                }
            }
        ]
    }

    header = Header(
        MediaLinkDocument(
            'image/jpeg',
            aspectRatio='1:1',
            uri='http://somesite.com/somepic.png',
            title='Welcome to mad hatter',
            text='Here we have the best hats for your head.'
        )
    )

    option1 = MultimediaMenuDocument.Option(
        label=WebLinkDocument(
            'https://somesite.com',
            text='Go to our site'
        )
    )

    option2 = MultimediaMenuDocument.Option(
        label='Show stock',
        value={
            'action': 'show-items'
        }
    )

    multimenu = MultimediaMenuDocument(
        header=header,
        options=[
            option1,
            option2
        ]
    )

    assert expectedJson == multimenu.ToJson()

    expectedJson = {
        'itemType': 'application/vnd.lime.document-select+json',
        'items': [
            {
                'header': {
                    'type': 'application/vnd.lime.media-link+json',
                    'value': {
                        'title': 'Title',
                        'text': 'This is a first item',
                        'type': 'image/jpeg',
                        'uri': 'http://somesite.com/someimage.jpg'
                    }
                },
                'options': [
                    {
                        'label': {
                            'type': 'application/vnd.lime.web-link+json',
                            'value': {
                                'title': 'Link',
                                'uri': 'http://somesite.com'
                            }
                        }
                    },
                    {
                        'label': {
                            'type': 'text/plain',
                            'value': 'Text 1'
                        },
                        'value': {
                            'type': 'application/json',
                            'value': {
                                'key1': 'value1',
                                'key2': '2'
                            }
                        }
                    }
                ]
            },
            {
                'header': {
                    'type': 'application/vnd.lime.media-link+json',
                    'value': {
                        'title': 'Title 2',
                        'text': 'This is another item',
                        'type': 'image/jpeg',
                        'uri': 'http://somesite.com/someimage.jpg'
                    }
                },
                'options': [
                    {
                        'label': {
                            'type': 'application/vnd.lime.web-link+json',
                            'value': {
                                'title': 'Second link',
                                'text': 'Weblink',
                                'uri': 'http://somesite.com'
                            }
                        }
                    },
                    {
                        'label': {
                            'type': 'text/plain',
                            'value': 'Second text'
                        },
                        'value': {
                            'type': 'application/json',
                            'value': {
                                'key3': 'value3',
                                'key4': '4'
                            }
                        }
                    },
                    {
                        'label': {
                            'type': 'text/plain',
                            'value': 'More one text'
                        },
                        'value': {
                            'type': 'application/json',
                            'value': {
                                'key5': 'value5',
                                'key6': '6'
                            }
                        }
                    }
                ]
            }
        ]
    }

    header = Header(
        MediaLinkDocument(
            'image/jpeg',
            title='Title',
            text='This is a first item',
            uri='http://somesite.com/someimage.jpg'
        )
    )

    options = [
        MultimediaMenuDocument.Option(
            label=WebLinkDocument(
                'http://somesite.com',
                'Link'
            )
        ),
        MultimediaMenuDocument.Option(
            label='Text 1',
            value={
                'key1': 'value1',
                'key2': '2'
            }
        )
    ]

    multimenu1 = MultimediaMenuDocument(header=header, options=options)

    header = MediaLinkDocument(
        'image/jpeg',
        title='Title 2',
        text='This is another item',
        uri='http://somesite.com/someimage.jpg'
    )

    options = [
        MultimediaMenuDocument.Option(
            label=WebLinkDocument(
                'http://somesite.com',
                'Second link',
                'Weblink'
            )
        ),
        MultimediaMenuDocument.Option(
            label='Second text',
            value={
                'key3': 'value3',
                'key4': '4'
            }
        ),
        MultimediaMenuDocument.Option(
            label='More one text',
            value={
                'key5': 'value5',
                'key6': '6'
            }
        )
    ]

    multimenu2 = MultimediaMenuDocument(header=header, options=options)

    collection = CollectionDocument(
        MultimediaMenuDocument.Type,
        [
            multimenu1,
            multimenu2
        ]
    )

    assert expectedJson == collection.ToJson()


def test_paymentinvoicedocument():

    now = datetime.now()

    expectedJson = {
        'created': now.strftime('%Y-%m-%dT%H:%M:%SZ'),
        'dueTo': '2016-08-27T19:03:37Z',
        'currency': 'BRL',
        'total': 10.85,
        'items': [
            {
                'quantity': 1.0,
                'unit': 10.85,
                'currency': 'BRL',
                'total': 10.85,
                'description': 'Subscription for product: Hit'
            }
        ]
    }

    payment = PaymentInvoiceDocument(
        'BRL',
        datetime(2016, 8, 27, 19, 3, 37, 24),
        [
            PaymentItem(
                1,
                10.85,
                'BRL',
                'Subscription for product: Hit'
            )
        ]
    )

    given = payment.ToJson()

    given['created'] = now.strftime('%Y-%m-%dT%H:%M:%SZ')

    assert expectedJson == given


def test_paymentreceiptdocument():

    expectedJson = {
        'paidOn': '2016-08-26T19:03:37Z',
        'code': '215BF6B5-01EF-4F9A-A944-0BC05FD0F228',
        'method': {
                'name': 'Credit Card'
        },
        'currency': 'BRL',
        'total': 10.85,
        'items': [{
            'quantity': 1.0,
            'unit': 10.85,
            'currency': 'BRL',
            'total': 10.85,
            'description': 'Item 1'
        }
        ]
    }

    payment = PaymentReceiptDocument(
        datetime(2016, 8, 26, 19, 3, 37),
        '215BF6B5-01EF-4F9A-A944-0BC05FD0F228',
        'Credit Card',
        'BRL',
        [
            PaymentItem(
                1,
                10.85,
                'BRL',
                'Item 1'
            )
        ]
    )

    assert expectedJson == payment.ToJson()


def test_plaintextdocument():

    expectedJson = 'Welcome to our service! How can I help you?'

    pt = PlainTextDocument('Welcome to our service! How can I help you?')

    assert expectedJson == pt.ToJson()


def test_redirectdocument():

    expectedJson = {
        'address': 'attendance'
    }

    redirect = RedirectDocument('attendance')

    assert expectedJson == redirect.ToJson()

    expectedJson = {
        'address': 'mysdkbot@msging.net',
        'context': {
            'type': 'text/plain',
            'value': 'Get started'
        }
    }

    redirect = RedirectDocument(
        Node.Parse('mysdkbot@msging.net'),
        'Get started'
    )

    assert expectedJson == redirect.ToJson()


def test_resourcedocument():

    expectedJson = {
        'key': 'welcome-message'
    }

    resource = ResourceDocument('welcome-message')

    assert expectedJson == resource.ToJson()

    expectedJson = {
        'key': 'welcome-message',
        'variables': {
            'name': 'John Doe'
        }
    }

    resource = ResourceDocument('welcome-message',
                                {
                                    'name': 'John Doe'
                                })

    assert expectedJson == resource.ToJson()


def test_sensitiveinformationdocument():

    expectedJson = {
        'type': 'text/plain',
        'value': 'Your password is 123456'
    }

    si = SensitiveInformationDocument(
        PlainTextDocument('Your password is 123456')
    )

    sameSI = SensitiveInformationDocument('Your password is 123456')

    assert expectedJson == si.ToJson() == sameSI.ToJson()

    expectedJson = {
        'type': 'application/vnd.lime.web-link+json',
        'value': {
            'text': 'Please follow this link for the checkout',
            'uri': 'https://somelink.com'
        }
    }

    si = SensitiveInformationDocument(
        WebLinkDocument(
            'https://somelink.com',
            text='Please follow this link for the checkout'
        )
    )

    assert expectedJson == si.ToJson()


def test_weblinkdocument():

    expectedJson = {
        'uri': 'http://limeprotocol.org/content-types.html#web-link',
        'target': 'self',
        'text': 'Here is a documentation weblink'
    }

    weblink = WebLinkDocument(
        'http://limeprotocol.org/content-types.html#web-link',
        text='Here is a documentation weblink',
        target='self'
    )

    assert expectedJson == weblink.ToJson()

    expectedJson = {
        'uri': 'http://somesite.com',
        'target': 'selfTall',
        'text': 'Second link',
        'title': 'Weblink',
        'previewUri': 'http://somesite.com/preview.jpg'
    }

    weblink = WebLinkDocument(
        'http://somesite.com',
        'Weblink',
        'Second link',
        'http://somesite.com/preview.jpg',
        Target.SelfTall
    )

    assert expectedJson == weblink.ToJson()
