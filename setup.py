from setuptools import setup
from setuptools.command.test import test
from setuptools.command.develop import develop
import configit


test_requirements = [
    'virtualenv == 1.7.1.2',
    'tox == 1.3',
    'pytest == 2.2.4',
    'pylint == 0.25.1',
    'pytest-pep8 == 1.0.2',
]


class DevelopCommand(develop):
    """
    When developing you should always run tests.

    Add test_requirements to install requires and then build env.
    """
    def run(self):
        # augment our requirements to include testing requirements
        tests_require = getattr(self.distribution, 'tests_require', [])
        if tests_require:
            install_requires = self.distribution.install_requires or []
            self.distribution.install_requires = install_requires +\
                 tests_require

        # super only works on new style objects
        # setuptools is behind the times
        develop.run(self)


class TestCommand(test):
    def finalize_options(self):
        # super only works on new style objects
        # setuptools is behind the times
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        from pylint.lint import Run
        Run(['configit', '--reports=n', '--include-ids=y'], exit=False)
        import tox
        tox.cmdline(args=[])


setup(
    name="ConfigIt",
    version=configit.version,
    author="Pictage",
    author_email="dev@pictage.com",
    description=("Python Configurations"),
    long_description=open('README.rst').read(),
    license="MIT",
    keywords="configuration",
    url="https://github.com/pictage/ConfigIt",
    py_modules=["configit"],
    package_data={'configit':["README.rst"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
    ],
    tests_require=test_requirements,
    cmdclass={
        'test': TestCommand,
        'develop': DevelopCommand
    }
)
