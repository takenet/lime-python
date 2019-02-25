# IIdentity Interface
# Gabriel R Santos (@chr0m1ng)
''' Base interface for identities,
    that represents an element
    in a network'''

import abc


class IIdentity(metaclass=abc.ABCMeta):

    # Identity unique name on his domain
    Name = ''
    Domain = ''
