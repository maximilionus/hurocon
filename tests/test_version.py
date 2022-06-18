import unittest
from pathlib import Path

from hurocon import meta


PYPROJECT_TOML_PATH = Path('pyproject.toml')


def fetch_pyproject_version() -> str:
    with open(PYPROJECT_TOML_PATH, 'rt') as file:
        for line in file:
            if line.startswith('version'):
                return line.strip().split(' = ')[1].replace('"', '')


class TestVersionMatch(unittest.TestCase):
    def test_assert_all_versions(self):
        self.assertEqual(meta.version, fetch_pyproject_version())
