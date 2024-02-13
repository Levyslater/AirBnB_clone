#!/usr/bin/python3
"""Storage Module that handles data operations"""
import json
from models.base_model import BaseModel
from models.user import User



class FileStorage:
    """
    A class that stores objects in a JSON file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary"""
        return self.__objects

    def new(self, instance):
        """Sets in __objects the instance with key <instance class name>.id"""
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.__objects[key] = instance

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        instance_dict = {key: instance.to_dict() for key, instance in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(instance_dict, file)

    def reload(self):
        """
        Deserializes the JSON file
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                instance_dict = json.load(file)
                for key, value in instance_dict.items():
                    class_name, instance_id = key.split('.')

                    instance = globals()[class_name](**value)

                    self.__objects[key] = instance
        except Exception:
            pass
