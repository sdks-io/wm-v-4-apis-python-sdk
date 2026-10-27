from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class UpdateInboundPlanNameRequest(SdkBaseModel):
    """The ``updateInboundPlanName`` request."""

    name: str
    """A human-readable name to update the inbound plan name to."""


class UpdateInboundPlanNameRequestDict(TypedDict):
    name: str
