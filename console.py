#!/usr/bin/python3
import cmd
import re
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    ''' Defines the HBNBCommand interpreter '''

    prompt = '(hbnb) '

    classes = {
        'BaseModel', 'User', 'Place',
        'State', 'City', 'Amenity', 'Review'
    }

    def do_quit(self, line):
        '''
        Description:
        - quits command interpreter when quit is inputed
        -> Usage: quit
        '''
        return True

    def do_EOF(self, line):
        '''
        Description:
        - quits command interpreter on
            EOF marker (if no text in cmd line)
        - performs forward delete if in between two
            characters or line beginning
        -> Usage: Ctrl + D
        '''
        print("")
        return True

    def emptyline(self):
        ''' Do nothing upon receiving an empty line.
            or an empty line + space
        '''
        pass


        ''' implements the default commands  '''
        objects = storage.all().values()
        argv = line.split('.', 1)
        if len(argv) != 2:
            return
        if argv[0] in HBNBCommand.classes and argv[1].endswith('()'):
            command = argv[1][:-2]

            if command == 'all':
                attrs = \
                    [obj for obj in objects if type(obj).__name__ == argv[0]]
                [print(att, end=', ' if att != attrs[-1] else '\n')
                    for att in attrs]
                return

            if command == 'count':
                count = 0
                for obj in objects:
                    if type(obj).__name__ == argv[0]:
                        count += 1
                print(count)
                return

        cls_name = argv[0]
        param = re.search(r"\((.*?)\)", argv[1])
        attributes = re.search(r"\{(.*?)\}", param[1])

        if param:
            method = argv[1][:param.span()[0]]
            param_list = param[1].split(', ', 2)
            id = param_list[0][1:-1]
            if len(param_list) == 1:
                line = ' '.join([cls_name, id])
                eval('self.do_' + method)(line)
            elif not attributes:
                param_list = ' '.join(param_list)
                line = ' '.join([cls_name, param_list])
                eval('self.do_' + method)(line)
            else:
                param_list = param[1].split(', ', 1)
                attr_dict = param_list[1].replace("'", '"')
                line = ' '.join([cls_name, id, attr_dict])
                eval('self.do_' + method)(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
