from pprint import pformat

import click

from .. import core
from .root import cli


@cli.group()
def device():
    """ Device commands """
    pass


@device.command('info')
def device_info():
    """ Get device information """
    try:
        device_info_str = pformat(core.get_device_info())
    except Exception as e:
        device_info_str = 'Can not get device information, reason: "{}"' \
            .format(e)

    click.echo(device_info_str)


@device.command('reboot')
def device_reboot():
    """ Reboot the router without any confirmation prompts """
    try:
        core.reboot_device()
    except Exception as e:
        click.echo('Execution failed, reason: "{}"'.format(e))
    else:
        click.echo('Rebooting the device, router will restart in several moments')
