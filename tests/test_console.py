#!/usr/bin/python3
"""test for console"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):

    def tearDown(self):
        """Remove temporary file (file.json) created as a result"""
        try:
            os.remove("../file.json")
        except Exception:
            pass

    def test_docstrings_in_console(self):
        """checking for docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand().do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand().do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand().emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand().do_create.__doc__)
        self.assertIsNotNone(HBNBCommand().do_show.__doc__)
        self.assertIsNotNone(HBNBCommand().do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand().do_all.__doc__)
        self.assertIsNotNone(HBNBCommand().do_update.__doc__)
        self.assertIsNotNone(HBNBCommand().do_count.__doc__)
        self.assertIsNotNone(HBNBCommand().default.__doc__)

    def test_press_enter(self):
        """When press enter no action has to been executed"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("            \n")
        self.assertEqual(f.getvalue(), '')

    def test_wrong_command(self):
        """When press random words no action has to been executed"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Goku")
        self.assertEqual(f.getvalue(), '*** Unknown syntax: Goku\n')

    def test_help_with_args(self):
        """Test if all docstring were written"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        self.assertEqual(f.getvalue(), 'Quit command to exit the program\n\n')

    def test_command_with_spaces(self):
        """Despite spaces the command has to be executed"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("     help        quit")
        self.assertEqual(f.getvalue(), 'Quit command to exit the program\n\n')

    def test_quit(self):
        """Test quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        self.assertEqual(f.getvalue(), '')

    def test_EOF(self):
        """Test EOF"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        self.assertEqual(f.getvalue(), '\n')

    def test_count(self):
        """Validate count method"""
        try:
            os.remove("file.json")
        except:
            pass

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
        self.assertNotEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("id.count()")
        self.assertEqual(f.getvalue(), '0\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count(d)")
        self.assertEqual(f.getvalue(), '*** Unknown syntax: User.count(d)\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()d")
        self.assertEqual(f.getvalue(), '*** Unknown syntax: User.count()d\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
        self.assertEqual(f.getvalue(), '0\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count id")
        self.assertEqual(f.getvalue(), '0\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count BaseModel id")
        self.assertEqual(f.getvalue(), '0\n')

    def test_create(self):
        """Validate create method"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Goku")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        self.assertRegex(f.getvalue(), '^[0-9a-f]{8}-[0-9a-f]{4}-[1-5]'
                                       '[0-9a-f]{3}-[89ab][0-9a-f]{3}-'
                                       '[0-9a-f]{12}$')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        self.assertRegex(f.getvalue(), '^[0-9a-f]{8}-[0-9a-f]{4}-[1-5]'
                                       '[0-9a-f]{3}-[89ab][0-9a-f]{3}-'
                                       '[0-9a-f]{12}$')

    def test_show(self):
        """Validate show in both ways"""
        try:
            os.remove("file.json")
        except:
            pass

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show" + "User " + id)
        self.assertIsNotNone(f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show dsdsdas")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User 111")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show(1)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("sdasdasd.show(1)")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')

    def test_destroy(self):
        """Validate destroy in both ways"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy dsdsdas")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User 111")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy User")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy(1)")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("sdasdasd.destroy(1)")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy()")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')

    def test_all(self):
        """Validate all both ways"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        self.assertNotEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        self.assertNotEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all sddsds")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
        self.assertNotEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all(ss)")
        self.assertEqual(f.getvalue(),
                         '*** Unknown syntax: BaseModel.all(ss)\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("ssss.all()")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all(dasds)")
        self.assertEqual(f.getvalue(), '*** Unknown syntax: User.all(dasds)\n')

    def test_update(self):
        """Validate all both ways"""
        try:
            os.remove("file.json")
        except:
            pass

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
        id = f.getvalue()

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        self.assertEqual(f.getvalue(), '** class name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update asdasdas")
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User")
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User 1112")
        self.assertEqual(f.getvalue(), '** no instance found **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + id)
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + id + " name")
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + id + " name " + "Goku")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update User " + id + " name " + "Goku")
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("asdasd.update()".format(id))
        self.assertEqual(f.getvalue(), '** class doesn\'t exist **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update()".format(id))
        self.assertEqual(f.getvalue(), '** instance id missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update(\"{}\")".format(id))
        self.assertEqual(f.getvalue(), '** attribute name missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update(\"{}\", \"name\")".format(id))
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update(\"{}\", \'name\')".format(id))
        self.assertEqual(f.getvalue(), '** value missing **\n')
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.update(\"{}\", \'name\', \"Goku\")".
                                 format(id))
        self.assertEqual(f.getvalue(), '')
        with patch('sys.stdout', new=StringIO()) as f:
            a = "User.update(\"{}\", \'name\', \"Goku Holberton\")".format(id)
            HBNBCommand().onecmd(a)
        self.assertEqual(f.getvalue(), '')

if __name__ == '__main__':
    unittest.main()
