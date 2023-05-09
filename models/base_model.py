#!/usr/bin/python3
"""
A module with a class that is inherited in all sub classes
"""

import uuid


class BaseModel:
    """ A class that defines attributes and methods """

    def __init__(self, *args, **kwargs):
        """ A method that initializes all attributes """

        self.id = str(uuid.uuid4())
