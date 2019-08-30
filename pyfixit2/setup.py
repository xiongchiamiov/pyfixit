#!/usr/bin/env python
import os
from setuptools import setup, find_packages

from constants import VERSION

setup(
   name = 'pyfixit2',
   version = VERSION,
   author = 'Baptiste THIVEND',
   author_email = 'baptiste.thivend@insa-lyon.fr',
   url = 'https://github.com/Dynnammo/pyfixit',
   description = 'A Python library wrapping the iFixit API.',
   long_description = open('../README.md').read(),
   long_description_content_type = "text/markdown",
   setup_requires=['wheel'],
   packages = find_packages(),
   license = "WTFPL 2.0",
   # install_requires = [
   #    'requests >= 1.2.0, < 2.0',
   # ],
   # This doesn't actually work for me.  But it should:
   # https://nose.readthedocs.org/en/latest/setuptools_integration.html
   # test_suite = 'nose.collector',
)

