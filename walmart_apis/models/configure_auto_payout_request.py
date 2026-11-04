from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class ConfigureAutoPayoutRequest(SdkBaseModel):
    enabled: bool
    """true to enable automatic payouts; false to disable"""


class ConfigureAutoPayoutRequestDict(TypedDict):
    enabled: bool
