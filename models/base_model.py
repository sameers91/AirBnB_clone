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
        dict = {}
        dict['__class__'] = type(self).__name__
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dict[key] = value.isoformat()
            else:
                dict[key] = value
        return dict

    def __str__(self):
        return f"{type(self).__name__} ({self.id}) {self.__dict__}"

