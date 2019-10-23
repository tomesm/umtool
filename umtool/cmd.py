""" User Management tool terminal interface """

import sys
import click

from .umtool import Umtool

@click.command()
@click.option('--password', prompt=True, hide_input=True)
#@click.option('-U', '--utility', required=True)
@click.option('-u', '--user', required=True)
@click.option('-s', '--shell', default='/usr/bin/false')
@click.option('-G', '--group', default='staff')
@click.argument('utility', required=True)

def run(utility, password, user, shell, group):
    ''' Run terminal User Management tool '''

    print(utility + ' ' + password + ' ' + user + ' ' + shell + ' ' + group)
    # umtool = Umtool(utility, password, user, shell, group)
    # umtool.execute()
