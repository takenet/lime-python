from Utils.StringUtils import StringUtils


class DiscreteTypes:

    Application = 'application'
    Text = 'text'
    image = 'image'
    Audio = 'audio'
    Video = 'video'


class CompositeTypes:

    Message = 'message'
    Multipart = 'multipart'


class SubTypes:

    Plain = 'plain'
    JSON = 'json'
    XML = 'xml'
    HTML = 'html'
    JPeg = 'jpeg'
    Bitmap = 'bmp'
    Javascript = 'javascript'


class _MediaType:

    def __init__(self, inType, subtype, suffix=None):
        if StringUtils.IsNoneOrEmpty(inType):
            raise TypeError
        if StringUtils.IsNoneOrEmpty(subtype):
            raise TypeError

        self.Type = inType
        self.Subtype = subtype
        self.Suffix = suffix

    def IsJson(self):
        return (self.Suffix is not None and
                self.Suffix.lower() == SubTypes.JSON) or \
                (self.Subtype is not None and
                    self.Subtype.lower() == SubTypes.JSON)

    def __str__(self):
        if StringUtils.IsNoneOrEmpty(self.Suffix):
            return '%s/%s' % (self.Type, self.Subtype)
        return '%s/%s+%s' % (self.Type, self.Subtype, self.Suffix)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, mediaType):

        if mediaType is None:
            return False
        try:
            return self.Type.lower() == mediaType.Type.lower() and \
                self.Subtype.lower() == mediaType.Subtype.lower() and \
                (self.Suffix is None and mediaType.Suffix is None or
                    (self.Suffix is not None and mediaType.Suffix is not None and
                        self.Suffix.lower() == mediaType.Suffix.lower()))
        except:
            return False

    @staticmethod
    def Parse(s):
        if StringUtils.IsNoneOrEmpty(s):
            raise TypeError

        splittedMediaType = s.split(';')[0].split('/')
        if len(splittedMediaType) != 2:
            raise ValueError('Invalid media type format')

        mtype = splittedMediaType[0]
        splittedSubtype = splittedMediaType[1].split('+')
        subtype = splittedSubtype[0]
        suffix = ''

        if len(splittedSubtype > 1):
            suffix = splittedSubtype[1]

        return _MediaType(mtype, subtype, suffix)

    @staticmethod
    def TryParse(s):
        try:
            return True, Parse(s)
        except:
            return False, None


class MediaType(_MediaType):

    TextPlain = _MediaType(DiscreteTypes.Text, SubTypes.Plain)
    ApplicationJson = _MediaType(DiscreteTypes.Application, SubTypes.JSON)
