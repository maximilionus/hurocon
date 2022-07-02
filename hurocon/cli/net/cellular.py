import click
from click_didyoumean import DYMGroup
from huawei_lte_api.Client import Client

from . import net
from ...core.connection import HRC_Connection


@net.group(cls=DYMGroup)
def cellular():
    """ Cellular connection controls """
    pass


@cellular.command('status')
def cellular_status():
    """ Get cellular connection status """
    try:
        with HRC_Connection() as conn:
            con_stat = Client(conn).dial_up.mobile_dataswitch()['dataswitch']
    except Exception as e:
        msg = 'Execution failed, reason: "{}"'.format(e)
    else:
        msg = 'Connected to cellular network' if con_stat == '1' else \
              'No connection to cellular network'

    click.echo(msg)


@cellular.command('set')
@click.argument('mode', required=True, type=bool)
def cellular_set_connection(mode: bool):
    """
    Enable or disable cellular connection

    MODE (bool): True, False | [Y]es, [N]o | 1, 0
    """
    try:
        with HRC_Connection() as conn:
            Client(conn).dial_up.set_mobile_dataswitch(int(mode))
    except Exception as e:
        msg = 'Can not switch connection mode, reason: "{}"'.format(e)
    else:
        msg = 'Successfully {} cellular data'.format('enabled' if mode else 'disabled')

    click.echo(msg)
