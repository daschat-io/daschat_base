""" DasChat type definitions

https://stackoverflow.com/questions/24487405/enum-getting-value-of-enum-on-string-conversion
"""
from enum import Enum
from typing import Any, Dict, List, Optional


class MessageTypeEnum(str, Enum):
    text = "text"
    image = "image"
    audio = "audio"
    video = "video"
    file = "file"
    location = "location"
    contact = "contact"
    template = "template"
    sticker = "sticker"

    # def __repr__(self):
    #     return self.value


class MessageDispatchEnum(str, Enum):
    """MessageDispatchEnum

    Types that define which module of the DasChat ecosystem will process the message.

    See:

    https://medium.com/ingeniouslysimple/static-and-dynamic-dispatch-324d3dc890a3
    """

    gateway = "gateway"
    # action = "action"
    # flow = "flow"
    # storage = "storage"
    # contact = "contact"
    # bot = "bot"
    # plugin = "plugin"
    # webhook = "webhook"
    # system = "system"

    # def __repr__(self):
    #     return self.value


class ActionToTypeEnum(str, Enum):
    """ActionToTypeEnum

    Actions types.
    """

    contact = "contact"
    owner = "owner"
    bot = "bot"
    plugin = "plugin"
    devops = "devops"
    webhook = "webhook"
    system = "system"

    # def __repr__(self):
    #     return self.value
