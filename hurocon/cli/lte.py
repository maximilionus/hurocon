import click
from huawei_lte_api.Client import Client

from .. import core
from .root import cli


@cli.group()
def lte():
    """ Cellular connection controls """
    pass


@lte.command('status')
def lte_status():
    """ Get cellular connection status """
    try:
        with core.HRC_Connection() as conn:
            con_stat = Client(conn).dial_up.mobile_dataswitch()['dataswitch']
    except Exception as e:
        msg = 'Execution failed, reason: "{}"'.format(e)
    else:
        msg = 'Connected to cellular network' if con_stat == '1' else \
              'No connection to cellular network'

    click.echo(msg)


@lte.command('set')
@click.argument('mode', required=True, type=bool)
def lte_set_connection(mode: bool):
    """
    Enable on disable cellular connection

    MODE: True, False | [Y]es, [N]o | 1, 0
    """
    try:
        with core.HRC_Connection() as conn:
            Client(conn).dial_up.set_mobile_dataswitch(int(mode))
    except Exception as e:
        msg = 'Can not switch connection mode, reason: "{}"'.format(e)
    else:
        msg = 'Successfully {} cellular data'.format('enabled' if mode else 'disabled')

    click.echo(msg)
