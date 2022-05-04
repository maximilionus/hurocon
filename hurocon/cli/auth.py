from getpass import getpass

import click

from .. import core
from .root import cli


@cli.group()
def auth():
    """ Router authentification """
    pass


@auth.command('login')
def auth_login():
    """ Safely configure all authentification related details for further interactions """
    print('Authentification Configurator\n')
    con_ip = input(
        '(leave empty to use "{}")\n'
        'Full address to router: '
        .format(core.LOCAL_CONFIG_DEFAULT['connection_address'])
    )
    uname = input('Username: ')
    passwd = getpass('Password: ')

    auth_cfg = core.AuthConfig()
    auth_cfg.username = uname
    auth_cfg.password = passwd
    auth_cfg.connection_address = con_ip if len(con_ip) > 0 else \
        core.LOCAL_CONFIG_DEFAULT['connection_address']

    auth_cfg.commit()

    print("\nAuthentification details successfully specified")


@auth.command('logout')
def auth_logout():
    """ Remove all authentification details """
    core.AuthConfig().reset()
    core.AuthConfig().commit()
    print("All authentification details removed")


@auth.command('test')
def auth_test_connection():
    """ Test connection to router with current auth details """
    test_result = core.test_connection()
    if test_result == 'ok':
        click.echo('Successful Authentification')
    else:
        click.echo('Auth failed, reason: "{}"'.format(test_result))