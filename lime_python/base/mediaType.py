from lime_python.utils.stringUtils import StringUtils


class _MediaType:

    def __init__(self, inType, subtype, suffix=None):

        self.Type = inType
        self.Subtype = subtype
        self.Suffix = suffix

    @property
    def Type(self):
        return self.__Type

    @Type.setter
    def Type(self, inType):
        if StringUtils.IsNoneOrEmpty(inType) or inType is None:
            raise TypeError
        self.__Type = inType

    @property
    def Subtype(self):
        return self.__Subtype

    @Subtype.setter
    def Subtype(self, subtype):
        if StringUtils.IsNoneOrEmpty(subtype) or subtype is None:
            raise TypeError
        self.__Subtype = subtype

    @property
    def Suffix(self):
        return self.__Suffix

    @Suffix.setter
    def Suffix(self, suffix):
        if suffix is not None and not isinstance(suffix, str):
            raise ValueError('"Suffix" must be a string')
        self.__Suffix = suffix

    def IsJson(self):
        return (self.Suffix is not None and
                self.Suffix.lower() == MediaType.SubTypes.JSON) or \
            (self.Subtype is not None and
             self.Subtype.lower() == MediaType.SubTypes.JSON)

    def __str__(self):
        if StringUtils.IsNoneOrEmpty(self.Suffix):
            return '%s/%s' % (self.Type, self.Subtype)
        return '%s/%s+%s' % (self.Type, self.Subtype, self.Suffix)

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, mediaType):

        if mediaType is None:
            return False
        try:
            return self.Type.lower() == mediaType.Type.lower() and \
                self.Subtype.lower() == mediaType.Subtype.lower() and \
                (self.Suffix is None and mediaType.Suffix is None or
                    (self.Suffix is not None and
                        mediaType.Suffix is not None and
                        self.Suffix.lower() == mediaType.Suffix.lower()))
        except:
            return False

    @property
    def __class__(self):
        return MediaType


class MediaType(_MediaType):

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
        suffix = None

        if len(splittedSubtype) > 1:
            suffix = splittedSubtype[1]

        return MediaType(mtype, subtype, suffix)

    @staticmethod
    def TryParse(s):
        try:
            return True, Parse(s)
        except:
            return False, None

    TextPlain = _MediaType(DiscreteTypes.Text, SubTypes.Plain)
    ApplicationJson = _MediaType(DiscreteTypes.Application, SubTypes.JSON)
