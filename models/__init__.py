#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage
according to HBNB_TYPE_STORAGE environment variable"""
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage

else:
    from models.engine.file_storage import FileStorage
