#!/usr/bin/python3
"""
A module that defines amenities
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Defines amenities that user can choose
    from to offer at its place"""

    name = ""
