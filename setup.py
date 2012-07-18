#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import os, re

path = os.path.join(os.path.dirname(__file__), 'gshell', '__init__.py')
init_py = open(path).read()
VERSION = re.match("__version__ = '([^']+)'", init_py).group(1)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    scripts= ['scripts/upyun-ft']
    name = 'upyun-ft',
    version = VERSION,
    url = 'https://geakit.com/dingyan/upyun-ft',
    license = 'BSD',
    description = "Upyun File Transfer based on Python API",
    long_description=read('README.rst'),
    author = 'Michael Ding',
    author_email = 'dingyan@{nospam}freestorm.org',
    packages = ['upyun'],
    test_suite = 'tests',
    classifiers = [
        'Environment :: Console',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: System Administrators',
        'License :: License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: System :: Systems Administration :: Authentication/Directory'
    ]
)
