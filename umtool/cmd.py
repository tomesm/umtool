""" User Management tool Termonal interface """

import sys
import click

from .umtool import Umtool

@click.command()
@click.option('--password', prompt=True, hide_input=True)
@click.option('-U', '--utility', required=True)
@click.option('-u', '--user', required=True)
@click.option('-s', '--shell', default='/usr/bin/false')
@click.option('-G', '--group', default='staff')

def run(password, utility, user, shell, group):
    ''' Run terminal User Management tool '''

    umtool = Umtool(utility, password, user, shell, group)
    umtool.execute()
