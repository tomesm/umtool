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
    res = out.decode('UTF-8').split('\n')
    return res


@pytest.fixture
def osx():
    uname = "test1"
    utility = "useradd"
    password = get_password()
    return OSX(utility, password, uname)


def test_useradd(osx):
    osx.call_useradd()
    assert "test1" in get_users()


def test_userdel(osx):
    osx.call_userdel()
    assert "test1" not in get_users()



