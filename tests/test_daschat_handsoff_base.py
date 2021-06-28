#!/usr/bin/env python
"""Tests for `daschat_handsoff_base` package."""
# pylint: disable=redefined-outer-name

import pytest

from daschat_handsoff_base import __author__, __email__, __version__

current_version = "0.1.0"
current_author = "Daschat.io"
current_email = "admin@daschat.io"


# def test_package_version() -> None:
#     """Test package version calculation."""
#     assert package_version() == current_version


# def test_package_version_not_found() -> None:
#     """Test package version calculation when package is not installed."""
#     assert package_version(package="incorrect") == "Package not found."


def test_version() -> None:
    """Test package version number."""
    assert __version__ == current_version


def test_author() -> None:
    """Test package version number."""
    assert __author__ == current_author


def test_email() -> None:
    """Test package version number."""
    assert __email__ == current_email


# @pytest.fixture
# def response():
#     """Sample pytest fixture.

#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string
#     del response
