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

    def save(self):
        """updates the public instance attribute
            updated_at with the current datetime
        """

        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """creates a dict with keys and
        returning datetimes as string
        """
        dict_data = dict(self.__dict__)
        dict_data['__class__'] = type(self).__name__
        dict_data['created_at'] = self.created_at.isoformat()
        dict_data['updated_at'] = self.updated_at.isoformat()
        return dict_data
