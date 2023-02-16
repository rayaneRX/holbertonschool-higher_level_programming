#!/usr/bin/python3
"""class Base"""
import json
from os import path


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs"""
        my_list = []
        if list_objs is not None:
            for i in list_objs:
                my_list.append(i.to_dictionary())
        with open(cls.__name__ + ".json", 'w') as f:
            f.write(cls.to_json_string(my_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""
        if json_string is None or json_string == {}:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        if cls.__name__ == "Rectangle":
            instance = cls(8, 12)
        else:
            instance = cls(8)

        instance.update(**dictionary)
        return instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances:"""
        instance = []
        if path.isfile(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json", 'r') as f:
                lists = cls.from_json_string(f.read())
            for i in lists:
                instance.append(cls.create(**i))
        return instance
