from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.format1 import Format1OrStr
from .enums.type1 import Type1OrStr


class PackageDocument(SdkBaseModel):
    type_: Type1OrStr = Field(alias="type")
    format: Format1OrStr
    contents: str
    """Base64-encoded document bytes."""


class PackageDocumentDict(TypedDict):
    type_: Type1OrStr
    format: Format1OrStr
    contents: str
