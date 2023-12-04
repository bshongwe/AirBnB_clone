#!/usr/bin/python3
"""Module for FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """Serialises BaseModel to JSON & deserialises JSON back to BaseModel"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects dict"""
        return FileStorage.__objects
