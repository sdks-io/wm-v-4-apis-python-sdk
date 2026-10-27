from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

DeleteSubscriptionByIdErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _DeleteSubscriptionByIdError:
    def map(self, status_code: int, content: bytes) -> DeleteSubscriptionByIdErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


delete_subscription_by_id_error_mapper: Final[
    ErrorMapper[DeleteSubscriptionByIdErrorBody]
] = _DeleteSubscriptionByIdError()
