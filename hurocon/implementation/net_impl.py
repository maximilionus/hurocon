from click import echo
from huawei_lte_api.Client import Client

from ..core.connection import HRC_Connection


def cellular_status_impl():
    try:
        with HRC_Connection() as conn:
            con_stat = Client(conn).dial_up.mobile_dataswitch()['dataswitch']
    except Exception as e:
        msg = 'Execution failed, reason: "{}"'.format(e)
    else:
        msg = 'Connected to cellular network' if con_stat == '1' else \
              'No connection to cellular network'

    echo(msg)


def cellular_set_connection_impl(mode: bool):
    try:
        with HRC_Connection() as conn:
            Client(conn).dial_up.set_mobile_dataswitch(int(mode))
    except Exception as e:
        msg = 'Can not switch connection mode, reason: "{}"'.format(e)
    else:
        msg = 'Successfully {} cellular data'.format('enabled' if mode else 'disabled')

    echo(msg)
