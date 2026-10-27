from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_msku_quantity import CommonMskuQuantity, CommonMskuQuantityDict
from .enums.common_item_label_page_type import CommonItemLabelPageTypeOrStr
from .enums.common_label_print_type import CommonLabelPrintTypeOrStr


class CreateMarketplaceItemLabelsRequest(SdkBaseModel):
    """The ``createMarketplaceItemLabels`` request."""

    height: Optional[float] = UNSET
    """The height of the item label."""

    label_type: CommonLabelPrintTypeOrStr = Field(alias="labelType")
    """Indicates the type of print type for a given label."""

    locale_code: str = Field(default="en_US", alias="localeCode")
    """The locale code constructed from ISO 639 language code and ISO 3166-1 alpha-2 country codes separated by an
    underscore character."""

    marketplace_id: str = Field(alias="marketplaceId")
    """The Walmart Marketplace ID. For a list of possible values, refer to `Marketplace IDs
    <https://developer-docs.walmart.com/seller-api/docs/marketplace-ids>`__."""

    msku_quantities: list[CommonMskuQuantity] = Field(alias="mskuQuantities")
    """Represents the quantity of an MSKU to print item labels for."""

    page_type: Optional[CommonItemLabelPageTypeOrStr] = Field(default=UNSET, alias="pageType")
    """The page type to use to print the labels."""

    width: Optional[float] = UNSET
    """The width of the item label."""


class CreateMarketplaceItemLabelsRequestDict(TypedDict):
    height: NotRequired[float]
    label_type: CommonLabelPrintTypeOrStr
    locale_code: NotRequired[str]
    marketplace_id: str
    msku_quantities: list[CommonMskuQuantityDict]
    page_type: NotRequired[CommonItemLabelPageTypeOrStr]
    width: NotRequired[float]
