""" Input/Output wrappers """
import textwrap


def printx(*text, limit_line_length: bool = False):
    """ Enhanced long-text printing function """
    final_text = ''
    for line in text:
        line_processed = str(line)
        final_text += prettify(line_processed) if limit_line_length else line_processed

    print(final_text)


def prettify(text) -> str:
    return textwrap.fill(
        text,
        width=80,
        tabsize=4,
        replace_whitespace=False
    )
