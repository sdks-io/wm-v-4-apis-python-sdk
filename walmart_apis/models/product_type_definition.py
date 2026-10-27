from __future__ import annotations

from typing import Any

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class ProductTypeDefinition(SdkBaseModel):
    meta_schema: Optional[str] = Field(default=UNSET, alias="metaSchema")
    schema_value: Optional[Any] = Field(default=UNSET, alias="schema")
    """JSON Schema for this product type's attributes"""

    requirements: Optional[Any] = UNSET
    property_groups: Optional[Any] = Field(default=UNSET, alias="propertyGroups")


class ProductTypeDefinitionDict(TypedDict):
    meta_schema: NotRequired[str]
    schema_value: NotRequired[Any]
    requirements: NotRequired[Any]
    property_groups: NotRequired[Any]
