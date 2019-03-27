# Documentation

- [Base](#Base)
  - [MediaType](#MediaType)
    - [DiscreteTypes](#DiscreteTypes)
    - [CompositeTypes](#CompositeTypes)
    - [SubTypes](#SubTypes)
  - [Identity](#Identity)
  - [Node](#Node)
  - [Envelope](#Envelope)
  - [Document](#Document)
  - [Command](#Command)
    - [CommandMethod](#CommandMethod)
    - [CommandStatus](#CommandStatus)
  - [Message](#Message)
  - [Notification](#Notification)
    - [NotificationEvent](#NotificationEvent)
- [Documents](#Documents)
  - [Chat State](#Chat%20State)
    - [ChatState](#ChatState)
  - [Plain Text](#Plain%20Text)
  - [Location](#Location)
  - [Input](#Input)
    - [Rule](#Rule)
    - [Validation](#Validation)
  - [Media Link](#Media%20Link)
  - [Web Link](#Web%20Link)
    - [Target](#Target)
  - [Menu](#Menu)
  - [Multimedia Menu](#Multimedia%20Menu)  
  - [Sensitive Information](#Sensitive%20Information)
  - [Resource](#Resource)
  - [Redirect](#Redirect)
  - [Payment Invoice](#Payment%20Invoice)
  - [Payement Receipt](#Payment%20Receipt)
  - [List](#List)
  - [Container](#Container)
  - [Collection](#Collection)
- [Utils](#Utils)
  - [Header](#Header)
  - [Lime Exception](#Lime%20Exception)
  - [Reason Code](#Reason%20Code)
  - [Reason](#Reason)
  - [Scope](#Scope)

# Base

## MediaType

`MediaType` have 3 subclasses, `DiscreteTypes`, `CompositeTypes` and `SubTypes` that can be used to create a new `MediaType`.

You can also use the `MediaType.Parse(string)` method to parse a string into a new `MediaType`.

### Class Information

#### DiscreteTypes

| Property    | Type     |
| ----------- | -------- |
| Application | `string` |
| Text        | `string` |
| Image       | `string` |
| Audio       | `string` |
| Video       | `string` |

#### CompositeTypes

| Property  | Type     |
| --------- | -------- |
| Message   | `string` |
| Multipart | `string` |

#### SubTypes

| Property   | Type     |
| ---------- | -------- |
| Plain      | `string` |
| JSON       | `string` |
| XML        | `string` |
| HTML       | `string` |
| Jpeg       | `string` |
| Bitmap     | `string` |
| Javascript | `string` |

#### MediaType

| Property        | Type        |
| --------------- | ----------- |
| Type            | `string`    |
| SubType         | `string`    |
| Suffix          | `string`    |
| TextPlain       | `MediaType` |
| ApplicationJson | `MediaType` |

### Usage

```python
from lime_python import MediaType

TextPlain = MediaType(DiscreteTypes.Text, SubTypes.Plain)
CollectionType = MediaType.Parse('application/vnd.lime.collection+json')
```

---

## Identity

### Class Information

| Property | Type     |
| -------- | -------- |
| Name     | `string` |
| Domain   | `string` |

### Usage

```python
from lime_python import Identity

identity = Identity('gabriel', 'take')
sameIdentity = Identity.Parse('gabriel@take')
```

---

## Node

### Class Information

| Property | Type     |
| -------- | -------- |
| Name     | `string` |
| Domain   | `string` |
| Instance | `string` |

### Usage

```python
from lime_python import Node

node = Node('gabriel', 'take', 'lime')
sameNode = Node.Parse('gabriel@take/lime')
```

## Envelope

### Class Information

| Property | Type     |
| -------- | -------- |
| Id       | `string` |
| From     | `Node`   |
| To       | `Node`   |

### Usage

```python
from lime_python import Envelope, Node

envelope = Envelope(fromN=Node.Parse('gabriel@take'), to=Node.Parse('lime'))
otherEnvelope = Envelope('some-guid-uuid', to='gabriel@take')
```

---

## Documents

This is the base for all lime documents. Every class that implements `Document`must have `ToJson()` method.

### Class Information

| Property  | Type        |
| --------- | ----------- |
| MediaType | `MediaType` |

### Usage

```python
from lime_python import Document, MediaType

# Normal use
document = Document(MediaType.ApplicationJson)

# OR

# Creating a new lime Document
class SomeNewDocument(Document):

    def __init__(self, mediaType, info):
        super().__init__(mediaType)
        self.Info = info

    def ToJson(self):
        return {
            'info' : self.Info
        }
```

---

## Command

Commands may have methods (`CommandMethod`) and/or status (`CommandStatus`).

### Class Information

#### CommandMethod

| Enum        |
| ----------- |
| Get         |
| Set         |
| Delete      |
| Subscribe   |
| Unsubscribe |
| Observe     |
| Merge       |

#### CommandStatus

| Enum    |
| ------- |
| Pending |
| Success |
| Failure |

#### Command

| Property | Type            |
| -------- | --------------- |
| Id       | `string`        |
| From     | `Node`          |
| To       | `Node`          |
| Uri      | `string`        |
| Resource | `Document`      |
| Method   | `CommandMethod` |
| Status   | `Status`        |
| Reason   | `Reason`        |

### Usage

```python
from lime_python import Command, CommandMethod, Node

command = Command(to=Node('gabriel'), uri='/intentions', method=CommandMethod.Get)
```

---

## Message

### Class Information

| Property | Type       |
| -------- | ---------- |
| Id       | `string`   |
| From     | `string`   |
| To       | `string`   |
| Content  | `Document` |

### Usage

```python
from lime_python import Message, PlainTextDocument, Node

message = Message(to='gabriel@take', content=PlainTextDocument('So far away'))

otherMessage = Message(to=Node('gabriel'), content={'dire': 'straits'})
```

---

## Notification

Notifications may have events (`NotificationEvent`).

### Class Informations

#### NotificationEvent

| Enum       |
| ---------- |
| Failed     |
| Accepted   |
| Validated  |
| Authorized |
| Dispatched |
| Received   |
| Consumed   |

#### Notification

| Property | Type                |
| -------- | ------------------- |
| Id       | `string`            |
| To       | `Node`              |
| From     | `Node`              |
| event    | `NotificationEvent` |
| Reason   | `Reason`            |

### Usage

```python
from lime_python import Notification, NotificationEvent, Reason, ReasonCode

notification = Notification(to='gabriel@take')
```

---

# Documents

All documents implements `ToJson()` method that returns a `dictionary` representing the document itself and `Type` property that holds the document's `MediaType`.

## Chat State

To create a `ChatStateDocument` you need to pass a `ChatState`.

### Class Information

#### ChatState

| Enum      |
| --------- |
| Starting  |
| Composing |
| Paused    |
| Deleting  |
| Gone      |

#### ChatStateDocument

| Property  | Type        |
| --------- | ----------- |
| State     | `ChatState` |
| MIME_TYPE | `string`    |
| Type      | `MediaType` |

### Usage

```python
from lime_python import ChatStateDocument, ChatState

state = ChatStateDocument(ChatState.Composing)
```

---

## Plain Text

### Class Information

| Property | Type        |
| -------- | ----------- |
| Value    | `string`    |
| Type     | `MediaType` |

### Usage

```python
from lime_python import PlainTextDocument

plainText = PlainTextDocument('Welcome to our service! How can I help you?')
```

---

## Location

### Class Information

| Property  | Type        |
| --------- | ----------- |
| Text      | `string`    |
| Latitude  | `float`     |
| Longitude | `float`     |
| Altitude  | `float`     |
| MIME_TYPE | `string`    |
| Type      | `MediaType` |

### Usage

```python
from lime_python import LocationDocument

location = LocationDocument("Take's place", -19.939132, -43.938741, 906)
```

---

## Input

To create a `InputDocument` you need to pass the `Validation`.
To create a `Validation` you need to pass the `Rule`, in case of `Rule.Type` the `Validation.MediaType` need to be passed.

### Class Information

#### Rule

| Enum |
| ---- |
| Type |
| Text |

#### Validation

| Property  | Type        |
| --------- | ----------- |
| MediaType | `MediaType` |
| Rule      | `Rule`      |

#### InputDocument

| Property   | Type                |
| ---------- | ------------------- |
| Label      | `PlainTextDocument` |
| Validation | `Validation`        |
| MIME_TYPE  | `string`            |
| Type       | `MediaType`         |

### Usage

```python
from lime_python import InputDocument, Validation, Rule, LocationDocument

# Text Input
inputText = InputDocument('What is your name?', Validation(Rule.Text))

# Location Input
i = InputDocument("send me your location let's, focus on communication", Validation(Rule.Type, LocationDocument.Type))
```

---

## Media Link

### Class Information

| Property    | Type        |
| ----------- | ----------- |
| MimeType    | `MediaType` |
| Size        | `float`     |
| AspectRatio | `string`    |
| Uri         | `string`    |
| Title       | `string`    |
| Text        | `string`    |
| PreviewType | `MediaType` |
| PreviewUri  | `string`    |
| MIME_TYPE   | `string`    |
| Type        | `MediaType` |

### Usage

```python
from lime_python import MediaLinkDocument, MediaType

# Audio
audio = MediaLinkDocument(MediaType.Parse('audio/mp3'),
                          '3124123',
                          uri='http://blaamandagjazzband.dk/jazz/mp3/basin_street_blues.mp3')

# Document/Files
doc = MediaLinkDocument(MediaType.Parse('application/pdf'),
                        5540,
                        uri='https://gradcollege.okstate.edu/sites/default/files/PDF_linking.pdf',
                        title='pdf_open_parameters.pdf')

# Gif
gif = MediaLinkDocument(MediaType.Parse('image/gif'),
                        uri='http://i.giphy.com/14aUO0Mf7dWDXW.gif')

# Images
image = MediaLinkDocument(MediaType.Parse('image/jpeg'),
                          227791,
                          "1:1",
                          'http://2.bp.blogspot.com/-pATX0YgNSFs/VP-82AQKcuI/AAAAAAAALSU/Vet9e7Qsjjw/s1600/Cat-hd-wallpapers.jpg',
                          'Cat',
                          'Here is a cat image for you',
                          MediaType.Parse('image/jpeg'),
                          'https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcS8qkelB28RstsNxLi7gbrwCLsBVmobPjb5IrwKJSuqSnGX4IzX')

# Video
video = MediaLinkDocument(MediaType.Parse('video/mp4'),
                          uri='http://techslides.com/demos/sample-videos/small.mp4')
```
---

# Utils

## Header

### Class Informations

| Property | Type       |
| -------- | ---------- |
| Value    | `Document` |

### Usage

```python
from lime_python import Header, PlainTextDocument

header = Header(PlainTextDocument('The lunatic is on the grass'))
```

---

## Lime Exception

### Class Informations

This class only implements `Exception`.

### Usage

```python
from lime_python import LimeException

raise LimeException('Some exception involving lime occurred')
```
---

## Reason Code

### Class Informations

| Enum                                |
| ----------------------------------- |
| GENERAL_ERROR                       |
| SESSION_ERROR                       |
| SESSION_REGISTRATION_ERROR          |
| SESSION_AUTHENTICATION_FAILED       |
| ...                                 |
| [Complete List](/docs/REASON%20CODES.md) |

### Usage

```python
from lime_python import ReasonCode

print(ReasonCode.GENERAL_ERROR)

print(ReasonCode.GENERAL_ERROR.value)
```
---

## Reason

### Class Informations

| Property    | Type         |
| ----------- | ------------ |
| Code        | `ReasonCode` |
| Description | `string`     |

### Usage

```python
from lime_python import Reason, ReasonCode

reason = Reason(ReasonCode.GENERAL_ERROR, "Hey I, but, I'm still alive")
```
---

## Scope

### Class Informations

| Enum       |
| ---------- |
| Transient  |
| Persistent |
| Immediate  |

### Usage

```python
from lime_python import Scope

print(Scope.Immediate)
print(Scope.Immediate.value)
```
