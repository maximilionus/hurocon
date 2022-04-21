from pathlib import Path

from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection
from huawei_lte_api.enums.device import ControlModeEnum

from serialix import Serialix


LOCAL_CONFIG_PATH = Path.home() / Path('.config/huawei_lte_cli/config.json')
LOCAL_CONFIG_DEFAULT = {
    "config_version": 1,
    "connection_ip": "192.168.8.1",
    "auth": {
        "username": "admin",
        "password": "admin"
    }
}


class LocalConfig(Serialix):
    def __new__(self):
        return super().__new__(
            self, 'json',
            LOCAL_CONFIG_PATH, LOCAL_CONFIG_DEFAULT,
            parser_write_kwargs={"indent": 4}
        )


class HLC_Connection(Connection):
    def __init__(self):
        cfg = LocalConfig()
        super().__init__(
            url='http://{}/'.format(cfg['connection_ip']),
            username=cfg['auth']['username'],
            password=cfg['auth']['password']
        )


def reboot_router():
    with HLC_Connection() as router_con:
        client = Client(router_con)
        client.device.set_control(ControlModeEnum.REBOOT)
