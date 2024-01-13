#!/usr/bin/python3
"""Model base"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """Base Class"""
    def __init__(self, *args, **kwargs):
        """Constructor
        Args:
            *args (any): unused
            **kwargs (dict): key/value pairs of attributes
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at':
                    self.created_at = datetime.fromisoformat(value)
                elif key == 'updated_at':
                    self.updated_at = datetime.fromisoformat(value)
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Update the timestamp for the updates"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """dictionary containing all keys/values"""
        rdict = self.__dict__.copy()
        rdict['created_at'] = self.created_at.isoformat()
        rdict['updated_at'] = self.updated_at.isoformat()
        rdict['__class__'] = self.__class__.__name__
        return rdict

    def __str__(self):
        """ print() __str__ method """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
