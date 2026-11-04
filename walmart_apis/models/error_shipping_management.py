from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ErrorShippingManagement(SdkBaseModel):
    code: str
    message: str
    details: str
    """Required diagnostic context. The create, update, and get fulfillment center operations always return this field
    as a string, whether the error originated in WSA or AFS. For AFS errors this is ``info``, falling back to
    ``description`` when ``info`` is absent."""


class ErrorShippingManagementDict(TypedDict):
    code: str
    message: str
    details: str
