from unittest import TestCase
from configit import conf_from_file


class TestUse(TestCase):

    def test_use_module(self):
        filepath = r'tests/configs/use_module.py'
        config = conf_from_file(filepath)

        assert config.config_dict['name'] == 'use module'
        assert config.config_type == 'module_supplement'

    def test_use_module_as(self):
        filepath = r'tests/configs/use_module_as.py'

        config = conf_from_file(filepath)
        assert config.config_dict.name == 'use module with as'
        assert config.config_type == 'module_supplement'

    def test_use_file(self):
        filepath = r'tests/configs/use_file.py'
        config = conf_from_file(filepath)

        assert config.config_dict['name'] == 'use file'
        assert config.config_type == 'file_supplement'

    def test_use_order(self):
        filepath = r'tests/configs/use_order_test.py'
        config = conf_from_file(filepath)

        assert config.config_dict['name'] == 'use file'
        assert config.config_type == 'module_supplement'
        assert config.some_other_dict.foo == 'bar'

    def test_use_order_2(self):
        filepath = r'tests/configs/use_order_test_2.py'
        config = conf_from_file(filepath)

        assert config.config_dict['name'] == 'use module'
        assert config.config_type == 'file_supplement'
        assert config.some_other_dict.foo == 'bar'

    def test_use_module_cascading(self):
        filepath = r'tests/configs/use_module_cascading.py'
        config = conf_from_file(filepath)

        assert config.config_dict['name'] == 'use level3'
        assert config.level1 == 'here'
        assert config.level2 == 'here'
        assert config.level3 == 'here'

    def test_use_file_cascading(self):
        filepath = r'tests/configs/use_file_cascading.py'
        config = conf_from_file(filepath)

        assert config.config_dict['name'] == 'use level3'
        assert config.level1 == 'here'
        assert config.level2 == 'here'
        assert config.level3 == 'here'
