#!/usr/bin/env python
"""Tests for `daschat_base` package."""
# pylint: disable=redefined-outer-name

import pytest

from daschat_base.messages import msg_dict, msg_result
from daschat_base.schemas import DispatchCallOutSchema, ResultFieldSchema


def test_msg_result() -> None:
    """Test generation of result data."""
    data = DispatchCallOutSchema(result=msg_result(True, "NO_AGENT_ONLINE"))
    assert type(data.result) == ResultFieldSchema
    assert data.result.msg_id == "NO_AGENT_ONLINE"
    assert len(data.result.params) == 0
    data = DispatchCallOutSchema(
        result=msg_result(True, "DEBUG"),
        param1="value1",
        param2={"field1": "field1_value"},
    )
    assert type(data.result) == ResultFieldSchema
    assert data.result.msg_id == "DEBUG"
    assert len(data.result.params) == 2
    assert data.result.params["param1"] == "value1"
    assert type(data.result.params["param2"]) == dict
    assert len(data.result.params["param2"]) == 1
    assert data.result.params["param2"]["field1"] == "field1_value"
