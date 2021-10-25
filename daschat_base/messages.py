""" DasChat standard messages text


"""
from copy import deepcopy

from .schemas import ResultFieldSchema

__all__ = "msg_result", "msg_dict", "msg_result_custom", "msg_dict_custom"

MSGS = {
    "DEBUG": {"text": "Debug", "params": {}},
    "INFO": {"text": "Info", "params": {}},
    "WARNING": {"text": "Warning", "params": {}},
    "ERROR": {"text": "Error", "params": {}},
    "CRITICAL": {"text": "Critical", "params": {}},
    "SUCCESS": {"text": "Success", "params": {}},
    "NO_AGENT_ONLINE": {"text": "Desculpe, nenhum agente online", "params": {}},
    "NOT_LOGGET_IN": {"text": "Não logado", "params": {}},
    "UNABLE_TO_LOGIN": {"text": "Não foi possível fazer login", "params": {}},
    "UNABLE_TO_REGISTER_CONTACT": {
        "text": "Não foi possível registrar o contato",
        "params": {},
    },
    "BAD_REQUEST": {"text": "Bad HTTP request", "params": {}},
    "FAILED": {"text": "Failed HTTP request", "params": {}},
    "CONNECTION_FAIL": {"text": "Failed HTTP connection", "params": {}},
}


def msg_result(status: bool, msg_id: str, **kwargs) -> ResultFieldSchema:
    msg = deepcopy(MSGS[msg_id])
    print(MSGS[msg_id])
    result = ResultFieldSchema(status=status, msg_id=msg_id, **msg)
    if len(kwargs) > 0:
        result.params = kwargs
    return result


def msg_result_custom(
    status: bool, msg_id: str, text: str, **kwargs
) -> ResultFieldSchema:
    result = ResultFieldSchema(status=status, msg_id=msg_id, text=text)
    if len(kwargs) > 0:
        result.params = kwargs
    return result


def msg_dict(msg_id: str, **kwargs) -> dict:
    result = deepcopy(MSGS[msg_id])
    result["msg_id"] = msg_id
    if len(kwargs) > 0:
        result["params"] = kwargs
    return result


def msg_dict_custom(msg_id: str, text: str, **kwargs) -> dict:
    result = {}
    result["msg_id"] = msg_id
    result["text"] = text
    result["params"] = {}
    if len(kwargs) > 0:
        result["params"] = kwargs
    return result
