""" DasChat standard result types


"""
from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Extra, Field
from typing_extensions import Annotated

from .schemas import DispatchCallOutSchema, ResultFieldSchema


class Param(BaseModel):
    class Config:
        allow_population_by_field_name = True
        allow_mutation = False
        extra = Extra.forbid

    name: str
    type: Any
    min_size: Optional[int] = 1
    max_size: Optional[int] = 64


class Result(BaseModel):
    class Config:
        allow_population_by_field_name = True
        allow_mutation = False
        extra = Extra.forbid

    id: str
    status: bool
    params: Optional[
        List[Annotated[Param, Field(title="Params", description="Params List")]]
    ] = []


class SystemDispatchMessages(BaseModel):
    class Config:
        allow_population_by_field_name = True
        allow_mutation = False
        extra = Extra.forbid

    # Low level messages
    info: Optional[Annotated[Result, Field(alias="INFO")]]
    warning: Optional[Annotated[Result, Field(alias="WARNING")]]
    error: Optional[Annotated[Result, Field(alias="ERROR")]]
    critical: Optional[Annotated[Result, Field(alias="CRITICAL")]]

    # Daschat messages
    success: Optional[Annotated[Result, Field(alias="SUCCESS")]]
    no_agent_online: Optional[Annotated[Result, Field(alias="NO_AGENT_ONLINE")]]
    unable_to_create_contact: Optional[
        Annotated[Result, Field(alias="UNABLE_TO_CREATE_CONTACT")]
    ]
    not_logged_in: Optional[Annotated[Result, Field(alias="NOT_LOGGED_IN")]]
    logged_in: Optional[Annotated[Result, Field(alias="LOGGED_IN")]]


MSGS = SystemDispatchMessages(
    info=Result(
        id="INFO",
        status=True,
        params=[{"name": "message", "type": str, "max_size": 1024}],
    ),
    warning=Result(
        id="WARNING",
        status=True,
        params=[{"name": "message", "type": str, "max_size": 1024}],
    ),
    error=Result(
        id="ERROR",
        status=False,
        params=[{"name": "message", "type": str, "max_size": 1024}],
    ),
    critical=Result(
        id="CRITICAL",
        status=False,
        params=[{"name": "message", "type": str, "max_size": 1024}],
    ),
    success=Result(id="SUCCESS", status=True),
    no_agent_online=Result(id="NO_AGENT_ONLINE", status=False),
    not_logged_in=Result(
        id="NOT_LOGGED_IN",
        status=False,
        params=[{"name": "user", "type": str, "min_size": 1, "max_size": 256}],
    ),
    logged_in=Result(
        id="LOGGED_IN",
        status=True,
    ),
    unable_to_create_contact=Result(
        id="UNABLE_TO_CREATE_CONTACT",
        status=False,
        params=[{"name": "contact", "type": str, "min_size": 1, "max_size": 256}],
    ),
)


def result_factory(msg: Result, **kwargs) -> ResultFieldSchema:
    """result_factory Generate result as expected by Daschat

    Examples:
        from daschat_base.messages import MSGS, msg_factory
        msg_factory(MSGS.success)
        msg_factory(MSGS.not_logged_in, user="abner")

    Args:
        msg (Result): Any result type in the MSGS contant

    Raises:
        ValueError: Parameter name not allowed
        ValueError: Result don't accept params
        ValueError: Wrong number of params
        ValueError: Wrong parameter type
        ValueError: Wrong parameter size

    Returns:
        ResultFieldSchema: [description]
    """
    call_params: int = len(kwargs)
    msg_params: int = len(msg.params)
    params: dict = {}

    if call_params > 0 and msg_params == 0:
        raise ValueError("This message do not accept params")
    if not call_params == msg_params:
        raise ValueError(
            f"Wrong number of params. This message only accepts {msg_params} parameter(s)"
        )
    if len(kwargs) > 0:
        for k in kwargs:
            param_def = next((item for item in msg.params if item.name == k), None)
            if param_def is None:
                raise ValueError(f"This parameter name is not allowed: {k}")
            if not type(kwargs[k]) == param_def.type:
                raise ValueError(
                    f"Wrong parameter type: '{k}' must be {param_def.type}"
                )
            if param_def.type == str:
                if not param_def.min_size <= len(kwargs[k]) <= param_def.max_size:
                    raise ValueError(
                        f"Wrong parameter size: '{k}' must be between {param_def.min_size} and {param_def.max_size}"
                    )
            params[k] = kwargs[k]

    return ResultFieldSchema(id=msg.id, status=msg.status, params=params)


def dispatch_factory(msg: Result, **kwargs) -> DispatchCallOutSchema:
    """result_factory Generate result as expected by Daschat

    Examples:
        from daschat_base.messages import MSGS, msg_factory
        msg_factory(MSGS.success)
        msg_factory(MSGS.not_logged_in, user="abner")

    Args:
        msg (Result): Any result type in the MSGS contant

    Raises:
        ValueError: Parameter name not allowed
        ValueError: Result don't accept params
        ValueError: Wrong number of params
        ValueError: Wrong parameter type
        ValueError: Wrong parameter size

    Returns:
        ResultFieldSchema: [description]
    """
    call_params: int = len(kwargs)
    msg_params: int = len(msg.params)
    params: dict = {}

    if call_params > 0 and msg_params == 0:
        raise ValueError("This message do not accept params")
    if not call_params == msg_params:
        raise ValueError(
            f"Wrong number of params. This message only accepts {msg_params} parameter(s)"
        )
    if len(kwargs) > 0:
        for k in kwargs:
            param_def = next((item for item in msg.params if item.name == k), None)
            if param_def is None:
                raise ValueError(f"This parameter name is not allowed: {k}")
            if not type(kwargs[k]) == param_def.type:
                raise ValueError(
                    f"Wrong parameter type: '{k}' must be {param_def.type}"
                )
            if param_def.type == str:
                if not param_def.min_size <= len(kwargs[k]) <= param_def.max_size:
                    raise ValueError(
                        f"Wrong parameter size: '{k}' must be between {param_def.min_size} and {param_def.max_size}"
                    )
            params[k] = kwargs[k]

    return DispatchCallOutSchema(
        result=ResultFieldSchema(id=msg.id, status=msg.status, params=params)
    )
