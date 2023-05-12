#!/usr/bin/python3
"""
Console for the AirBnB clone project
"""
import cmd
import models


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """
        Called when an empty line is entered in response to the prompt.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and
        prints the id.
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class
        name and id.
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = models.storage.all()
        if key not in objs:
            print("** no instance found **")
        else:
            print(objs[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change
        into the JSON file).
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = models.storage.all()
        if key not in objs:
            print("** no instance found **")
        else:
            del objs[key]
            models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the
        class name.
        """
        args = arg.split()
        objs = models.storage.all()
        if not arg:
            print([str(objs[key]) for key in objs])
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        else:
            print([str(objs[key]) for key in objs if args[0] in key])

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        objs = models.storage.all()
        if key not in objs:
            print("** no instance found **")
            return
