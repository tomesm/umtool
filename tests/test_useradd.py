import pytest
import umtool
import configparser


def get_password():
    config = configparser.ConfigParser()
    config.read("test_conf.cfg")
    return config['test']['password']


def test_useradd():
    uname = "test1"
    utility = "useradd"
    password = get_password()


