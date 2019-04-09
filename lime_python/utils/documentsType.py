from lime_python.utils.limeException import LimeException
from lime_python.base.mediaType import MediaType


def GetDocumentByMediaType(mediaType):
    """
    Returns a document from that implements the given mediaType

    Parameters:
        mediaType (str)
    """

    from lime_python.documents.chatStateDocument import ChatStateDocument
    from lime_python.documents.collectionDocument import CollectionDocument
    from lime_python.documents.containerDocument import ContainerDocument
    from lime_python.documents.inputDocument import InputDocument
    from lime_python.documents.listDocument import ListDocument
    from lime_python.documents.locationDocument import LocationDocument
    from lime_python.documents.mediaLinkDocument import MediaLinkDocument
    from lime_python.documents.menuDocument import MenuDocument
    from lime_python.documents.redirectDocument import RedirectDocument
    from lime_python.documents.plainTextDocument import PlainTextDocument
    from lime_python.documents.resourceDocument import ResourceDocument
    from lime_python.documents.webLinkDocument import WebLinkDocument
    from lime_python.documents.multimediaMenuDocument \
        import MultimediaMenuDocument
    from lime_python.documents.paymentInvoiceDocument \
        import PaymentInvoiceDocument
    from lime_python.documents.paymentReceiptDocument \
        import PaymentReceiptDocument
    from lime_python.documents.sensitiveInformationDocument \
        import SensitiveInformationDocument

    DOCUMENTS_TYPES = {
        ChatStateDocument.MIME_TYPE: ChatStateDocument,
        CollectionDocument.MIME_TYPE: CollectionDocument,
        ContainerDocument.MIME_TYPE: ContainerDocument,
        InputDocument.MIME_TYPE: InputDocument,
        ListDocument.MIME_TYPE: ListDocument,
        LocationDocument.MIME_TYPE: LocationDocument,
        MediaLinkDocument.MIME_TYPE: MediaLinkDocument,
        MenuDocument.MIME_TYPE: MenuDocument,
        MultimediaMenuDocument.MIME_TYPE: MultimediaMenuDocument,
        PaymentInvoiceDocument.MIME_TYPE: PaymentInvoiceDocument,
        PaymentReceiptDocument.MIME_TYPE: PaymentReceiptDocument,
        PlainTextDocument.MIME_TYPE: PlainTextDocument,
        RedirectDocument.MIME_TYPE: RedirectDocument,
        ResourceDocument.MIME_TYPE: ResourceDocument,
        SensitiveInformationDocument.MIME_TYPE: SensitiveInformationDocument,
        WebLinkDocument.MIME_TYPE: WebLinkDocument,
        str(MediaType.ApplicationJson): dict
    }
    try:
        return DOCUMENTS_TYPES[mediaType]
    except KeyError:
        return None
