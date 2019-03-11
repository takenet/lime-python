from command import CommandMethod, CommandStatus
from utils.stringUtils import StringUtils
from reasonCodes import ReasonCodes
from identity import Identity
from reason import Reason
import hashlib


class UtilExtensions:

    PING_URI_TEMPLATE = '/ping'

    @staticmethod
    def IsPingRequest(command):
        if command is None:
            raise TypeError

        if command.Method == CommandMethod.Get and \
                command.Status == CommandStatus.Pending and \
                command.Uri is not None:
            if command.Uri.IsRelative():
                return command.Uri.Path.lower() == \
                    UtilExtensions.PING_URI_TEMPLATE
            else:
                return command.Uri.ToUri().path == \
                    UtilExtensions.PING_URI_TEMPLATE

        return False

    @staticmethod
    def GetResourceUri(command):
        if command.Uri is None:
            raise ValueError('The command "uri" value is None')
        if command.Uri.IsRelative():
            if command.From is None:
                raise ValueError('The command "from" value is None')
            return command.Uri.ToUri(command.From)
        else:
            return command.Uri.ToUri()

    @staticmethod
    def GetIdentity(certificate=None, uri=None):
        if certificate is None and uri is None:
            raise TypeError
        if certificate is not None:
            identityName = certificate.subject[0].value
            if StringUtils.IsNoneOrEmpty(identityName) is False:
                identity = Identity.Parse(identityName)
                return identity
            return None
        elif uri is not None:
            if uri.scheme != 'dns':
                raise ValueError('The uri hostname must be a dns value')
            if uri.username is not None and uri.password is not None:
                return Identity('%s:%s' % (uri.username, uri.password),
                                uri.hostname)
            elif uri.username is not None:
                return Identity(uri.username, uri.hostname)
            elif uri.password is not None:
                return Identity(uri.password, uri.hostname)
            else:
                raise ValueError('The given uri does not contain \
                                username or password')

    @staticmethod
    def ToSHA1Hash(inputString):
        if inputString is None:
            raise TypeError
        return hashlib.sha1(inputString.encode('utf-8')).hexdigest()

    @staticmethod
    def ToReason(exception):
        return Reason(ReasonCodes.GENERAL_ERROR, str(exception))
