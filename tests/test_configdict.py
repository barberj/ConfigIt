from unittest import TestCase
from configit import ConfigDict
from py.test import raises


class TestConfigDict(TestCase):

    def test_configdict_instance(self):

        config = ConfigDict()
        assert isinstance(config, ConfigDict), "ConfigDict not created"
        assert isinstance(config, dict), "ConfigDict not created"

    def test_configdict_setattr(self):

        config = ConfigDict()

        config.test = 'value'
        assert config['test'] == 'value', 'Incorrect attribute value'

        config.test = 'updated'
        assert config['test'] != 'value', 'Incorrect attribute value'

        config['test'] = 'new value'
        assert config['test'] == 'new value', 'Incorrect attribute value'

    def test_configdict_getattr(self):

        config = ConfigDict()

        # verify attribute doesn't already exist
        raises(AttributeError, lambda: getattr(config, 'test'))

        config['test'] = 'value'
        assert config['test'] == 'value', 'Incorrect attribute value'
        assert config.test == 'value', 'Incorrect attribute value'

        config.test = 'updated'
        assert config['test'] != 'value', 'Incorrect attribute value'
        assert config.test != 'value', 'Incorrect attribute value'
        assert config['test'] == 'updated', 'Incorrect attribute value'
        assert config.test == 'updated', 'Incorrect attribute value'
        assert getattr(config, 'test') ==\
            'updated', 'Incorrect attribute value'

    def test_configdict_delattr(self):

        config = ConfigDict()

        config['test'] = 'value'

        del config.test
        raises(AttributeError, lambda: getattr(config, 'test'))
