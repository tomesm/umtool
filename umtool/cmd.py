""" User Management tool Termonal interface """

import sys
import click

from .umtool import Umtool

# from .umtool import Umtool

@click.command()
@click.option('--password', prompt=True, hide_input=True)
@click.option('-U', '--utility', required=True)
@click.option('-u', '--user', required=True)


def run(password, utility, user):
    ''' Run terminal User Management tool '''

    umtool = Umtool(utility, password, user)
    umtool.execute()
