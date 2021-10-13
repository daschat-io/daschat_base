"""Daschat base schemas."""

from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import AnyHttpUrl, BaseModel, Field, stricturl


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


# class DasFileUrl(AnyHttpUrl):
#     allowed_schemes = ["https", "http"]
#     tld_required = False


class Config(BaseModel):
    class Config:
        validate_assignment = True

    label: str = Field(
        ...,
        max_length=255,
        title="Label",
        description="This config label.",
        example="Some config label",
    )
    key: str = Field(
        ...,
        max_length=50,
        title="Config key",
        description="Config unique key.",
        example="unique-configkey-ckasnzjot0001p2xutk68nys8",
    )
    value: Dict[str, Any] = Field(
        ..., title="Config value", description="Config value in json format."
    )
    status: int = Field(
        1, title="Config status", description="Config status.", example="1", gt=-1, lt=2
    )
    id: str = Field(
        ...,
        max_length=25,
        title="SID",
        description="The ID of the config.",
        example="ckasokq6g0000yvxuigfa2agy",
    )
    owner_id: str = Field(
        ...,
        max_length=25,
        title="Owner ID",
        description="The ID of the owner of this config.",
        example="ckasolg5o0001yvxuzdty0jrd",
    )


class StateItemSchema(BaseModel):
    class Config:
        validate_assignment = True

    id: str = Field(
        ...,
        max_length=25,
        title="State ID",
        description="State ID value.",
        example="optin",
    )

    data: Dict[str, Any] = Field(
        {}, title="State Data", description="State saved data."
    )
    order: int = Field(
        0,
        title="Order",
        description="Order in wich the plugin was executed.",
        example=0,
        gt=-1,
        lt=100,
    )
    state: str = Field(
        "init",
        max_length=25,
        title="State",
        description="Current state value.",
        example="init",
    )


class StatesSchema(BaseModel):
    class Config:
        validate_assignment = True

    channel_in: Optional[List[StateItemSchema]] = []


class HandsoffDataSchema(BaseModel):
    class Config:
        validate_assignment = True

    namespace: str = Field(
        ...,
        max_length=255,
        title="Namespace",
        description="Which plugin this data belongs to.",
        example="rocketchat",
    )
    key: str = Field(
        ...,
        max_length=50,
        title="Data key",
        description="Data unique key.",
        example="chat",
    )
    value: Dict[str, Any] = Field(
        ..., title="Data value", description="Data value in json format."
    )


class Chat(BaseModel):
    class Config:
        validate_assignment = True

    id: str = Field(
        ...,
        max_length=25,
        title="SID",
        description="The ID of this chat.",
        example="ckasokq6g0000yvxuigfa2000",
    )
    owner_id: str = Field(
        ...,
        max_length=25,
        title="Owner ID",
        description="The ID of the owner of this chat.",
        example="ckasolg5o0001yvxuzdty0222",
    )
    contact_id: str = Field(
        ...,
        max_length=25,
        title="Contact ID",
        description="The contact ID this chat call.",
        example="ckasolg5o0001yvxuzdty0111",
    )
    created_at: datetime
    channel: str = Field(
        ...,
        max_length=25,
        title="Channel",
        description="Channel used by this chat.",
        example="whatsapp",
    )
    channel_plugin: str = Field(
        ...,
        max_length=25,
        title="Channel Plugin",
        description="Channel plugin used by this chat.",
        example="twwhatsapp",
    )
    channel_uid: str = Field(
        ...,
        max_length=255,
        title="Channel UID",
        description="Contact from UID.",
        example="5527999000000",
    )
    channel_contact_uid: str = Field(
        ...,
        max_length=255,
        title="Channel Contact UID",
        description="Channel contact UID.",
        example="5527999000011",
    )
    channel_config: str = Field(
        ...,
        max_length=50,
        title="Channel Config",
        description="Channel config key.",
        example="twwhatsapp-ckasnzjot0001p2xutk68n000",
    )
    handson: str = Field(
        ...,
        max_length=25,
        title="Handson",
        description="Channel handson PLUGIN.",
        example="tiledesk",
    )
    handson_config: str = Field(
        ...,
        max_length=50,
        title="Handson Config Key",
        description="Channel handson config key.",
        example="tiledesk-ckbl7w4nq0000zuxuiibic000",
    )
    subject: Dict[str, Any] = Field(..., title="Subject", description="Chat subject.")
    status: int = Field(
        ..., title="Status", description="Chat status.", example="1", gt=-1, lt=1025
    )
    # state: Dict[str, Any] = Field({}, title="State", description="Chat state machine.")
    state: Optional[StatesSchema]
    handsoff_cid: Optional[str] = Field(
        None,
        max_length=128,
        title="Handsoff chat ID",
        description="Handsoff app own chat ID",
        example="BxdYnAjpu3PTciw6Z",
    )
    handsoff_data: Optional[List[HandsoffDataSchema]] = Field(
        [],
        title="Handsoff app data",
        description="handsoff data received from the plugin and that need to be stored.",
    )


class Contact(BaseModel):
    class Config:
        validate_assignment = True

    id: str = Field(
        ...,
        max_length=25,
        title="SID",
        description="The ID of the Contact call.",
        example="ckasokq6g0000yvxuigfa2agy",
    )
    owner_id: str = Field(
        ...,
        max_length=25,
        title="Owner ID",
        description="The ID of the owner of this Contact call.",
        example="ckasolg5o0001yvxuzdty0jrd",
    )
    created_at: datetime
    full_name: str = Field(
        ...,
        max_length=255,
        title="Full Name",
        description="Contact full name.",
        example="John Doe",
    )
    email: str = Field(
        ...,
        max_length=255,
        title="Email",
        description="Contact email.",
        example="johndoe@domain.com",
    )
    channel: str = Field(
        ...,
        max_length=25,
        title="Channel",
        description="Channel used by this contact.",
        example="whatsapp",
    )
    channel_id: str = Field(
        ...,
        max_length=255,
        title="Channel ID",
        description="Contact channel ID.",
        example="5527999000000",
    )
    profile: Dict[str, Any] = Field(
        ..., title="Profile", description="Contact profile."
    )
    status: int = Field(
        ..., title="Status", description="Contact status.", example="1", gt=-1, lt=1025
    )


class CustomFields(BaseModel):
    class Config:
        validate_assignment = True

    key: str = Field(
        ...,
        max_length=32,
        title="Key",
        description="Unique key.",
        example="channel",
    )
    value: str = Field(
        ...,
        max_length=128,
        title="Value",
        description="Value of the key.",
        example="whatsapp",
    )
    overwrite: bool = Field(
        ...,
        title="Overwrite",
        description="Overwrite existent value.",
    )


class MediaMetaData(BaseModel):
    class Config:
        validate_assignment = True

    name: str = Field(
        ...,
        max_length=128,
        title="File Name",
        description="Original media file name.",
        example="filename.png",
    )
    path: Path = Field(
        ...,
        title="Media Path",
        description="The valid absolute path of the media in the storage system",
        example="/media/filename.png",
    )
    src: AnyHttpUrl = Field(
        ...,
        title="Media URL",
        description="The valid absolute URL of the media. Needs to be HTTPS",
        example="https://mydomain.com/media/filename.png",
    )
    type: str = Field(
        ...,
        max_length=128,
        title="Type",
        description="Media type.",
        example="image/png",
    )
    height: Optional[int] = Field(
        0, title="Height", description="Height for image media.", example=460
    )
    width: Optional[int] = Field(
        0, title="Width", description="Width for image media.", example=817
    )
    uid: Optional[str] = Field(
        "",
        max_length=64,
        title="Media UID",
        description="Media optional UID.",
        example="AAAAAElFTkSuQmCC",
    )


class MessageSchema(BaseModel):
    class Config:
        validate_assignment = True

    message_type: MessageTypeEnum = Field(
        MessageTypeEnum.text, title="Type", description="Message type.", example="text"
    )
    content: str = Field(
        ...,
        max_length=2048,
        title="Content",
        description="Message content.",
        example="This is a message content.",
    )
    metadata: Optional[MediaMetaData]


class HandsoffInfoDataSchema(BaseModel):
    class Config:
        validate_assignment = True

    version: str = Field(
        ...,
        max_length=64,
        title="Version",
        description="Handsoff app version.",
        example="v4.0.1",
    )
    departments: Optional[List[Dict[str, Any]]] = Field(
        [],
        title="Departments",
        description="Handsoff departments.",
    )
    agents: Optional[List[Dict[str, Any]]] = Field(
        [],
        title="Agents",
        description="Handsoff agents.",
    )
    business_hours: Optional[List[Dict[str, Any]]] = Field(
        [],
        title="Business Hours",
        description="Business hours of human attendants",
    )


class HandsoffInfoSchema(BaseModel):
    class Config:
        validate_assignment = True

    success: bool = Field(
        ...,
        title="Success",
        description="Handsoff app is online.",
    )
    status_code: int = Field(
        200,
        title="Status Code",
        description="Request status code.",
        example="200",
        gt=99,
        lt=600,
    )
    data: HandsoffInfoDataSchema = Field(
        ..., title="Data", description="Handsoff app data."
    )
