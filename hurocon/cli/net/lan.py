from click_didyoumean import DYMGroup
from huawei_lte_api.Client import Client

from . import net


@net.group(cls=DYMGroup)
def lan():
    """ Lan connection controls """


@lan.command('list')
def lan_list_connected():
    """ List devices connected to network """
    print("❌ - Proto 😅")
