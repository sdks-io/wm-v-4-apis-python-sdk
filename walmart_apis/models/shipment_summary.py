from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .common_address import CommonAddress, CommonAddressDict
from .enums.label_prep_type import LabelPrepTypeOrStr
from .enums.shipment_box_contents_source import ShipmentBoxContentsSourceOrStr
from .enums.shipment_status import ShipmentStatusOrStr


class ShipmentSummary(SdkBaseModel):
    """Summary details for a single shipment, as returned by ``getShipments`` (aligned with the Inbound Order Workflow
    upstream ``ShipmentData`` shape). A deliberately smaller/flatter shape than the full ``Shipment`` returned by
    ``getShipment`` -- upstream's list-search endpoint returns only these fields, not the full shipment detail."""

    shipment_id: str = Field(alias="shipmentId")
    """Identifier of the shipment (external reference id) (upstream ShipmentId)."""

    ship_from_address: Optional[CommonAddress] = Field(default=UNSET, alias="shipFromAddress")
    """Specific details to identify a place."""

    destination_fulfillment_center_id: Optional[str] = Field(default=UNSET, alias="destinationFulfillmentCenterId")
    """The Ship Node identifier for the destination fulfillment center (upstream DestinationFulfillmentCenterId)."""

    status: Optional[ShipmentStatusOrStr] = UNSET
    """The status of a shipment, as returned by ``getShipments`` (upstream ``ShipmentStatusList`` /
    ``ShipmentData.ShipmentStatus``). A hard enum here is safe -- this is a net-new v4 response shape with no
    pre-existing consumers, unlike the free-string ``Shipment.status`` field on the ``getShipment`` sibling op (which
    carries the same vocabulary PLUS ``UNCONFIRMED``, kept as a free string there for that op's own historical
    reasons)."""

    label_prep_type: Optional[LabelPrepTypeOrStr] = Field(default=UNSET, alias="labelPrepType")
    """Labeling requirement for the shipment (upstream ``LabelPrepType``). NOTE : upstream renamed the first value from
    ``NO_LABEL`` to ``SELLER_LABEL`` -- same meaning (seller supplies their own label), clearer name."""

    are_cases_required: Optional[bool] = Field(default=UNSET, alias="areCasesRequired")
    """Whether cases are required for this shipment (upstream AreCasesRequired)."""

    confirmed_need_by_date: Optional[str] = Field(default=UNSET, alias="confirmedNeedByDate")
    """The confirmed need-by / estimated delivery date for the shipment, ISO 8601 datetime (upstream
    ConfirmedNeedByDate)."""

    box_contents_source: Optional[ShipmentBoxContentsSourceOrStr] = Field(default=UNSET, alias="boxContentsSource")
    """How box contents were declared for this shipment (upstream ``BoxContentsSource``). NOTE: distinct vocabulary from
    the shared ``BoxContentInformationSource`` enum used on ``Box`` -- that schema models a DIFFERENT upstream concept
    (box-level packing-plan input) with its own ``BOX_CONTENT_PROVIDED``/``MANUAL_PROCESS``/``BARCODE_2D`` values; do
    not conflate the two."""


class ShipmentSummaryDict(TypedDict):
    shipment_id: str
    ship_from_address: NotRequired[CommonAddressDict]
    destination_fulfillment_center_id: NotRequired[str]
    status: NotRequired[ShipmentStatusOrStr]
    label_prep_type: NotRequired[LabelPrepTypeOrStr]
    are_cases_required: NotRequired[bool]
    confirmed_need_by_date: NotRequired[str]
    box_contents_source: NotRequired[ShipmentBoxContentsSourceOrStr]
