#!/usr/bin/python3
"""
Class CommandConsole for Airbnb
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    HBNB Class
    """

    prompt = '(hbnb)'

    def do_quit(self, line):
        """quit command: exit the program"""
        return True

    def do_EOF(self, line):
        """End of File command: exit the program"""
        return True

    def emptyline(self):
        """overridden to not do nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
