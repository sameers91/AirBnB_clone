"""
BaseModel class that defines all common attributes
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel():
    """
    class BaseModel
    """

    def __init__(self, *args, **kwargs):

        if kwargs != {}:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)

        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        storage.new(self)

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        dict = self.__dict__
        dict['__class__'] = type(self).__name__
        print(self.created_at)
        print(type(self.created_at))
        self.created_at = datetime.strptime(self.created_at, '%Y-%m-%dT%H:%M:%S.%f')
        print(self.created_at)
        dict['created_at'] = (self.created_at).isoformat()
        dict['updated_at'] = (self.updated_at).isoformat()
        return dict

    def __str__(self):
        return f"{type(self).__name__} ({self.id}) {self.__dict__}"

