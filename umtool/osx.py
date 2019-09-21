import subprocess


def command(utility, **args):
    if utility == "adduser":
        adduser(**args)


def adduser(**args):
    subprocess.run(["ls", "-l"])

