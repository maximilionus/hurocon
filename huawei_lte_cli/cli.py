from getpass import getpass

import click

from . import core


# Root CLI handler
@click.group(
    help='CLI for Huawei LTE routers'
)
def cli():
    pass


# Main commands
@cli.command()
def reboot():
    try:
        core.reboot_router()
    except Exception as e:
        click.echo('Execution failed, reason: "{}"'.format(e))
    else:
        click.echo('Rebooting the device, router will restart in several moments')


# Auth control
@cli.group()  # TODO
def auth():
    pass


@auth.command()
def login():
    """ safely configure all authentification related details for further interactions """
    print('Authentification Configurator\n')
    con_ip = input('IP Address of router: ')
    uname = input('Username: ')
    passwd = getpass('Password: ')

    core.write_auth_details(uname, passwd)
    core.set_connection_details(con_ip)

    print("\nAuthentification details successfully specified")


@auth.command()
def logout():
    """ remove all authentification details """
    core.reset_auth_details()
    print("All authentification details removed")


@auth.command(name='test')
def test_connection():
    """ test connection with router """
    test_result = core.test_connection()
    if test_result == 'ok':
        click.echo('Successful Authentification')
    else:
        click.echo('Auth failed, reason: "{}"'.format(test_result))


if __name__ == '__main__':
    cli()
