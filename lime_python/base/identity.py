# Identity Class
# Gabriel R Santos (@chr0m1ng)
''' Represents an identity in a domain'''
from lime_python.utils.stringUtils import StringUtils
import sys


class Identity:
    # Initializes a new instance of the Identity class
    def __init__(self, name, domain):
        self.Name = name
        self.Domain = domain

    @property
    def Name(self):
        return self.__Name

    @Name.setter
    def Name(self, name):
        if not isinstance(name, str):
            raise ValueError('"Name" must be a string')
        self.__Name = name

    @property
    def Domain(self):
        return self.__Domain

    @Domain.setter
    def Domain(self, domain):
        if domain is not None and not isinstance(domain, str):
            raise ValueError('"Domain" must be a string')
        self.__Domain = domain

    # Returns a string that represents this instance
    def __str__(self):
        if StringUtils.IsNoneOrEmpty(self.Domain):
            return self.Name
        return '%s@%s' % (self.Name, self.Domain)

    ''' Returns a hash code for this instance
        A hash code for this instance, suitable for use in hashing algorithms
        and data structures like a hash table.'''

    def __hash__(self):
        return hash(str(self).lower()) % ((sys.maxsize + 1) * 2)

    # Determines whether the specified object is equal to this instance
    def __eq__(self, identity):
        if identity is None:
            return False
        try:

            return ((self.Name is None and identity.Name is None) or
                    (self.Name is not None and
                     self.Name.lower() == identity.Name.lower())) and \
                ((self.Domain is None and identity.Domain is None) or
                    (self.Domain is not None and
                        self.Domain.lower() == identity.Domain.lower()))
        except:
            return False

    ''' Creates a Node instance based on the identity,
        with a null value for the instance property.'''

    def ToNode(self):
        from lime_python.base.node import Node
        return Node(self.Name, self.Domain)

    ''' Parses the string to a valid Identity.'''
    def Parse(string):
        if string is None:
            raise TypeError
        if string.isspace():
            raise ValueError('The value cannot be empty')

        splittedIdentity = string.split('@')

        if not StringUtils.IsNoneOrEmpty(splittedIdentity[0]):
            name = splittedIdentity[0]
        else:
            name = None

        if len(splittedIdentity) > 1 and \
                not StringUtils.IsNoneOrEmpty(splittedIdentity[1]):
            domain = splittedIdentity[1].split('/')[0]
        else:
            domain = None
        return Identity(name, domain)

    ''' Tries to parse the string to a valid identity.
        Returns true if parsed with the obj,
        return false if an error occurs and None.'''
    def TryParse(string):
        try:
            value = Identity.Parse(string)
            return True, value
        except:
            return False, None
