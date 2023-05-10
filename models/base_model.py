#!/usr/bin/python3
"""
A module with a class that is inherited in all sub classes
"""

import uuid
import datetime


class BaseModel:
    """ A class that defines attributes and methods """

    def __init__(self, id, created_at, updated_at):
        """ A method that initializes all attributes """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

