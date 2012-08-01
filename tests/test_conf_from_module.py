from unittest import TestCase
from configit import conf_from_module


class TestConfFromModule(TestCase):

    def test_configdict_values(self):
        import tests.configs.module_config

        config = conf_from_module(tests.configs.module_config)
        assert config.config_type == 'module'
        assert config['config_dict']['name'] == 'module_config'

        assert config['some_other_dict']['foo'] == 'bar'
        assert config.some_other_dict['answer'] == 42
