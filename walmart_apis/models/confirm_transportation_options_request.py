from __future__ import annotations

from pydantic import Field
from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .common_transportation_selection import CommonTransportationSelection, CommonTransportationSelectionDict


class ConfirmTransportationOptionsRequest(SdkBaseModel):
    """The ``confirmTransportationOptions`` request."""

    transportation_selections: list[CommonTransportationSelection] = Field(alias="transportationSelections")
    """Information needed to confirm one of the available transportation options."""


class ConfirmTransportationOptionsRequestDict(TypedDict):
    transportation_selections: list[CommonTransportationSelectionDict]
