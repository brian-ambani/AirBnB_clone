#!/usr/bin/python3
"""
A module with a class that is inherited in all sub classes
"""

import uuid
from datetime import datetime


class BaseModel:
    """ A class that defines attributes and methods """

    def __init__(self, *args, **kwargs):
        """ A method that initializes attributes
            Arguements:
                *args - list of arguements
                **kwargs - A dict of value with keys
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key in kwargs:
                if key == "create_at":
                    self.__dict__["created_at"] = datetime.strptime(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]

    def __str__(self):
        """ Returns class name, id and dict"""

        return "[{}] ({}) {}"\
            .format(self.__class__.__name__, self.id, self.__dict__)
