from __future__ import annotations

from typing import Any

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class GetAdditionalInputsResponse(SdkBaseModel):
    payload: Optional[Any] = UNSET
    """JSON Schema (draft-07 compatible) describing the additional inputs required for the given rateId. Served verbatim
    from the upstream carrier integration."""


class GetAdditionalInputsResponseDict(TypedDict):
    payload: NotRequired[Any]
