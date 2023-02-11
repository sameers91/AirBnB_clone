#!/usr/bin/python3

"""
HBNBCommand contains the entry point of the command interpreter
"""

import cmd
import sys
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):

    """
    class HBNBCommand
    """

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'

    def do_quit(self, arg):
        sys.exit(1)

    def do_EOF(self, line):
        sys.exit(1)

    def emptyline(self):
        pass

    def help_quit(self):
        print ("syntax: quit")
        print ("-- terminates the application")

    def help_EOF(self):
        print ("syntax: EOF")
        print ("-- terminates the application")

    def do_create(self, args):
        
        if len(args) == 0:
            print("** class name missing **")
        else:
            args_list = args.split()
            if args_list[0] not in ['BaseModel']:
                print(args_list[0])
                print('** class name missing **')
            else:
                if args_list[0] == 'BaseModel':
                    my_model = BaseModel()
                    print (my_model.id)

    def help_create(self):
        print ("syntax: create")
        print ("-- create an instance of a model")

    def do_show(self, args):
        if len(args) == 0:
            print("** class name missing **")

    def help_show(self):
        print ("syntax: create")
        print ("-- show an instance of a model")

    def do_destroy(self, args):
        if len(args) == 0:
            print("** class name missing **")
    
    def help_destroy(self):
        print ("syntax: create")
        print ("-- desroy an instance of a model")

    def do_all(self, args):
        if len(args) == 0:
            print("** class name missing **")
    
    def help_all(self):
        print ("syntax: create")
        print ("-- Prints all string representation of all instances")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
