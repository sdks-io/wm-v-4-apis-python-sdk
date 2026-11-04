from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.prep_instruction_fulfillment_inbound_shipments import PrepInstructionFulfillmentInboundShipmentsOrStr
from .enums.prep_owner import PrepOwnerOrStr


class ShipmentItemPrepDetail(SdkBaseModel):
    """One preparation instruction for a shipment item, as returned by ``getShipmentItems`` (upstream ``PrepDetail``).
    Upstream documents ``PrepInstruction``/``PrepOwner`` on this particular schema as free strings, but the v4 contract
    aligns them to the same ``BAG``/``TAPE``/``WRAP``/``LABEL`` and ``SELLER``/``WALMART`` vocabulary formally
    enumerated elsewhere in this same upstream spec (``listInboundPlanItems``'s ``PrepInstruction`` schema) -- safe to
    enforce as a hard enum here since this is a net-new v4 response shape."""

    prep_instruction: Optional[PrepInstructionFulfillmentInboundShipmentsOrStr] = Field(
        default=UNSET, alias="prepInstruction"
    )
    """Type of preparation required. Possible values: BAG, TAPE, WRAP, LABEL."""

    prep_owner: Optional[PrepOwnerOrStr] = Field(default=UNSET, alias="prepOwner")
    """Party responsible for the prep. Possible values: SELLER, WALMART."""


class ShipmentItemPrepDetailDict(TypedDict):
    prep_instruction: NotRequired[PrepInstructionFulfillmentInboundShipmentsOrStr]
    prep_owner: NotRequired[PrepOwnerOrStr]
