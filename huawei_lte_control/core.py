from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection
from huawei_lte_api.enums.device import ControlModeEnum


class HLC_Connection(Connection):
    def __init__(self):
        super().__init__(url='http://admin:PASSWORD@192.168.8.1/')  # TODO: Values should be configurable


def reboot_router():
    with HLC_Connection() as router_con:
        client = Client(router_con)
        client.device.set_control(ControlModeEnum.REBOOT)
