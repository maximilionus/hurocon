import click

from .. import core
from .root import cli


@cli.group()
def device():
    """ Device commands """
    pass


@device.command('reboot')
def device_reboot():
    """ Reboot the router without any confirmation prompts """
    try:
        core.reboot_router()
    except Exception as e:
        click.echo('Execution failed, reason: "{}"'.format(e))
    else:
        click.echo('Rebooting the device, router will restart in several moments')
