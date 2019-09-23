from subprocess import call


class OSX:
    """ Class for executing OSX utilities commands """

    def __init__(self, utility, password, user):
        """ Class constructor """
        self.utility = utility
        self.password = password
        self.user = user


    def execute(self):
        """ Executes commands """
        if self.utility == 'useradd':
            self.call_useradd()
        elif self.utility == 'userdel':
            self.call_userdel()
        else:
            print("Command not recognized")

    def call_useradd(self):
        """ Adds user """
        adduser = 'dscl . -create /Users/{}'.format(self.user)
        call('echo {} | sudo -S {}'.format(self.password, adduser), shell=True)

    def call_userdel(self):
        """ Deletes user """
        userdel = 'dscl . -delete /Users/{}'.format(self.user)
        command = 'echo {} | sudo -S {}'.format(self.password, userdel)
        call(command, shell=True)

