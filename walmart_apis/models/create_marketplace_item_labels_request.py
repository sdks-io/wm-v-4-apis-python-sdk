from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_msku_quantity import CommonMskuQuantity, CommonMskuQuantityDict
from .enums.common_item_label_page_type import CommonItemLabelPageTypeOrStr
from .enums.common_label_print_type import CommonLabelPrintTypeOrStr
from .enums.locale_code import LocaleCode, LocaleCodeOrStr


class CreateMarketplaceItemLabelsRequest(SdkBaseModel):
    """The ``createMarketplaceItemLabels`` request."""

    height: Optional[float] = UNSET
    """The height of the item label, in millimeters. Optional — Walmart uses pre-configured label templates, so a custom
    height is accepted for cross-marketplace spec parity but ignored during label generation."""

    label_type: CommonLabelPrintTypeOrStr = Field(alias="labelType")
    """Indicates the type of print type for a given label."""

    locale_code: LocaleCodeOrStr = Field(default=LocaleCode.EN_US, alias="localeCode")
    """The locale code constructed from an ISO 639 language code and an ISO 3166-1 alpha-2 country code separated by an
    underscore. Optional; defaults to ``en_US``."""

    marketplace_id: str = Field(alias="marketplaceId")
    """The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
    <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__."""

    msku_quantities: list[CommonMskuQuantity] = Field(alias="mskuQuantities")
    """Represents the quantity of an MSKU to print item labels for."""

    page_type: Optional[CommonItemLabelPageTypeOrStr] = Field(default=UNSET, alias="pageType")
    """The page type to use to print the labels."""

    width: Optional[float] = UNSET
    """The width of the item label, in millimeters. Optional — Walmart uses pre-configured label templates, so a custom
    width is accepted for cross-marketplace spec parity but ignored during label generation."""


class CreateMarketplaceItemLabelsRequestDict(TypedDict):
    height: NotRequired[float]
    label_type: CommonLabelPrintTypeOrStr
    locale_code: NotRequired[LocaleCodeOrStr]
    marketplace_id: str
    msku_quantities: list[CommonMskuQuantityDict]
    page_type: NotRequired[CommonItemLabelPageTypeOrStr]
    width: NotRequired[float]
