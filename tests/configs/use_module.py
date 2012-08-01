config_dict = {
    'name': 'use module',
}

some_other_dict = dict(
    foo='bar',
    answer=42
)

import configit
import tests.configs.module_supplement
configit.use(tests.configs.module_supplement)
