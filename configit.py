import inspect
import os
import sys
import warnings
warnings.simplefilter("always")

__version__ = (0,1,2)
version = '.'.join(map(str,__version__))

try:
    unicode
except NameError:
    # Python 3
    basestring = unicode = str


class ConfigDict(dict):
    '''
    Dictionary supporting attribute read & write access.

    :raise AttributeError: Attempted to read an invalid attribute
    '''
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            # to conform with __getattr__ spec
            raise AttributeError(key)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        del self[key]


def use(conf_source):
    '''
    Include configurations in local configuration dictionary.

    :param conf_source: The path string or
    module to include in configuration.
    '''

    if isinstance(conf_source, basestring):
        conf_dict = from_file(conf_source)
    elif inspect.ismodule(conf_source):
        conf_dict = from_module(conf_source)

    _locals_dict = sys._getframe(1).f_locals
    _locals_dict.update(conf_dict)


def conf_from_module(module):
    warnings.warn("Deprecated. Use configit.from_module", DeprecationWarning)
    return from_module(module)

def from_module(module):
    '''
    Creates a configuration dictionary from a module.

    :param module: The module, either as a string or the module itself.
    '''

    if isinstance(module, str):
        module = import_module(module)
    module_dict = dict(inspect.getmembers(module))
    conf_dict = from_dict(module_dict)

    return conf_dict


def conf_from_file(filepath):
    warnings.warn("Deprecated. Use configit.from_file", DeprecationWarning)
    return from_file(filepath)

def from_file(filepath):
    '''
    Creates a configuration dictionary from a file.

    :param filepath: The path to the file.
    '''

    abspath = os.path.abspath(os.path.expanduser(filepath))
    conf_dict = {}

    try:
        exec(compile(open(abspath).read(), abspath, 'exec'),
             globals(), conf_dict)
    except IOError as ioerror:
        raise IOError('Error while trying to get configuration from file: '
                      '%s\n'
                      '%s' % (abspath, ioerror))

    conf_dict = from_dict(conf_dict)
    conf_dict['__config_file__'] = abspath

    return conf_dict


def conf_from_dict(conf_dict):
    warnings.warn("Deprecated. Use configit.from_file", DeprecationWarning)
    return from_dict(conf_dict)

def from_dict(conf_dict):
    '''
    Creates a configuration dictionary from a dictionary.

    :param dictionary: The dictionary.
    '''

    conf = ConfigDict()

    for k, v in conf_dict.items():
        if k.startswith('__'):
            continue
        if inspect.ismodule(v):
            continue
        if isinstance(v, dict):
            v = from_dict(v)

        conf[k] = v
    return conf


def import_module(conf):
    '''
    Imports the configuration as a module.

    :param conf: The string to the configuration.
    Automatically strips off ".py" file extensions.
    '''

    if '.' in conf:
        parts = conf.split('.')
        name = '.'.join(parts[:-1])
        fromlist = parts[-1:]

        try:
            module = __import__(name, fromlist=fromlist)
            conf_mod = getattr(module, parts[-1])
        except AttributeError:
            raise ImportError('No module named %s' % conf)
    else:
        conf_mod = __import__(conf)

    return conf_mod
