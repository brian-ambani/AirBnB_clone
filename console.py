#!/usr/bin/env python3
"""This module defines the HBNBCommand class, which is used to implement a
console for interacting with the HBNB data storage system.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the command interpreter for the HBNB data storage
    system console.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program gracefully on end-of-file (EOF)"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def help_help(self):
        """Provide help documentation for the help command"""
        print("Get help on a command by entering 'help <command>'.")
        print("List available commands by entering 'help'.")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
