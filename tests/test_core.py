#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_core
.. moduleauthor:: Carl Simon Adorf <simon.adorf@epfl.ch>
"""
import pytest

from marketplace.core import MarketPlace


@pytest.fixture
def marketplace(environment):
    instance = MarketPlace()
    yield instance


def test_constructor(marketplace):
    pass


def test_default_headers(marketplace):
    headers = marketplace.default_headers
    assert len(headers) >= 3
    for key in ("Accept", "User-Agent", "Authorization"):
        assert key in headers
