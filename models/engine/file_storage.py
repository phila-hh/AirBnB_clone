#!/usr/bin/python3
""" FileStorage class
Serializes instances to a JSON file and deserializes JSON files to instances.

"""
import json
from uuid import uuid4
from datetime import datetime
import os
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """ Definition for the FileStorage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        FileStorage.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as fname:
            new_dict = {key: obj.to_dict() for key, obj in
                        FileStorage.__objects.items()}
            json.dump(new_dict, fname)

    def reload(self):
        """ Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing """
        if (os.path.isfile(FileStorage.__file_path)):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as fname:
                l_json = json.load(fname)
                for key, value in l_json.items():
                    FileStorage.__objects[key] = eval(
                                        value["__class__"])(**value)
