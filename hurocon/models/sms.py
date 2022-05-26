from huawei_lte_api.Client import Client

from ..core.connection import HRC_Connection


def get_sms_list_deep(page_depth: int = 1) -> dict:
    """
    SMS deep scanning function

    :param page_depth: Depth of pages to be fetched and scanned, defaults to 1
    :return: Dictionary with all messages in `api.Sms.get_sms_list` style
    """
    messages_all = {'Count': 0, 'Messages': {'Message': []}}

    for selected_page in range(1, 2 if page_depth <= 1 else page_depth):
        with HRC_Connection() as conn:
            messages_current_page = Client(conn).sms.get_sms_list(
                page=selected_page
            )

        if messages_current_page['Count'] == '0':
            break

        messages_all['Count'] = str(
            int(messages_all['Count']) + int(messages_current_page['Count'])
        )

        messages_all['Messages']['Message'].extend(
            messages_current_page['Messages']['Message']
        )

    return messages_all
