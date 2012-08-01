from unittest import TestCase
from configit import conf_from_module


class TestModuleConfig(TestCase):

    def test_conf_from_module(self):
        import tests.configs.default
        config = conf_from_module(tests.configs.default)
        assert config.config_dict.name == 'default'
        assert config.some_other_dict.foo == 'bar'
        assert config['some_other_dict']['answer'] == 42

    def test_conf_from_module_as(self):
        import tests.configs.default as default_conf
        config = conf_from_module(default_conf)
        assert config.config_dict.name == 'default'
        assert config.some_other_dict.foo == 'bar'
        assert config['some_other_dict']['answer'] == 42
