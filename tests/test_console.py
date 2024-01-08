#!/usr/bin/python3
'''tests for the console'''
import cmd
from unittest.mock import patch
from io import StringIO

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

from models import storage

from console import HBNBCommand
import os

import unittest
import datetime


class Testconsole(unittest.TestCase):
    """tests for the HBNBCommand 'console' class"""

    def setUp(self):
        '''set up module'''
        try:
            os.remove('file.json')
        except Exception as e:
            pass

    def tearDown(self):
        '''tear down module'''
        try:
            os.remove('file.json')
        except Exception as e:
            pass

    def test_help(self):
        '''tests for the help command'''
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update\n
"""
        self.assertEqual(output, f.getvalue())

    def test_help_EOF(self):
        '''tests for the help EOF command'''
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            HBNBCommand().onecmd('help EOF')
            self.assertEqual(mock_stdout.getvalue().strip(),
                             'Exits the program without formatting')

    def test_help_quit(self):
        '''tests for the help quit command'''
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            HBNBCommand().onecmd('help quit')
            self.assertEqual(mock_stdout.getvalue().strip(),
                             'Exits the program with formatting')

    def test_emptyline(self):
        '''tests for the emptyline method'''
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            HBNBCommand().onecmd('')
            self.assertEqual(mock_stdout.getvalue().strip(), '')

    def test_do_create(self):
        """tests for create command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            HBNBCommand().onecmd('create BaseModel')
            model_id = mock_stdout.getvalue().strip()
            model_key_objects = "BaseModel.{}".format(model_id)
            storage.reload()
            self.assertTrue(model_key_objects in storage.all())
            self.assertIsInstance(model_id, str)
            self.assertEqual(model_id, storage.all()[model_key_objects].id)

        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            HBNBCommand().onecmd('create State')
            model_id = mock_stdout.getvalue().strip()
            model_key_objects = "State.{}".format(model_id)
            storage.reload()
            self.assertTrue(model_key_objects in storage.all())
            self.assertIsInstance(model_id, str)
            self.assertEqual(model_id, storage.all()[model_key_objects].id)

    def test_create_with_arg(self):
        """tests for create command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            HBNBCommand().onecmd('create State name="California"')
            model_id = mock_stdout.getvalue().strip()
            model_key_in_objects = "State.{}".format(model_id)
            storage.reload()
            self.assertTrue(model_key_in_objects in storage.all())
            model = storage.all()[model_key_in_objects]
            self.assertIsInstance(model_id, str)
            self.assertIsInstance(model.name, str)
            self.assertEqual(model.name, "California")

    def test_create_with_args(self):
        """tests for create command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            HBNBCommand().onecmd('\
create Place city_id="0001" user_id="0001" name="My_little_house" name2="My_little"_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297')
            model_id = mock_stdout.getvalue().strip()
            model_key_in_objects = "Place.{}".format(model_id)
            storage.reload()
            self.assertTrue(model_key_in_objects in storage.all())
            model = storage.all()[model_key_in_objects]
            self.assertIsInstance(model_id, str)
            self.assertIsInstance(model.city_id, str)
            self.assertIsInstance(model.user_id, str)
            self.assertIsInstance(model.name, str)
            self.assertIsInstance(model.number_rooms, int)
            self.assertIsInstance(model.number_bathrooms, int)
            self.assertIsInstance(model.max_guest, int)
            self.assertIsInstance(model.price_by_night, int)
            self.assertIsInstance(model.latitude, float)
            self.assertIsInstance(model.longitude, float)
            self.assertEqual(model.name, "My little house")
            self.assertEqual(model.name2, 'My little\\" house')

    def test_help_create(self):
        '''tests for the help create command'''
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            HBNBCommand().onecmd('help create')
            self.assertEqual(mock_stdout.getvalue().strip(),
                             """Creates a class of any type
[Usage]: create <className>""")
