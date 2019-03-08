from command import CommandMethod, CommandStatus


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
