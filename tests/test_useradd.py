import pytest
import umtool
import configparser
import subprocess

from umtool import OSX

def get_password():
    config = configparser.ConfigParser()
    config.read("test_conf.cfg")
    return config['test']['password']


def get_users():
    cmd = 'dscl . -list /Users'
    out = subprocess.check_output([cmd], shell=True)
    res = out.decode('UTF-8').strip('\n').split(' ')
    return res[1]

def extecute(cmd):
    subprocess.call('echo {} | sudo -S {}'.format(get_password(), cmd), shell=True)


def test_useradd():
    uname = "test1"
    utility = "useradd"
    password = get_password()
    osx = OSX(utility, password, uname)

    print(get_users())

