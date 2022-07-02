import click
from click_didyoumean import DYMGroup

from .cli_base import cli
from ..implementation import net_impl


@cli.group(cls=DYMGroup)
def net():
    """ Network controls """
    pass


# Cellular cli group
@net.group(cls=DYMGroup)
def cellular():
    """ Cellular connection controls """
    pass


@cellular.command('status')
def cellular_status():
    """ Get cellular connection status """
    net_impl.cellular_status_impl()


@cellular.command('set')
@click.argument('mode', required=True, type=bool)
def cellular_set_connection(mode: bool):
    """
    Enable or disable cellular connection

    MODE (bool): True, False | [Y]es, [N]o | 1, 0
    """
    net_impl.cellular_set_connection_impl(mode)


# LAN cli group
@net.group(cls=DYMGroup)
def lan():
    """ Lan connection controls """


@lan.command('list')
def lan_list_connected():
    """ List devices connected to network """
    # ! Implement this before stable release or hide it 👍
    print("❌ - proto for 'huawei_lte_api.api.WLan.host_list' 😅")
