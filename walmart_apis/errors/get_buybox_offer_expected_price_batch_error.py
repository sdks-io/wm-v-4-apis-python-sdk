from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError, decode_json
from ..models.error_catalog_items import ErrorCatalogItems

GetBuyboxOfferExpectedPriceBatchErrorBody: TypeAlias = list[ErrorCatalogItems] | RawError


@dataclass(frozen=True, slots=True)
class _GetBuyboxOfferExpectedPriceBatchError:
    def map(self, status_code: int, content: bytes) -> GetBuyboxOfferExpectedPriceBatchErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return decode_json[list[ErrorCatalogItems]](content)
            case _:
                return RawError(status_code, content)


get_buybox_offer_expected_price_batch_error_mapper: Final[
    ErrorMapper[GetBuyboxOfferExpectedPriceBatchErrorBody]
] = _GetBuyboxOfferExpectedPriceBatchError()
