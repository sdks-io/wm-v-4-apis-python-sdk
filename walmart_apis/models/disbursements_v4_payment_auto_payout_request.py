from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class DisbursementsV4PaymentAutoPayoutRequest(SdkBaseModel):
    enabled: bool
    """true to enable automatic payouts; false to disable"""


class DisbursementsV4PaymentAutoPayoutRequestDict(TypedDict):
    enabled: bool
