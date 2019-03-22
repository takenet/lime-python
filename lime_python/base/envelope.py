from lime_python.base.node import Node
import uuid


class Envelope:

    def __init__(self, id=None, fromN=None, to=None):

        self.Id = id
        self.From = fromN
        self.To = to

    @property
    def Id(self):
        return self.__Id

    @Id.setter
    def Id(self, id):
        if id is None:
            id = str(uuid.uuid4())
            self.__Id = id
        else:
            self.__Id = id

    @property
    def From(self):
        return self.__From

    @From.setter
    def From(self, fromN):
        if fromN is not None and isinstance(fromN, str):
            fromN = Node.Parse(fromN)
        if fromN is None or isinstance(fromN, Node):
            self.__From = fromN
        else:
            raise ValueError('"From" must be a Node')

    @property
    def To(self):
        return self.__To

    @To.setter
    def To(self, to):
        if to is not None and isinstance(to, str):
            to = Node.Parse(to)
        if to is None or isinstance(to, Node):
            self.__To = to
        else:
            raise ValueError('"To" must be a Node')

    def ToJson(self):
        json = {
            'id': self.Id
        }
        if self.To is not None:
            json['to'] = str(self.To)
        if self.From is not None:
            json['from'] = str(self.From)
        return json
