from lime_python.utils.stringUtils import StringUtils
from lime_python.base.identity import Identity


class Node(Identity):
    """
    Representation of a LIME Message

    Parameters:
        name (str)
        domain (str)
        instance (str)
    """

    def __init__(self, name, domain=None, instance=None):
        super().__init__(name, domain)
        self.Instance = instance

    def __str__(self):
        """Returns a string that represents this instance."""
        if self.Instance is not None:
            return ('%s/%s' % (super().__str__(), self.Instance)).rstrip('/')
        else:
            return super().__str__()

    def __repr__(self):
        return str(self)

    def __eq__(self, node):
        """Determines whether the specified object is equal to this instance"""
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

    def __hash__(self):
        """Returns a hash code for this instance."""
        return super().__hash__()

    def Parse(string):
        """Parses the string to a valid Node."""
        if StringUtils.IsNoneOrEmpty(string):
            raise TypeError

        identity = Identity.Parse(string)
        identityString = str(identity)

        if len(string) > len(identityString):
            instance = string[len(identityString) + 1:]
        else:
            instance = None

        return Node(identity.Name, identity.Domain, instance)

    def TryParse(string):
        """Tries to parse the string to a valid Node
            Returns true if parsed with the obj,
            return false if an error occurs and None."""
        try:
            value = Node.Parse(string)
            return True, value
        except:
            return False, None

    def ToIdentity(self):
        """Creates an Identity instance based on the Node identity."""
        return Identity(self.Name, self.Domain)

    def IsComplete(self):
        """Indicates if the node is a complete representation,
            with name, domain and instance."""
        return not StringUtils.IsNoneOrEmpty(self.Name) and \
            not StringUtils.IsNoneOrEmpty(self.Domain) and \
            not StringUtils.IsNoneOrEmpty(self.Instance)

    def Copy(self):
        """Creates a new object that is a copy of the current instance."""
        return Node(self.Name, self.Domain, self.Instance)
