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

        def my_errors(self, line, num_of_args):
        """Displays error messages to user
        Args:
            line(any): gets user input using command line
            num_of_args(int): number of input arguments
        Description:
            Displays output to the use based on
            the input commands.
        """
        classes = ["BaseModel", "User", "State", "City",
                   "Amenity", "Place", "Review"]

        msg = ["** class name missing **",
               "** class doesn't exist **",
               "** instance id missing **",
               "** no instance found **",
               "** attribute name missing **",
               "** value missing **"]
        if not line:
            print(msg[0])
            return 1
        args = line.split()
        if num_of_args >= 1 and args[0] not in classes:
            print(msg[1])
            return 1
        elif num_of_args == 1:
            return 0
        if num_of_args >= 2 and len(args) < 2:
            print(msg[2])
            return 1
        d = storage.all()

        for i in range(len(args)):
            if args[i][0] == '"':
                args[i] = args[i].replace('"', "")
        key = args[0] + '.' + args[1]
        if num_of_args >= 2 and key not in d:
            print(msg[3])
            return 1
        elif num_of_args == 2:
            return 0
        if num_of_args >= 4 and len(args) < 3:
            print(msg[4])
            return 1
        if num_of_args >= 4 and len(args) < 4:
            print(msg[5])
            return 1
        return 0
    
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
            return 1
        else:
            args_list = args.split()
            if args_list[0] not in ['BaseModel']:
                print(args_list[0])
                print('** class name missing **')
            else:
                if args_list[0] == 'BaseModel':
                    my_model = BaseModel()
                    my_model.save()
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
            return 1
        else:
            args_list = args.split()
            if args_list[0] not in ['BaseModel']:
                print(args_list[0])
                print('** class name missing **')
    
    def help_all(self):
        print ("syntax: create")
        print ("-- Prints all string representation of all instances")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
