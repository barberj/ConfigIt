from setuptools import setup
from setuptools.command.test import test as TestCommand
from setuptools import Command
import configit

test_requirements = [
    'virtualenv == 1.7.1.2',
    'tox == 1.3',
    'pytest == 2.2.4',
    'pylint == 0.25.1',
    'pytest-pep8 == 1.0.2',
]

extra_requirements = dict(
    docs='sphinx == 1.1.3'
)


class ToxTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        from pylint.lint import Run
        Run(['configit', '--reports=n', '--include-ids=y'], exit=False)
        import tox
        tox.cmdline(args=[])


class GenDocs(Command):
    description = "Generate ConfigIt Documentation"
    user_options = []

    def initialize_options(self):
        """init options"""
        pass

    def finalize_options(self):
        """finalize options"""
        pass

    def run(self):
        """runner"""
        if self.distribution.extras_require:
            self.distribution.fetch_build_eggs(
                self.distribution.extras_require['docs']
            )
        print('runner')

setup(
    name="ConfigIt",
    version=configit.__version__,
    author="Pictage",
    author_email="dev@pictage.com",
    description=("Python Configurations"),
    license="MIT License",
    keywords="configuration",
    url="http://pictage.com",
    py_modules=["configit"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: Proprietary",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
    ],
    tests_require=test_requirements,
    extras_require=extra_requirements,
    cmdclass={
        'test': ToxTest,
        'docs': GenDocs
    }
)
