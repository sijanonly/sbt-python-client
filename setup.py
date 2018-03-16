# -*- coding: utf-8 -*-
# @Author: Sijan
# @Date:   2018-03-14 15:55:52
# @Last Modified time: 2018-03-16 10:11:56


from distutils.core import setup

import sys

from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='sbt-python-client',
    version='1.0.2',
    packages=['solutions_by_text', 'solutions_by_text.test'],
    url='http://pypi.python.org/pypi/SolutionsByText',
    license='MIT',
    author='Sijan Bhandari',
    author_email='sijanonly@gmail.com',
    description='A python implementation of solutions by text REST API',
    long_description=open('README.txt').read(),
    install_requires=[
        "requests",
    ],
    tests_require=['pytest'],
    cmdclass={'test': PyTest},

)
