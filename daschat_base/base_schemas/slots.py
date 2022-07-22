import time
from datetime import datetime
from enum import Enum
from typing import Any, Dict, Literal, Optional

from pydantic import AnyUrl, BaseModel, Field, stricturl, validator


class SlotDataSchema(BaseModel):
    class Config:
        validate_assignment = True

    value_type: Literal["text", "bool", "float", "list", "dict", "categorical", "int"] = Field(
        ...,
        title="Slot Type",
        description="Slot value type.",
        example="text",
    )
    timestamp: int = Field(
        int(time.time() * 1000),
        title="Timestamp",
        description="Timestamp when value was set.",
        example="1640378764507",
    )
    name: str = Field(
        ...,
        max_length=256,
        title="Slot Name",
        description="Slot unique name.",
        example="department",
    )
    value: Any = Field(
        ...,
        title="Slot value",
        description="Slot value in the slot value_type format.",
        example="General",
    )
