#!/usr/bin/python3
"""
Class CommandConsole for Airbnb
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    HBNB Class
    """
    prompt = '(hbnb)'
    allowed_class = {"BaseModel": BaseModel}

    def do_quit(self, line):
        """quit command: exit the program"""
        return True

    def do_EOF(self, line):
        """End of File command: exit the program"""
        return True

    def emptyline(self):
        """overridden to not do nothing"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id"""
        if len(line) == 0:
            print("** class name missing **")
            return
        elif line in HBNBCommand.allowed_class.keys():
            instance =  HBNBCommand.allowed_class[line]()
        elif line not in HBNBCommand.allowed_class.keys():
            print("** class doesn't exist **")
            return

        print(instance.id)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
