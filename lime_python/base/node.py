from lime_python.utils.stringUtils import StringUtils
from lime_python.base.identity import Identity


class Node(Identity):

    ''' Initializes a new instance of the Node class.'''

    def __init__(self, name, domain=None, instance=None):
        super().__init__(name, domain)
        self.Instance = instance

    ''' Returns a string that represents this instance.'''

    def __str__(self):
        if self.Instance is not None:
            return ('%s/%s' % (super().__str__(), self.Instance)).rstrip('/')
        else:
            return super().__str__()

    def __repr__(self):
        return str(self)

    ''' Determines whether the specified object is equal to this instance.'''

    def __eq__(self, node):
        if node is None:
            return False
        try:
            return ((self.Name is None and node.Name is None) or
                    (self.Name is not None and
                    self.Name.lower() == node.Name.lower()) and
                    (self.Domain is None and node.Domain is None) or
                    (self.Domain is not None and
                    self.Domain.lower() == node.Domain.lower()) and
                    (self.Instance is None and node.Instance is None) or
                    (self.Instance is not None and
                    self.Instance.lower() == node.Instance.lower()))
        except:
            return False

    ''' Returns a hash code for this instance.'''

    def __hash__(self):
        return super().__hash__()

    ''' Parses the string to a valid Node.'''
    def Parse(string):
        if StringUtils.IsNoneOrEmpty(string):
            raise TypeError

        identity = Identity.Parse(string)
        identityString = str(identity)

        if len(string) > len(identityString):
            instance = string[len(identityString) + 1:]
        else:
            instance = None

        return Node(identity.Name, identity.Domain, instance)

    ''' Tries to parse the string to a valid Node
        Returns true if parsed with the obj,
        return false if an error occurs and None.'''
    def TryParse(string):
        try:
            value = Node.Parse(string)
            return True, value
        except:
            return False, None

    ''' Creates an Identity instance based on the Node identity.'''

    def ToIdentity(self):
        return Identity(self.Name, self.Domain)

    ''' Indicates if the node is a complete representation,
        with name, domain and instance.'''

    def IsComplete(self):
        return not StringUtils.IsNoneOrEmpty(self.Name) and \
            not StringUtils.IsNoneOrEmpty(self.Domain) and \
            not StringUtils.IsNoneOrEmpty(self.Instance)

    ''' Creates a new object that is a copy of the current instance.'''

    def Copy(self):
        return Node(self.Name, self.Domain, self.Instance)
