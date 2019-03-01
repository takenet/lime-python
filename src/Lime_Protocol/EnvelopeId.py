import uuid


class EnvelopeId:

    @staticmethod
    def NewId():
        return str(uuid.uuid4())
