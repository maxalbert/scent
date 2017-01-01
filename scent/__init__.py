# -*- coding: utf-8 -*-

"""
Scent - Easy annotation of smells in your code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2016 by Maximilian Albert.
:license: MIT, see LICENSE for more details.
"""

__title__ = 'scent'
__author__ = 'Maximilian Albert'
__license__ = 'MIT'
__copyright__ = 'Copyright 2016 Maximilian Albert'

from .mark import MissingLabelError

# Added by versioneer
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
