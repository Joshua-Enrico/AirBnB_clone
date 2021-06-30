#!/usr/bin/python3
"""
test console
"""
import unittest
from unittest.mock import patch
from io import StringIO
# import pep8
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


class ConsoleTest(unittest.TestCase):
    """testing console"""

    @classmethod
    def setUpClass(self):
        """setting class up"""
        self.console = HBNBCommand()

    def test_docstrings(self):
        """testing docstings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)

    def test_non_exist_command(self):
        """testing a command that doesn't exist"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("goku")
            self.assertEqual('*** Unknown syntax: goku\n' or '',
                             f.getvalue())

    def test_empty_line(self):
        """testing empty input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """testing quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("quit")
            self.assertEqual('', f.getvalue())


class HelpTest(unittest.TestCase):
    """testing command test in console"""

    @classmethod
    def setUpClass(self):
        """setting class up"""
        self.console = HBNBCommand()

    def help_command(self):
        """testing an only help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help")
            output = '\nDocumented commands (type help <topic>)[103 chars]\n\n'
            self.assertEqual(output, f.getvalue())

    def help_help_command(self):
        """test commands: help help"""
        expected = 'List available commands with "help" or \
            detailed help with "help cmd".\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help help")
            self.assertEqual(expected, f.getvalue())

    def EOF_help_command(self):
        """test commands: help EOF"""
        expected = 'End of File command: exit the program\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(expected, f.getvalue())

    def all_help_command(self):
        """test commands: help all"""
        expected = 'Prints all string representation of all instances \
            based or not on the class name \
            Ex: $ all BaseModel or $ all.\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            self.assertEqual(expected, f.getvalue())

    def count_help_command(self):
        """test commands: help count"""
        expected = 'count instances of the class\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            self.assertEqual(expected, f.getvalue())

    def create_help_command(self):
        """test commands: help create"""
        expected = 'Creates a new instance of BaseModel, saves it (to the JSON file)\n \
            and prints the id\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            self.assertEqual(expected, f.getvalue())

    def quit_help_command(self):
        """test commands: help quit"""
        expected = 'quit command: exit the program\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(expected, f.getvalue())

    def destroy_help_command(self):
        """test commands: help destroy"""
        expected = 'Deletes an instance based on the class name and\n \
        id (save the change into the JSON file).\n \
        Ex: $ destroy BaseModel 1234-1234-1234\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(expected, f.getvalue())

    def show_help_command(self):
        """test commands: help show"""
        expected = 'Prints the string representation of an instance\n \
            based on the class name and id.\n \
            Ex: $ show BaseModel 1234-1234-1234.'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            self.assertEqual(expected, f.getvalue())

    def update_help_command(self):
        """test commands: help update"""
        expected = 'Updates an instance based on the class name and id\n \
            by adding or updating attribute\n \
            (save the change into the JSON file).\n \
            - Usage:\n \
            update <class name> <id> <attribute name> "<attribute value>"\n \
            - Ex:\n \
            $ update BaseModel 1234-1234-1234 email\
                 "aibnb@holbertonschool.com"\n \
            - Only one attribute can be updated at the time\n'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            self.assertEqual(expected, f.getvalue())


class CreateTest(unittest.TestCase):
    """testing command test in console"""

    @classmethod
    def setUpClass(self):
        """setting class up"""
        self.console = HBNBCommand()

    def test_create(self):
        """testing creat input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create holbieees")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.console.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            self.assertEqual(
                            '["[User', f.getvalue()[:7])


class ShowTest(unittest.TestCase):
    """testing command show in console"""

    @classmethod
    def setUpClass(self):
        """setting class up"""
        self.console = HBNBCommand()

    def test_show(self):
        """testing show's behaviour"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show holbieees")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User")
            self.assertEqual("** instance id missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User 123123")
            self.assertEqual("** no instance found **\n",
                             f.getvalue())

    def test_destroy(self):
        """testing destroy's behaviour"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy holbies")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy User 123123")
            self.assertEqual("** no instance found **\n",
                             f.getvalue())

    def test_all(self):
        """Test all command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all 123123")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all State")
            self.assertEqual('["[Stat', f.getvalue()[:7])

    def test_update(self):
        """Testing update's behaviour"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update holbies")
            self.assertEqual("** class doesn't exist **\n",
                             f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel")
            self.assertEqual(
                "** instance id missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User 123123")
            self.assertEqual(
                "** no instance found **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            obj = f.getvalue()
        my_id = obj[obj.find('(')+1:obj.find(')')]
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User " + my_id)
            self.assertEqual(
                "** attribute name missing **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update User " + my_id + " Name")
            self.assertEqual(
                "** value missing **\n", f.getvalue())
