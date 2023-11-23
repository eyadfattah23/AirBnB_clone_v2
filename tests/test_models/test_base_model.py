#!/usr/bin/python3
""" """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class TestBaseModel(unittest.TestCase):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """set up module"""
        pass

    def tearDown(self):
        """tear down module"""
        try:
            os.remove('file.json')
        except Exception as e:
            pass

    def test_default(self):
        """test instance type"""
        i = self.value()
        self.assertEqual(type(i), self.value)

        self.assertIsInstance(i.to_dict()['__class__'], str)

    def test_kwargs(self):
        """test creation with kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """test creation with kwargs with an int as a key """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """test string representation"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """test dictionary representation"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """test creation with a None kwargs"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """test creation with a single parameter in kwargs"""
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """test the id attribute"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """test created_at type"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)
        self.assertIsInstance(new.to_dict()['created_at'], str)

    def test_updated_at(self):
        """test updated_at type"""
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        self.assertIsInstance(new.to_dict()['updated_at'], str)
        n = new.to_dict()
        new = BaseModel(**n)
        create_time = new.updated_at
        new.id = '123465'
        new.save()
        self.assertFalse(create_time == new.updated_at)
