#!/usr/bin/env python
"""Tests for `daschat_base` package."""
# pylint: disable=redefined-outer-name

import pytest

from daschat_base.messages import MSGS, dispatch_factory, result_factory
from daschat_base.schemas import DispatchCallOutSchema, ResultFieldSchema


def test_result_factory() -> None:
    """Test generation of result data."""
    data = DispatchCallOutSchema(result=result_factory(MSGS.success))
    assert type(data) == DispatchCallOutSchema
    assert type(data.result) == ResultFieldSchema
    assert data.result.status is True
    assert data.result.id == "SUCCESS"
    assert len(data.result.params) == 0


def test_result_factory_with_params() -> None:
    data = dispatch_factory(msg=MSGS.logged_in, user="abner")
    assert type(data) == DispatchCallOutSchema
    assert type(data.result) == ResultFieldSchema
    assert data.result.status is True
    assert len(data.result.params) == 1
    assert data.result.params["user"] == "abner"
    assert type(data.result.params["user"]) == str
    assert len(data.result.params["user"]) == 5
    assert data.result.id == "LOGGED_IN"

    data = dispatch_factory(msg=MSGS.not_logged_in, user="abner")
    assert type(data) == DispatchCallOutSchema
    assert type(data.result) == ResultFieldSchema
    assert data.result.status is False
    assert len(data.result.params) == 1
    assert data.result.params["user"] == "abner"
    assert type(data.result.params["user"]) == str
    assert len(data.result.params["user"]) == 5
    assert data.result.id == "NOT_LOGGED_IN"
