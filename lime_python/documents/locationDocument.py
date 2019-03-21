from lime_python.base.mediaType import MediaType
from lime_python.base.document import Document


class _LocationDocument(Document):

    MIME_TYPE = 'application/vnd.lime.location+json'

    def __init__(self, text=None, latitude=None,
                 longitude=None, altitude=None):
        super().__init__(MediaType.Parse(_LocationDocument.MIME_TYPE))
        self.Text = text
        self.Latitude = latitude
        self.Longitude = longitude
        self.Altitude = altitude

    @property
    def Text(self):
        return self.__Text

    @Text.setter
    def Text(self, text):
        if text is not None and not isinstance(text, str):
            raise ValueError('"Text" must be a string')
        self.__Text = text

    @property
    def Latitude(self):
        return self.__Latitude

    @Latitude.setter
    def Latitude(self, latitude):
        if latitude is not None and not isinstance(latitude, float):
            raise ValueError('"Latitude" must be a float')
        self.__Latitude = latitude

    @property
    def Longitude(self):
        return self.__Longitude

    @Longitude.setter
    def Longitude(self, longitude):
        if longitude is not None and not isinstance(longitude, float):
            raise ValueError('"Logintude" must be a float')
        self.__Logintude = longitude

    @property
    def Altitude(self):
        return self.__Altutide

    @Altitude.setter
    def Altitude(self, altitude):
        if altitude is not None and not isinstance(altitude, float):
            raise ValueError('"Altitude" must be a float')
        self.__Altitude = altitude

    def ToJson(self):
        return {
            'latitude': self.Latitude,
            'longitude': self.Longitude,
            'altitude': self.Altitude,
            'text': self.Text
        }


class LocationDocument(_LocationDocument):

    Type = MediaType.Parse(_LocationDocument.MIME_TYPE)
