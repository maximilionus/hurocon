from getpass import getpass

import click

from . import core, meta


# Root CLI handler
@click.group()
@click.version_option(meta.version)
def cli():
    """ Command line interface for Huawei LTE routers """
    pass


# Device commands
@cli.group()
def device():
    """ Device commands """
    pass


@device.command()
def reboot():
    """ Reboot the router without any confirmation prompts """
    try:
        core.reboot_router()
    except Exception as e:
        click.echo('Execution failed, reason: "{}"'.format(e))
    else:
        click.echo('Rebooting the device, router will restart in several moments')


# Auth control
@cli.group()  # TODO
def auth():
    """ Router authentification """
    pass


@auth.command()
def login():
    """ Safely configure all authentification related details for further interactions """
    print('Authentification Configurator\n')
    con_ip = input(
        '(leave empty to use "{}")\n'
        'IP address of router: '
        .format(core.LOCAL_CONFIG_DEFAULT['connection_ip'])
    )
    uname = input('Username: ')
    passwd = getpass('Password: ')

    core.set_auth_details(uname, passwd)
    core.set_connection_details(con_ip if len(con_ip) > 0 else
                                core.LOCAL_CONFIG_DEFAULT['connection_ip']
                                )

    print("\nAuthentification details successfully specified")


@auth.command()
def logout():
    """ Remove all authentification details """
    core.reset_auth_details()
    print("All authentification details removed")


@auth.command(name='test')
def test_connection():
    """ Test connection to router with current auth details """
    test_result = core.test_connection()
    if test_result == 'ok':
        click.echo('Successful Authentification')
    else:
        click.echo('Auth failed, reason: "{}"'.format(test_result))


# SMS commands
@cli.group()
def sms():
    """ SMS commands """
    pass


@sms.command(name='send')
@click.option('-n', '--number', default='', help='Number that message will be sent to')
@click.option('-t', '--text', default='', help='Text of the message to be sent')
def sms_send(number: str, text: str):
    if len(number) == 0:
        number = input('Number: ')
    if len(text) == 0:
        text = input('Text: ')

    print(number, text)
    exit()

    try:
        if core.sms_send(number, text) is True:
            click.echo('SMS sent successfully to {}'.format(number))
        else:
            click.echo('SMS was not sent, wrong number or message size')
    except Exception as e:
        click.echo('Execution failed, reason: "{}"'.format(e))


if __name__ == '__main__':
    cli()
