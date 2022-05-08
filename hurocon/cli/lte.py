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
    try:
        with core.HRC_Connection() as conn:
            client = Client(conn)
            lte_status = client.dial_up.mobile_dataswitch()['dataswitch']  # {'dataswitch': '1'}

        msg = 'Connected to cellular network' if lte_status == '1' else \
              'No connection to cellular network'
    except Exception as e:
        msg = 'Execution failed, reason: "{}"'.format(e)
    finally:
        click.echo(msg)
