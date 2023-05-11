#!/usr/bin/python3
""" Module containing a class that
serializes instances to a JSON file
and deserilizes JSON file to instances
"""

import json


class FileStorage:
    """serilizes instances and deserilizes JSON files"""

    __file_path = "file.json"
    __object = {}

    def all(self):
        """ A method returning dict"""

        return self.objects

    def new(self, obj):
        """Method that sets in __objects the obj
        with key <obj class name>.id"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serilizes __objects to JSON file & path:
        __file_path"""

        with open(self.__file_path, 'w') as f:
            obj_dict = {}
            for key, value in self.__objects.items():
                obj_dict[key] = value.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        """deserilizes the JSON file to __objects"""
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_-path, 'r') as f:
            for key, value in json.load(f).item():
                self.new(dict[value['__class__']](**value))
