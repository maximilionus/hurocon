import click
from huawei_lte_api.Client import Client

from .. import core
from .root import cli


@cli.group()
def sms():
    """ SMS commands """
    pass


@sms.command('send')
@click.option('-n', '--number', default='', help='Number that message will be sent to')
@click.option('-t', '--text', default='', help='Text of the message to be sent')
def sms_send(number: str, text: str):
    if len(number) == 0:
        number = input('Number: ')
    if len(text) == 0:
        text = input('Text: ')

    try:
        with core.HRC_Connection() as router_con:
            send_status = Client(router_con).sms.send_sms(
                [number],
                text
            )

        if send_status.lower() == 'ok':
            click.echo('SMS sent successfully to {}'.format(number))
        else:
            click.echo('SMS was not sent, reason: "{}"'.format(send_status))
    except Exception as e:
        click.echo('Execution failed, reason: "{}"'.format(e))


@sms.command('count')
def sms_count_all():
    """ Get overall information about stored sms messages """
    try:
        with core.HRC_Connection() as conn:
            sms_count_dict = Client(conn).sms.sms_count()
    except Exception as e:
        cli_output = 'Can not get sms information, reason: "{}"'.format(e)
    else:
        cli_output = ''
        for key, value in sms_count_dict.items():
            cli_output += '• {}: {}\n'.format(key, value)
        cli_output = cli_output[:-1]

    click.echo(cli_output)


@sms.command('list')
@click.option(
    '--page-depth', '-D', 'page_depth',
    default=1, show_default=True, type=int,
    help='Depth of pages to be fetched if available'
)
def sms_list(selected_page: int):
    try:
        with core.HRC_Connection() as conn:
            response = Client(conn).sms.get_sms_list(
                page=selected_page
            )

            if response['Count'] == '0':
                result = 'No messages on this page'
            else:
                msg_formed = ()
                for msg in response['Messages']['Message']:
                    pass

                result = 'Count: {}' \
                         '\n\nMessages:' \
                         .format(response['Count'])
    except Exception as e:
        result = 'Can not fetch messages list, reason: "{}"'.format(e)

    click.echo(result)
