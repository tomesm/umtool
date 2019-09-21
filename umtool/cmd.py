""" User Management tool Termonal interface """

import sys
import click
from .osx import command

@click.command()
@click.argument('--utility', required=True)


# @click.option('--config_file', default='./auth.cfg',
                # help='A path to a configuration file',
                # type=click.Path(exists=True))
# @click.option('--query', default='#python', help='Searched expression, (eg. #python)')
# @click.option('--init_num', default=5, help='Number of lodaded tweets at the beginning')
# @click.option('--interval', default=10, help='Time interval of next queries')
# @click.option('--retweets', default=False, help='Include retweets?')


def run(utility):
    ''' Run terminal User Management tool '''

    if sys.platform.startswith('darwin'):
        # OSX support
        print("Platform supported")
        command(utility)
    elif sys.platform.startswith('linux'):
        print("Platform not supported")

