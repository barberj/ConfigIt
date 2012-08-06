ConfigIt
========

.. image:: TODO

ConfigIt is MIT Licensed Python Configuration library brought to you
by the camera shy people at `Pictage <http://www.pictage.com>`_.

Python is all about the dicts so why do we settle for `INIs <http://en.wikipedia.org/wiki/INI_file>`_?


Features
--------

All configuration files are native python files.

Using ConfigIt you can read those files in as a module, or file
and return a dictionary with attribute access.

One of the most powerful things about configit is its ability to use other
configurations within a configuration.


Installation
------------

To install configit, simply: ::

    $ pip install configit


API Documentation
-----------------


configit.conf_from_file(filepath)
    Reads a string file path and returns a ConfigDict. ::
    filepath = r'tests/configs/default.py'

    config = conf_from_file(filepath)
    assert config.config_dict.name == 'default'

configit.conf_from_module(module)
configit.conf_from_dict(conf_dict)
configit.use(conf_source)


Contribution
------------

#. Fork `the repository`_ on Github.
#. Install to your env or venv by running: ::

    $ python setup.py develop

#. Hack-a-thon, dance party!
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Test by running: ::

    $ python setup.py test

#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.

.. _`the repository`: http://github.com/pictage/ConfigIt
.. _AUTHORS: https://github.com/pictage/ConfigIt/blob/master/AUTHORS.rst
