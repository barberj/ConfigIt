from unittest import TestCase
from py.test import raises
from configit import conf_from_file


class TestConfFromFile(TestCase):

    def test_file_path_added(self):
        filepath = r'tests/configs/default.py'

        config = conf_from_file(filepath)
        assert filepath in config.__config_file__,\
            'Configuration File path not added to config'

    def test_no_file(self):
        filepath = r'tests/configs/does_not_exist.py'

        raises(IOError, lambda: conf_from_file(filepath))

    def test_configdict_values(self):
        filepath = r'tests/configs/default.py'

        config = conf_from_file(filepath)
        assert config.config_dict['name'] == 'default'
        assert config['config_dict']['name'] == 'default'

        assert config['some_other_dict']['foo'] == 'bar'
        assert config.some_other_dict['answer'] == 42

    def test_configuration_with_import(self):
        filepath = r'tests/configs/withimport.py'

        config = conf_from_file(filepath)
        assert config.config_dict['name'] == 'withimport'
        assert config.some_other_dict['foo'] == 'bar'
        assert config.an_extra_dict['so_long'] == 'Thanks for all the fish'
        assert config.an_extra_variable == 'another configuration'

    def test_recursive_dicts(self):
        filepath = r'tests/configs/recursive_config.py'

        config = conf_from_file(filepath)
        assert config.config_dict.name == 'recursive'
        assert config.some_other_dict.answer == 42
        assert config.recursive_test.first.second.last == 3.14

    def test_recursive_configdicts(self):
        filepath = r'tests/configs/recursive_w_configdict.py'

        config = conf_from_file(filepath)
        assert config.config_dict.name == 'recursive with configdict'
        assert config.some_other_dict.answer == 42
        assert config.recursive_test.first.second.last == 7.28
        assert config.onions.lots.oflayers == 'bam!'
