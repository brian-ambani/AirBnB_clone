#!/usr/bin/python3
"""
A module that defines city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """defines city to look for"""

    state_id = ""
    name = ""
