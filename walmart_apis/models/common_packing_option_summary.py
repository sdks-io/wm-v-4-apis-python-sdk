from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel


class CommonPackingOptionSummary(SdkBaseModel):
    """Summary information about a packing option."""

    packing_option_id: str = Field(alias="packingOptionId")
    """Identifier of a packing option."""

    status: str
    """The status of a packing option. Possible values: ``OFFERED``, ``ACCEPTED``, ``EXPIRED``."""


class CommonPackingOptionSummaryDict(TypedDict):
    packing_option_id: str
    status: str
