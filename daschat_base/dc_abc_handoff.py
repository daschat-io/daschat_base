""" Daschat handoff metaclasses

This module must be used to create any handoff plugin to be used with the `Daschat
System`.

Todo:
    * Write docs
    * You have to also use ``sphinx.ext.todo`` extension

Some docs about how it is made:

* https://realpython.com/factory-method-python/

* https://medium.com/@geoffreykoh/implementing-the-factory-pattern-via-dynamic-registry-and-python-decorators-479fc1537bbe

"""

import json

# Standard imports
from abc import ABCMeta, abstractmethod
from enum import Enum
from typing import Any, Callable, List, Optional

# Third party imports
import cuid
from loguru import logger
from pydantic import BaseSettings

# Application imports
from .schemas import (
    ActionToTypeEnum,
    Chat,
    Config,
    Contact,
    HandsoffInfoSchema,
    MessageSchema,
)


class ChatIdTypesEnum(int, Enum):
    """Possible ways handsoff app associate chat_id with Daschat

    Args:
        int ([type]): [description]
        Enum ([type]): [description]
    """

    DASCHAT = 0
    OWN = 1


class WebhookTypesEnum(int, Enum):
    """Webhook types processed by this plugin

    Args:
        int ([type]): [description]
        Enum ([type]): [description]
    """

    UNKNOW = 0
    CHAT_START = 10
    CHAT_QUEUED = 30
    CHAT_SESSION = 40
    CHAT_TAKEN = 50
    MESSAGE = 60


# Acceptable medias
MEDIA_TYPES = {
    "audio": [
        "audio/aac",
        "audio/mp4",
        "audio/amr",
        "audio/mpeg",
        "audio/ogg; codecs=opus",
    ],
    "image": ["image/jpeg", "image/png"],
    "sticker": ["image/webp"],
    "video": ["video/mp4", "video/3gpp"],
}


class HandoffBase(metaclass=ABCMeta):
    """Base class for an handoff plugin"""

    request_id: str = cuid.cuid()
    config: Config
    data: dict = {}
    plugin: str = "generic"
    _assignment: str = "handoff"
    api_url: str
    api_path: str
    _service_api: Callable
    init_kwargs: dict
    logged: bool = False
    headers: dict = {"Content-Type": "application/json"}
    _actions: List[dict] = []
    _agent_msg_bom: str = "=========== **[BOT] Mensagem do sistema - Início**"
    _agent_msg_eom: str = "=========== **[BOT] Mensagem do sistema - Fim**"
    _webhook_type: int = WebhookTypesEnum.MESSAGE.value
    status_code: int = 200
    chat_id_type: int = ChatIdTypesEnum.DASCHAT.value
    chat_id: str
    chat_status: int = 0
    request_status: int = 0
    have_msg: bool = True
    response_type = "application/json"
    response_content: str
    output_msg: Optional[List[MessageSchema]] = []
    agent_msg: Optional[List[MessageSchema]] = []
    settings: BaseSettings
    media_bucket: str
    data_in: str
    info_data: HandsoffInfoSchema

    def __init__(self, config: Config, settings: Any, data: dict, **kwargs):
        """Initialize handsoff plugin

        Args:
            config (Config): Config of channel, hansdoff app, plugins, etc
            settings (Any): Settinhs of the Daschat installation
            data (dict): Additional data
        """
        self.config: Config = config
        self.settings: BaseSettings = settings
        self.data: dict = data
        self.init_kwargs = kwargs
        self.media_bucket = f"s3://{settings.BUCKET_FS}"

    @abstractmethod
    async def info(self, full_info=True) -> bool:
        """Get info about handsoff app

        Args:
            full_info (bool, optional): Get full info or only test connection. Defaults to True.

        Raises:
            NotImplementedError: When not implemented

        Returns:
            bool: True if can get info, False otherwise
        """

    @abstractmethod
    async def webhook(self, data_in: dict, **kwargs) -> bool:
        """
        Abstract method to process webhook calls from handoff application"""
        pass

    @abstractmethod
    async def send_msg(
        self, contact: Contact, chat: Chat, messages: List[MessageSchema], **kwargs
    ) -> bool:
        """
        Abstract method to send messages coming from contact to handoff application"""
        pass

    @abstractmethod
    async def send_operator_msg(
        self, contact: Contact, chat: Chat, messages: List[MessageSchema], **kwargs
    ) -> bool:
        """
        Abstract method to send messages coming from Daschat yourself or
        any of it plugins/bots to handoff application chat agent"""
        pass

    async def _get_webhook_type(self, type_map: dict, value: str) -> bool:
        """_get_webhook_type from data received from handoff app

        Parameters
        ----------
        type_map : dict
            Map of value to Daschat WebhookTypesEnum
        value : str
            Value received from handoff app identifying the webhook type

        Returns
        -------
        bool
            True if can associate the value with any item of WebhookTypesEnum
        """
        self._webhook_type = type_map.get(value, 0)
        if self._webhook_type == 0:
            raise NotImplementedError(f"Unknow webhook type: {value}")
        return True

    async def take_action(self, method: str, step: str = "1", **kwargs):
        """Method to take action based in some variables"""
        state: dict = {
            "plugin": self.plugin,
            "module": self.__class__.__module__,
            "class": self.__class__.__name__,
            "assignment": self._assignment,
            "method": method,
            "to_type": "owner",
            "to": "",
            "step": step,
            "config_key": self.config.key,
            "status_code": kwargs.pop("status_code", 0),
            "status": kwargs.pop("status", "STATUS-UNKNOW"),
            "errors": [],
            "kwargs": {},
        }
        if "e" in kwargs:
            state["errors"].append(str(kwargs.pop("e")))
        state["kwargs"] = kwargs
        if method.upper() == "LOGIN":
            # Probably configuration error, notify the owner
            if len(state["errors"]) == 0:
                logger.warning(json.dumps(state))
            # Probably programming error, notify DevOps
            else:
                state["to_type"] = ActionToTypeEnum.devops
                logger.error(json.dumps(state))

            # Save action
            self._actions.append(state)
        else:
            # Probably configuration error, notify the owner
            if len(state["errors"]) == 0:
                logger.warning(json.dumps(state))
            # Probably programming error, notify DevOps
            else:
                state["to_type"] = ActionToTypeEnum.devops
                logger.error(json.dumps(state))

            # Save action
            self._actions.append(state)


# end class HandoffBase
