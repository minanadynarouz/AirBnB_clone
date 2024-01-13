#!/usr/bin/python3
"""Console App to control website"""

import cmd
import models
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Functions of the console"""
    intro = 'Welcome to the AirBnB Console! Type help or ? to list commands.\n'
    prompt = '(hbnb) '
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }

    # def precmd(self, argument):
    #     """ executed just before the command line is interpreted """
    #     args = argument.split('.', 1)
    #     if len(args) == 2:
    #         _class = args[0]
    #         args = args[1].split('(', 1)
    #         command = args[0]
    #         if len(args) == 2:
    #             args = args[1].split(')', 1)
    #             if len(args) == 2:
    #                 _id = args[0]
    #                 other_arguments = args[1]
    #         line = command + " " + _class + " " + _id + " " + other_arguments
    #         return line
    #     else:
    #         return argument

    def do_EOF(self, arg):
        '''End of the command line interpreter'''
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        raise SystemExit

    def emptyline(self):
        """Overrides default behavior not to print new line"""
        pass

    def do_create(self, arg):
        """Creates new object"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.__class__.classes.keys():
            print("** class doesn't exist **")
        else:
            obj = self.__class__.classes[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance"""
        arg_inputs = args.split(" ")
        if len(arg_inputs) == 0:
            print("** class name missing **")
        elif arg_inputs[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
        elif len(arg_inputs) == 1:
            print("** instance id missing **")
        else:
            obj_dict = storage.all()
            key = f"{arg_inputs[0]}.{str(arg_inputs[1])}"
            if key not in obj_dict.keys():
                print("** no instance found **")
            else:
                print(obj_dict[key])

    def do_destroy(self, args):
        """Destroys an object based on the Class Name and ID"""
        arg_inputs = args.split(" ")
        obj_dict = models.storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif arg_inputs[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
        elif len(arg_inputs) == 1:
            print("** instance id missing **")
        else:
            key = arg_inputs[0] + "." + arg_inputs[1]
            if key not in obj_dict.keys():
                print("** no instance found **")
            else:
                del obj_dict[key]
                models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = shlex.split(arg)
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            objlist = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objlist.append(obj.__str__())
                elif len(args) == 0:
                    objlist.append(obj.__str__())
            print(objlist)

    def do_update(self, args):
        """Updates attributes of object"""
        updates = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        elif updates[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(updates) == 1:
            print("** instance id missing **")
            return
        elif len(updates) == 2:
            print("** attribute name missing **")
        elif len(updates) == 3:
            print("** value missing **")
        else:
            key = updates[0] + "." + str(updates[1])
            all_instances = storage.all()
            if key not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[key]
                setattr(obj, updates[2], updates[3])
                storage.save()

    def do_count(self, arg):
        """Count all instances of a class"""
        args = arg.split(" ")
        instances = 0
        for obj in models.storage.all().values():
            if args[0] == type(obj).__name__:
                instances += 1
        print(instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
