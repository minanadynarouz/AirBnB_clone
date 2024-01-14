#!/usr/bin/python3
"""Console App to control website"""

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """ HBNB Class """
    prompt = '(hbnb) '


    def do_EOF(self, arg):
        """End of the command line interpreter"""
        print("")
        return True

    def help_EOF(self):
        """ Prints the help documentation for EOF """
        print("EOF command to exit the program\n")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """ Prints the help documentation for quit  """
        print("Quit command to exit the program\n")

    def emptyline(self):
        """Overrides default behavior not to print new line"""
        pass

if __name__ == '__main__':
    """infinite loop"""
    HBNBCommand().cmdloop()
