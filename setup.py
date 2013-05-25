#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = ['passwords']

setup(
    name='passwords',
    version='0.2.0',
    description='Passwords for everyone.',
    author='Jonathan Cremin',
    author_email='jonathan@crem.in',
    url='http://github.com/kudos/passwords',
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'passwords': 'passwords'},
    include_package_data=True,
    license=open('LICENSE').read(),
    classifiers=(
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ),
)
