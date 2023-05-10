#!/usr/bin/python3
"""
A module with a class that is inherited in all sub classes
"""

import uuid
from datetime import datetime
from models import storage


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

    def __str__(self):
        """ Returns class name, id and dict"""
