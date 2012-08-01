config_dict = {
    'name': 'withimport',
}

some_other_dict = dict(
    foo='bar',
    answer=42
)

import tests.configs.extraconfig as extraconfig
an_extra_dict = extraconfig.anextradict
an_extra_variable = extraconfig.anextravariable
