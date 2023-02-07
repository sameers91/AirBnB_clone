#!/usr/bin/python3
"""
BaseModel class that defines all common attributes

"""
import uuid
from datetime import datetime


class BaseModel():
    """
    class BaseModel
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict = self.__dict__
        dict['__class__'] = type(self).__name__
        dict['created_at'] = (self.created_at).isoformat()
        dict['updated_at'] = (self.updated_at).isoformat()
        return dict

    def __str__(self):
        return f"{type(self).__name__} ({self.id}) {self.__dict__}"
