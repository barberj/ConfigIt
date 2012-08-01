config_dict = {
    'name': 'use level2',
}

level2 = 'here'

import configit
import tests.configs.level3 as level3
configit.use(level3)
