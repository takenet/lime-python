from envelope import Envelope


class Session(Envelope):

    def __init__(self):
        super().__init__(None)
        self.State = None  # SessionState
        self.EncryptionOptions = []  # [SessionEncryption]
        self.Encryption = None  # SessionEncryption
        self.CompressionOptions = []  # [SessionCompression]
        self.Compression = None  # SessionCompression
        self.SchemeOptions = []  # [AuthenticationScheme]
        self.Authentication = None  # Authentication
        self.Reason = None  # Reason

    def Scheme(self):
        if self.Authentication is not None:
            return self.Authentication.GetAuthenticationScheme()
        return None
