#!/usr/bin/python3
"""Test User"""
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import pep8
import unittest


class Testuser(unittest.TestCase):
    """
    Unittests for the User class.
    """

    def test_pep8_user(self):
        """pep8 test.
        Test makes sure the Python code is up to the
        pep8 standard.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
