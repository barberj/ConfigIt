config_dict = {
    'name': 'use module with as',
}

import configit
import tests.configs.module_supplement as module_supplement
configit.use(module_supplement)
