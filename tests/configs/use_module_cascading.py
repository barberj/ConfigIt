config_dict = {
    'name': 'use level1',
}

level1 = 'here'

import configit
import tests.configs.level2
configit.use(tests.configs.level2)
