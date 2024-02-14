#!/usr/bin/python3
"""Main module where other classes inherits from"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """The base class where other classes inherit from"""
    date_style = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        Initialize a new instance of the BaseModel class.

            Args:
        *args: Positional arguments. These are not used.
        **kwargs: Keyword arguments.
        These are used to set attributes of the
            instance.
        """
        # To always initialize other classes's attrbutes not
        # in BaseModel
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        var = datetime.strptime(value, self.date_style)
                        setattr(self, key, var)
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        Return a string representation of the instance.

        Returns:
        str: A string representation of the instance.
        """
        # Return a string representation of the instance
        _str = "[" + str(self.__class__.__name__) + "]"
        _str += " (" + str(self.id) + ") " + str(self.__dict__)
        return _str

    def save(self):
        """
        Updates instance attribute 'updated_at'
        Save the instance to the storage.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        # Convert both datetime objects to string
        return {
            **{key: value.strftime(self.date_style)
               if isinstance(value, datetime)
               else value
               for key, value in self.__dict__.items()},
            "__class__": self.__class__.__name__
        }
