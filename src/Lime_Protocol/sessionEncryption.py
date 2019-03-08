from enum import Enum


class SessionEncryption(Enum):
    Null = 'null'  # Cannot be None in Python
    TLS = 'tls'
