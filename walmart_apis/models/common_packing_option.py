from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .common_incentive import CommonIncentive, CommonIncentiveDict
from .common_packing_configuration import CommonPackingConfiguration, CommonPackingConfigurationDict
from .common_shipping_configuration import CommonShippingConfiguration, CommonShippingConfigurationDict


class CommonPackingOption(SdkBaseModel):
    """A packing option contains a set of pack groups plus additional information such as any discounts or fees."""

    discounts: list[CommonIncentive]
    """Discount for the offered option."""

    expiration: Optional[RFC3339DateTime] = UNSET
    """The time at which this packing option is no longer valid. In ISO 8601 datetime format with pattern
    ``yyyy-MM-ddTHH:mm:ss.sssZ``."""

    fees: list[CommonIncentive]
    """Fee for the offered option."""

    packing_groups: list[str] = Field(alias="packingGroups")
    """Packing group IDs."""

    packing_option_id: str = Field(alias="packingOptionId")
    """Identifier of a packing option."""

    status: str
    """The status of the packing option. Possible values: ``OFFERED``, ``ACCEPTED``, ``EXPIRED``."""

    supported_configurations: list[CommonPackingConfiguration] = Field(alias="supportedConfigurations")
    """A list of possible configurations for this option."""

    supported_shipping_configurations: list[CommonShippingConfiguration] = Field(
        alias="supportedShippingConfigurations"
    )
    """List of supported shipping modes."""


class CommonPackingOptionDict(TypedDict):
    discounts: list[CommonIncentiveDict]
    expiration: NotRequired[RFC3339DateTime]
    fees: list[CommonIncentiveDict]
    packing_groups: list[str]
    packing_option_id: str
    status: str
    supported_configurations: list[CommonPackingConfigurationDict]
    supported_shipping_configurations: list[CommonShippingConfigurationDict]
