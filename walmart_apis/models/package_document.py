from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .enums.format_shipping import FormatShippingOrStr
from .enums.type_shipping import TypeShippingOrStr


class PackageDocument(SdkBaseModel):
    type_: TypeShippingOrStr = Field(alias="type")
    format: FormatShippingOrStr
    contents: str
    """Base64-encoded document bytes."""


class PackageDocumentDict(TypedDict):
    type_: TypeShippingOrStr
    format: FormatShippingOrStr
    contents: str
