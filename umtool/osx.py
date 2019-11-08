from subprocess import call
from subprocess import check_output

def find_group_id() -> str:
    """
    Finds primay group ID and returns as string
    """
    cmd = 'dscl . -list /groups PrimaryGroupID|grep staff|tr -s [:space:]'
    out = check_output([cmd], shell=True)
    res = out.decode('UTF-8').strip('\n').split(' ')
    return res[1]


def find_user_id() -> str:
    """
    Find out the next available user ID
    """
    cmd = "dscl . -list /Users UniqueID|awk '{{print $2}}'|sort -ug|tail -1"
    out = check_output([cmd], shell=True)
    # Decode from bytes to string, remove newline and convert to int
    max = int(out.decode('UTF-8').strip('\n'))
    return str(max + 1)


class OSX:
    """ Class for executing OSX utilities commands """

    def __init__(self, utility, user, shell='/usr/bin/false', group='staff'):
        """
        Class constructor
        """
        self.utility = utility
        # self.password = password
        self.user = user
        self.shell = shell
        self.group = group
        self.base_cmd = ''


    def execute(self):
        """
        Executes commands
        """
        if self.utility == 'useradd':
            self.call_useradd()
        elif self.utility == 'userdel':
            self.call_userdel()
        else:
            print("Command not recognized")


    def osx_call(self, command):
        """
        Real execution of terminal command
        """
        call('sudo -S {}'.format(command), shell=True)


    def call_useradd(self):
        """
        Adds a new user
        """
        base_cmd = 'dscl . -create /Users/{}'.format(self.user)
        self.osx_call(base_cmd)

        userid = base_cmd + ' UniqueID {}'.format(find_user_id())
        self.osx_call(userid)

        group = base_cmd + ' PrimaryGroupID {}'.format(find_group_id())
        self.osx_call(group)


    def call_userdel(self):
        """
        Deletes user
        """
        self.delete_from_groups()

        userdel = 'dscl . -delete /Users/{}'.format(self.user)
        self.osx_call(userdel)

    def delete_from_groups(self):
        """
        Deletes user from his groups
        """
        out = check_output(['groups', '{}'.format(self.user)], shell=True)
        groups = out.decode('UTF-8').strip('\n').split(' ')

        for group in groups:
            cmd = 'dseditgroup -o edit -d {} -t user {}'.format(self.user, group)
            self.osx_call(cmd)







