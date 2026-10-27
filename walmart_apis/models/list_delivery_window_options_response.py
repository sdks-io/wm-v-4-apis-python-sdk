from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_delivery_window_option import CommonDeliveryWindowOption, CommonDeliveryWindowOptionDict
from .common_pagination import CommonPagination, CommonPaginationDict


class ListDeliveryWindowOptionsResponse(SdkBaseModel):
    """The ``listDeliveryWindowOptions`` response."""

    delivery_window_options: list[CommonDeliveryWindowOption] = Field(alias="deliveryWindowOptions")
    """Delivery window options generated for the shipment."""

    pagination: Optional[CommonPagination] = UNSET
    """Contains tokens to fetch from a certain page."""


class ListDeliveryWindowOptionsResponseDict(TypedDict):
    delivery_window_options: list[CommonDeliveryWindowOptionDict]
    pagination: NotRequired[CommonPaginationDict]
