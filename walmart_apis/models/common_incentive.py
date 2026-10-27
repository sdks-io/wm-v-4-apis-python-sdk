from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_currency import CommonCurrency, CommonCurrencyDict


class CommonIncentive(SdkBaseModel):
    """Contains details about cost related modifications to the placement cost."""

    description: str
    """Description of the incentive."""

    target: str
    """Target of the incentive. Possible values: 'Placement Services', 'Fulfillment Fee Discount'."""

    type_: str = Field(alias="type")
    """Type of incentive. Possible values: ``FEE``, ``DISCOUNT``."""

    value: CommonCurrency
    """The type and amount of currency."""


class CommonIncentiveDict(TypedDict):
    description: str
    target: str
    type_: str
    value: CommonCurrencyDict
