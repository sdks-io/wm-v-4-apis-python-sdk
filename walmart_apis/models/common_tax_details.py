from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_currency import CommonCurrency, CommonCurrencyDict
from .common_tax_rate import CommonTaxRate, CommonTaxRateDict


class CommonTaxDetails(SdkBaseModel):
    """Information used to determine the tax compliance."""

    declared_value: Optional[CommonCurrency] = Field(default=UNSET, alias="declaredValue")
    """The type and amount of currency."""

    hsn_code: Optional[str] = Field(default=UNSET, alias="hsnCode")
    """Harmonized System of Nomenclature code."""

    tax_rates: Optional[list[CommonTaxRate]] = Field(default=UNSET, alias="taxRates")
    """List of tax rates."""


class CommonTaxDetailsDict(TypedDict):
    declared_value: NotRequired[CommonCurrencyDict]
    hsn_code: NotRequired[str]
    tax_rates: NotRequired[list[CommonTaxRateDict]]
