from enum import Enum


class SessionCompression(Enum):
    Null = 'null'  # Cannot be None in Python
    GZip = 'gzip'
