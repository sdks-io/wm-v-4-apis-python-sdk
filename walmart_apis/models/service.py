from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class Service(SdkBaseModel):
    id: str
    name: str


class ServiceDict(TypedDict):
    id: str
    name: str
