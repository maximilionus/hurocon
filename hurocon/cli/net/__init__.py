from click_didyoumean import DYMGroup

from ..__cli_base__ import cli


@cli.group(cls=DYMGroup)
def net():
    """ Network controls """
    pass


from . import cellular, lan
