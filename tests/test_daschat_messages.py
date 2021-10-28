#!/usr/bin/env python
"""Tests for `daschat_base` package."""
# pylint: disable=redefined-outer-name

import pytest

from daschat_base.messages import MSGS, result_factory
from daschat_base.schemas import DispatchCallOutSchema, ResultFieldSchema


def test_result_factory() -> None:
    """Test generation of result data."""
    data = DispatchCallOutSchema(result=result_factory(MSGS.success))
    assert type(data) == DispatchCallOutSchema
    assert type(data.result) == ResultFieldSchema
    assert data.result.status is True
    assert data.result.id == "SUCCESS"
    assert len(data.result.params) == 0

    data = DispatchCallOutSchema(
        result=result_factory(MSGS.not_logged_in, user="abner")
    )
    assert type(data) == DispatchCallOutSchema
    assert type(data.result) == ResultFieldSchema
    assert data.result.status is False
    assert data.result.id == "NOT_LOGGED_IN"
    assert len(data.result.params) == 1
    assert data.result.params["user"] == "abner"
    assert type(data.result.params["user"]) == str
    assert len(data.result.params["user"]) == 5
