import unittest

from libpyhat.fileio import io_json
from libpyhat.fileio import io_yaml

try:
    import yaml

    missing = False
except ImportError:
    missing = True

from libpyhat.examples import get_path


class TestYAML(unittest.TestCase):
    @unittest.skipIf(missing == True, 'YAML library not installed')
    def test_read(self):
        d = io_yaml.read_yaml(get_path('logging.yaml'))
        self.assertIn('handlers', d.keys())


class TestJSON(unittest.TestCase):
    def test_read(self):
        d = io_json.read_json(get_path('logging.json'))
        self.assertIn('handlers', d.keys())