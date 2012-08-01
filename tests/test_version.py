from unittest import TestCase
import configit


class TestVersion(TestCase):

    def test_version(self):
        assert configit.__version__, 'Unable to get version'
        assert configit.version, 'Unable to get version'
