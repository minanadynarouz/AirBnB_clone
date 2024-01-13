#!/usr/bin/python3
"""File storage that convert the dictionary
representation to a JSON string
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}
    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def all(self):
        """return dict objects"""
        return self.__class__.__objects

    def new(self, obj):
        """Add objects in __objects dict to be saved to file later"""
        obj_class_name = obj.__class__.__name__ + "." + str(obj.id)
        self.__class__.__objects[obj_class_name] = obj

    def save(self):
        """Save the objects in dict to a file and serialize them"""
        new_dict = {}
        for k in self.__objects:
            new_dict[k] = self.__objects[k].to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    class_name = value["__class__"]
                    if class_name not in self.classes:
                        pass

                    obj_class = self.classes[class_name]
                    base_data = obj_class(**value)
                    self.__objects[key] = base_data
