import click
from huawei_lte_api.Client import Client

from .root import cli
from ..models.sms import get_sms_list_deep
from ..core.connection import HRC_Connection


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
        with HRC_Connection() as router_con:
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
        with HRC_Connection() as conn:
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
@click.option(
    '--content-trim', '-C', 'content_trim',
    default=40, show_default=True, type=int,
    help='Trim the message content to specified number of characters'
)
def sms_list(page_depth: int, content_trim: int):
    """ List all sms messages content and other meta-data """
    try:
        msg_arr = []
        cli_output = ''

        for selected_page in range(0, page_depth):  # TODO: Re-implement using `..models.sms.get_sms_list_deep()`
            with HRC_Connection() as conn:
                response = Client(conn).sms.get_sms_list(
                    page=selected_page + 1
                )

            if response['Count'] == '0' and selected_page != 0:
                break

            msg_arr.append('• Page: {}\n'.format(selected_page + 1))

            for msg in response['Messages']['Message']:
                msg_arr[selected_page] += '  • ID: {}\n    From: {}\n    When: {}\n    Content: {}\n'.format(
                    msg['Index'], msg['Phone'], msg['Date'], msg['Content'][:content_trim] + '...'
                )

            for page in msg_arr:
                cli_output += page
            cli_output = cli_output[:-1]  # Cut the ending "\n"

    except Exception as e:
        cli_output = 'Can not fetch messages list, reason: "{}"'.format(e)

    click.echo(cli_output)


@sms.command('view')
@click.argument('message_index', type=int)
@click.option(
    '--page-depth', '-D', 'page_depth',
    default=1, show_default=True, type=int,
    help='Depth of pages to be fetched if available'
)
def sms_view(message_index: int, page_depth: int):
    response = {}

    try:
        response = get_sms_list_deep(page_depth)
    except Exception as e:
        cli_output = 'Can not fetch messages list, reason: "{}"'.format(e)
    else:
        message_matched = {}
        for message in response['Messages']['Message']:
            if str(message_index) == message['Index']:
                message_matched = message
                break

        if len(message_matched) > 0:
            cli_output = '• Index: {}\n• From: {}\n• Content: {}' \
                         .format(message_matched['Index'], message_matched['Phone'],
                                 message_matched['Content'])
        else:
            cli_output = '• Message with id "{}" was not found'.format(message_index)

    click.echo(cli_output)
