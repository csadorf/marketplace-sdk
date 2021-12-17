#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Software Development Toolkit to communicate with the Materials MarketPlace platform.

.. currentmodule:: marketplace
.. moduleauthor:: Carl Simon Adorf <simon.adorf@epfl.ch>
"""

from .core import MarketPlace
from .version import __version__

__all__ = [
    "MarketPlace",
    "__version__",
]
