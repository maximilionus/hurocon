import unittest

from click.testing import CliRunner

from hurocon.cli import get_cli


class Test_CLI(unittest.TestCase):
    def test_call_root(self):
        runner = CliRunner()
        cli = get_cli()
        result = runner.invoke(cli)

        self.assertEqual(0, result.exit_code)
