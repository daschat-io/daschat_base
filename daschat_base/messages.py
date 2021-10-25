""" DasChat standard messages text


"""
from copy import deepcopy

from .schemas import ResultFieldSchema

__all__ = "msg_result", "msg_dict"

MSGS = {
    "DEBUG": {"text": "Debug", "params": {}},
    "INFO": {"text": "Info", "params": {}},
    "WARNING": {"text": "Warning", "params": {}},
    "ERROR": {"text": "Error", "params": {}},
    "CRITICAL": {"text": "Critical", "params": {}},
    "SUCCESS": {"text": "Success", "params": {}},
    "NO_AGENT_ONLINE": {"text": "Sorry, no online agents", "params": {}},
}


def msg_result(status: bool, msg_id: str, **kwargs) -> ResultFieldSchema:
    msg = deepcopy(MSGS[msg_id])
    print(MSGS[msg_id])
    result = ResultFieldSchema(status=status, msg_id=msg_id, **msg)
    if len(kwargs) > 0:
        result.params = kwargs
    return result


def msg_dict(msg_id: str, **kwargs) -> dict:
    result = deepcopy(MSGS[msg_id])
    result["msg_id"] = msg_id
    if len(kwargs) > 0:
        result["params"] = kwargs
    return result
