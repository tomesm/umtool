""" User Management tool """

import sys
from .osx import OSX

class Umtool:
    """ User management controller class """
    def __init__(self, utility, password, user, shell, group):
        if sys.platform.startswith('darwin'):
            self.handler = OSX(utility, password, user, shell, group)
        elif sys.platform.startswith('linux'):
            print("Platform not supported")

    def execute(self):
        """ Executes commands based on platform """

        self.handler.execute()
