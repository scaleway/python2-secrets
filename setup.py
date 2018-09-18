#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

from setuptools import find_packages, setup

MODULE_NAME = 'secrets'

PACKAGE_NAME = 'python2-secrets'


def find_file(*paths):
    """ Builds path from arguments. """
    return os.path.join(os.path.dirname(__file__), *paths)


def get_version():
    """ Reads package version number from package's __init__.py. """
    with open(find_file(MODULE_NAME, '__init__.py')) as init:
        for line in init.readlines():
            res = re.match(r'^__version__ = [\'"](.*)[\'"]$', line)
            if res:
                return res.group(1)


def get_long_description():
    """ Read description from README and CHANGES. """
    with open(find_file('README.md')) as readme, \
        open(find_file('CHANGES.md')) as changes:
        return readme.read() + '\n' + changes.read()


setup(
    name=PACKAGE_NAME,
    version=get_version(),
    description='Backport of secrets for python2',
    long_description=get_long_description(),

    author='Scaleway',
    author_email='opensource@scaleway.com',
    url='https://github.com/scaleway/python2-secrets',
    packages=find_packages(),
    python_requires='>= 2.7, != 3.*.*',
    dependency_links=[
    ],
    test_suite=MODULE_NAME + '.tests',
    classifiers=[
        # See: https://pypi.python.org/pypi?:action=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        # List of python versions and their support status:
        # https://en.wikipedia.org/wiki/CPython#Version_history
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Security'
    ],
    package_data={},
)
