#!/usr/bin/python3
""" HBNBCommand class

Entry point of the command interpreter

"""
import cmd
import sys
import os
import json
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """ Definition for the HBNBCommand class """

    prompt = "(hbnb) "
    classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
               "Place": Place, "Review": Review, "State": State,
               "User": User}

    def do_quit(self, arg):
        """ Exit method for quit typing """
        exit()

    def do_EOF(self, arg):
        """ Exit method for EOF """
        print("")
        exit()

    def emptyline(self, arg):
        """ Method to pass if an emptyline is encountered """
        pass

    def do_create(self, arg):
        """ Creates a new instance """
        if len(arg) == 0:
            print("** class name missing **")
            return
        new = None
        if arg:
            arg_list = arg.split()
            if len(arg_list) == 1:
                if arg in self.classes.keys():
                    new = self.classes[arg]()
                    new.save()
                    print(new.id)
                else:
                    print("** class doesn't exist **")

    def do_show(self, arg):
        """ Prints the string representation of an instance
        based on the class name and id """
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg.split()[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg.split()) > 1:
            key = arg.split()[0] + "." + arg.split()[1]
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        else:
            print("** instance id missing **")

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file) """
        if len(arg) == 0:
            print("** class name missing **")
            return
        arg_list = arg.split()
        try:
            obj = eval(arg_list[0])
        except Exception:
            print("** class doesn't exist **")
            return

        if len(arg_list) == 1:
            print("** instance id missing **")
            return
        if len(arg_list) > 1:
            key = arg_list[0] + "." + arg_list[1]
            if key in storage.all():
                storage.all().pop(key)
                storage.save()
            else:
                print("** no instance found **")
                return

    def do_all(self, arg):
        """ Prints all string representation of all instances
        based or not on the class name """
        if len(arg) == 0:
            print([str(val) for val in storage.all().values()])
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            print([str(val) for key, val in storage.all().items()
                  if arg in key])

    def do_update(self, arg):
        """  Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file) """
        arg_list = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg_list[0] not in self.classes:
            print("** class doesn't exist **")
            return
        elif len(arg_list) == 1:
            print("** instance id missing **")
            return
        else:
            key = arg_list[0] + "." + arg_list[1]
            if key in storage.all():
                if len(arg_list) > 2:
                    if len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        setattr(
                                storage.all()[key],
                                arg[2],
                                arg[3][1:-1])
                        storage.all()[key].save()
                else:
                    print("** attribute name missing **")
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
