#!/usr/bin/env python
"""Tests for `daschat_base` package."""
# pylint: disable=redefined-outer-name

import pytest

from daschat_base import __author__, __email__, __version__
from daschat_base.dc_abc_handoff import HandoffBase, WebhookTypesEnum
from daschat_base.version import VERSION

from . import current_author, current_email

# current_version = "0.11.1"
# current_author = "Daschat.io"
# current_email = "admin@daschat.io"


# def test_package_version() -> None:
#     """Test package version calculation."""
#     assert package_version() == current_version


# def test_package_version_not_found() -> None:
#     """Test package version calculation when package is not installed."""
#     assert package_version(package="incorrect") == "Package not found."


def test_version() -> None:
    """Test package version number."""
    assert __version__ == VERSION


def test_author() -> None:
    """Test package version number."""
    assert __author__ == current_author


def test_email() -> None:
    """Test package version number."""
    assert __email__ == current_email


# def test_enums() -> None:
#     """Test package enums."""
#     assert repr(WebhookTypesEnum.CHAT_SESSION) == WebhookTypesEnum.CHAT_SESSION.value
#     assert repr(WebhookTypesEnum.CHAT_FORWARDED) == 51
#     assert repr(WebhookTypesEnum.CHAT_QUEUED) < 31
#     assert WebhookTypesEnum.CHAT_QUEUED < WebhookTypesEnum.MESSAGE


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
