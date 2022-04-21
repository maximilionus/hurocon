import click

from . import core


@click.group(
    help='CLI for Huawei LTE routers'
)
def cli():
    pass


@cli.command()
def reboot():
    click.echo('Rebooting the device')
    core.reboot_router()
    click.echo('Reboot requested, router will restart in several moments')


@cli.group()
def config():
    pass


@config.group()  # TODO
def auth():
    pass


if __name__ == '__main__':
    cli()
