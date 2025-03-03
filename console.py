#!/usr/bin/python3
"""
Implements a custom Python shell
using cmd module
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Implements a Python class that
    inherits from cmd module
    """
    class_reference = ["BaseModel", "User", "Place", "State",
                       "City", "Amenity", "Review"]
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """
        Exit the program
        Usage: (ctrl + D)
        """
        print()
        return True

    def do_quit(self, line):
        """
        Exit the program
        Usage: quit
        """
        return True

    def emptyline(self):
        """No action is taken for an empty line"""

    def do_create(self, line):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        Usage: create <class_name> <name>
        """
        arguments = shlex.split(line)
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.class_reference:
            print("** class doesn't exist **")
        else:
            new_instance = eval("{}()".format(arguments[0]))
            storage.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation
        of an instance based on the class name and id
        Usage: show <class_name> <id>
        """
        arguments = shlex.split(line)
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.class_reference:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            obj_key = f"{arguments[0]}.{arguments[1]}"
            if obj_key not in objects:
                print("** no instance found **")
            else:
                print(objects[obj_key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name
        and id (save the change into the JSON file)
        """
        arguments = shlex.split(line)
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.class_reference:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            obj_key = f"{arguments[0]}.{arguments[1]}"
            if obj_key not in objects:
                print("** no instance found **")
            else:
                del objects[obj_key]
                storage.save()

    def do_all(self, line):
        """Prints all string representations of
        instances based on the class name (optional)
        Usage: all -optional <class name>
        """
        # shlex.split() does not contain the command (line[0])
        # for input __all User__, contents of arguments list
        # will be ['User']
        arguments = shlex.split(line)
        # print(f"hhh{arguments}")
        instances = storage.all()

        spec_cls = arguments[0] if arguments else None

        if spec_cls and spec_cls not in HBNBCommand.class_reference:
            print("** class doesn't exist **")
        else:
            for key, value in instances.items():
                if not spec_cls or spec_cls == key.split('.')[0]:
                    print(str(value))

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating attribute
        (save the change into the JSON file)
        Usage: update <class name> <id>
        <attribute name> "<attribute value>"
        """
        arguments = shlex.split(line)
        if not arguments:
            print("** class name missing **")
        elif arguments[0] not in HBNBCommand.class_reference:
            print("** class doesn't exist **")
        elif len(arguments) == 1:
            print("** instance id missing **")
        else:
            objects = storage.all()
            obj_key = f"{arguments[0]}.{arguments[1]}"
            if obj_key not in objects:
                print("** no instance found **")
            elif len(arguments) < 3:
                print("** attribute name missing **")
            elif len(arguments) < 4:
                print("** value missing **")
            else:
                instance = objects[obj_key]

                attr_name = arguments[2]
                attr_value = arguments[3]

                try:
                    attr_value = eval(attr_value)
                except Exception:
                    pass
                setattr(instance, attr_name, attr_value)
                instance.save()

    def do_count(self, line):
        """Prints the number of instances based on the class name (optional)
        Usage: count -optional <class name>
        """
        arguments = shlex.split(line)
        instances = storage.all()

        spec_cls = arguments[0] if arguments else None

        if spec_cls and spec_cls not in HBNBCommand.class_reference:
            print("** class doesn't exist **")
        else:
            count = sum(1 for key in instances.keys()
                        if not spec_cls or spec_cls == key.split('.')[0])
            print(count)

    def default(self, line):
        """Handles unknown command and syntax error"""
        arguments = line.split('.')
        # To avoid IndexRangeError when unpacking for split
        # and one or more than two CLI
        if len(arguments) != 2:
            print(f"**Unknown syntax {line}")
            return False
        # single line assignment
        class_name, command_part = arguments
        arg_method, _ = (command_part.split('(') if '(' in
                         command_part else (command_part, ''))

        # dictionary of available methods for reference
        dict_of_methods = {
            'all': self.do_all,
            'count': self.do_count,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update
        }
        # check If args exist in already defined dictionary
        # and execute the corresponding method call
        # Not need to check if class_name exist as all methods
        # have this check
        if arg_method in dict_of_methods:
            # Pass the entire line (excluding class_name) as arguments
            return dict_of_methods[arg_method](f"{class_name} {_}")
        else:
            print(f"**Unknown Method '{arg_method}' in {class_name}")
            return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
