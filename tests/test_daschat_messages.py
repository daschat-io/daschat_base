#!/usr/bin/env python
"""Tests for `daschat_base` package."""
# pylint: disable=redefined-outer-name

import pytest

from daschat_base.messages import MSGS, dispatch_factory, result_factory
from daschat_base.schemas import DispatchCallOutSchema, ResultFieldSchema


def test_result_factory() -> None:
    """Test generation of result data without params."""
    data = DispatchCallOutSchema(result=result_factory(MSGS.success))
    assert type(data) == DispatchCallOutSchema
    assert type(data.result) == ResultFieldSchema
    assert data.result.status is True
    assert data.result.id == "SUCCESS"
    assert len(data.result.params) == 0

    data = DispatchCallOutSchema(result=result_factory(MSGS.no_agent_online))
    assert type(data) == DispatchCallOutSchema
    assert type(data.result) == ResultFieldSchema
    assert data.result.status is False
    assert data.result.id == "NO_AGENT_ONLINE"
    assert len(data.result.params) == 0


def test_result_factory_with_params() -> None:
    """Test generation of result messages with params."""
    data = dispatch_factory(msg=MSGS.info, message="abner")
    assert type(data) == DispatchCallOutSchema
    assert type(data.result) == ResultFieldSchema
    assert data.result.status is True
    assert len(data.result.params) == 1
    assert data.result.params["message"] == "abner"
    assert type(data.result.params["message"]) == str
    assert len(data.result.params["message"]) == 5
    assert data.result.id == "INFO"

    data = dispatch_factory(msg=MSGS.unable_to_create_contact, contact="ContactId")
    assert type(data) == DispatchCallOutSchema
    assert type(data.result) == ResultFieldSchema
    assert data.result.status is False
    assert len(data.result.params) == 1
    assert data.result.params["contact"] == "ContactId"
    assert type(data.result.params["contact"]) == str
    assert len(data.result.params["contact"]) == 9
    assert data.result.id == "UNABLE_TO_CREATE_CONTACT"
