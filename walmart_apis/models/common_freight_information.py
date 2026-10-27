from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_currency import CommonCurrency, CommonCurrencyDict


class CommonFreightInformation(SdkBaseModel):
    """Freight information describes the SKUs that are in transit."""

    declared_value: Optional[CommonCurrency] = Field(default=UNSET, alias="declaredValue")
    """The type and amount of currency."""

    freight_class: Optional[str] = Field(default=UNSET, alias="freightClass")
    """Freight class. Possible values: ``NONE``, ``FC_50``, ``FC_55``, ``FC_60``, ``FC_65``, ``FC_70``, ``FC_77_5``,
    ``FC_85``, ``FC_92_5``, ``FC_100``, ``FC_110``, ``FC_125``, ``FC_150``, ``FC_175``, ``FC_200``, ``FC_250``,
    ``FC_300``, ``FC_400``, ``FC_500``."""


class CommonFreightInformationDict(TypedDict):
    declared_value: NotRequired[CommonCurrencyDict]
    freight_class: NotRequired[str]
