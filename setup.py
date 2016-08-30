"""Scent - Easy annotation of code smells.

See: https://github.com/maxalbert/scent
"""

#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path
from scent import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='scent',
    version=__version__,
    description='Easy annotation of code smells.',
    long_description=long_description,
    url='https://github.com/maxalbert/scent',
    author='Maximilian Albert',
    author_email='maximilian.albert@gmail.com',
    license='MIT',
    packages=['scent'],
    install_requires=[],
    tests_require=['pytest', 'pytest-cov'],

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='refactoring code-smells documentation',
)
