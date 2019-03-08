from utils.stringUtils import StringUtils
from base64 import b64encode, b64decode


class StringExtensions:

    @staticmethod
    def RemoveCrLf(value):
        if value is None:
            raise TypeError
        return value.replace('\n', '').replace('\r', '')

    IDENT_STRING = '  '

    @staticmethod
    def IdentJson(jsonString):
        if StringUtils.IsNoneOrEmpty(jsonString):
            raise TypeError
        jsonString = StringExtensions.RemoveCrLf(jsonString)

        string = ''
        ident = 0
        quoted = False
        for i in range(len(jsonString)):
            ch = jsonString[i]
            if ch == '{' or ch == '[':
                string += ch
                if quoted is False:
                    string += '\n'
                    ident = ident + 1
                    for _ in range(ident):
                        string += IDENT_STRING

            elif ch == '}' or ch == ']':
                if quoted is False:
                    string += '\n'
                    ident = ident - 1
                    for _ in range(ident):
                        string += IDENT_STRING
                string += ch

            elif ch == '"':
                string += ch
                escaped = False
                index = i
                if index > 0:
                    index = index - 1
                while index > 0 and jsonString[index] == '\\':
                    escaped = not escaped
                    index = index - 1
                if escaped is False:
                    quoted = not quoted

            elif ch == ',':
                string += ch
                if quoted is False:
                    string += '\n'
                    for _ in range(ident):
                        string += IDENT_STRING

            elif ch == ':':
                string += ch
                if quoted is False:
                    string += ' '

            else:
                string += ch

        return string

    @staticmethod
    def ToCamelCase(value):
        titleCase = ''.join(x for x in value.title() if not x.isspace())
        return titleCase[0].lower() + titleCase[1:]

    @staticmethod
    def ToTitleCase(value):
        return ''.join(x for x in value.title() if not x.isspace())

    @staticmethod
    def ToBase64(value):
        if StringUtils.IsNoneOrEmpty(value):
            raise TypeError
        return b64encode(value.encode('utf-8'))

    @staticmethod
    def FromBase64(value):
        if StringUtils.IsNoneOrEmpty(value):
            raise TypeError
        return b64decode(value).decode('utf-8')

    @staticmethod
    def Escape(value):
        if value is None:
            raise TypeError
        return value.replace('\\', '\\\\').replace('"', '\\"')

    @staticmethod
    def TrimFirstDomainLabel(domain):
        if domain is None:
            raise TypeError
        indexOfPoint = domain.find('.')
        if indexOfPoint < 0:
            return domain
        return domain[domain.find('.') + 1: len(domain) - domain.find('.') - 1]
