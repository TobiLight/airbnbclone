#!/usr/bin/python3
# File: console.py
# Author: Oluwatobiloba Light
"""
Entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def do_EOF(self, line):
        """Exit the program using EOF (Ctrl+D)"""
        print()
        return True
    
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """Do nothing on  empty line"""
        pass
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()