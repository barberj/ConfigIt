config_dict = {
    'name': 'use file',
}

some_other_dict = dict(
    foo='bar',
    answer=42
)

import configit
configit.use('tests/configs/file_supplement.py')
