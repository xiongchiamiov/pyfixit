#!/usr/bin/env python
import os
import setuptools
from distutils.core import setup

from constants import VERSION

# I really prefer Markdown to reStructuredText.  PyPi does not.  This allows me
# to have things how I'd like, but not throw complaints when people are trying
# to install the package and they don't have pypandoc or the README in the
# right place.
try:
   import pypandoc
   description = pypandoc.convert_file('README.md','rst')
except (OSError, IOError, ImportError):
   description = ''

try:
   license = open('LICENSE').read()
except IOError:
   license = 'WTFPL 2.0'

setup(
   name = 'pyfixit2',
   version = VERSION,
   author = 'James Pearson',
   author_email = 'pearson@changedmy.name',
   packages = ['pyfixit2'],
   url = 'https://github.com/Dynnammo/pyfixit',
   license = license,
   description = 'A Python library wrapping the iFixit API.',
   long_description = description,
   setup_requires=['wheel'],
   # install_requires = [
   #    'requests >= 1.2.0, < 2.0',
   # ],
   # This doesn't actually work for me.  But it should:
   # https://nose.readthedocs.org/en/latest/setuptools_integration.html
   # test_suite = 'nose.collector',
)

