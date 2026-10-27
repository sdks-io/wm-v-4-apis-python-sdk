from __future__ import annotations

from dataclasses import dataclass
from typing import Final, TypeAlias

from ..core import ErrorMapper, RawError

SendTestNotificationErrorBody: TypeAlias = RawError


@dataclass(frozen=True, slots=True)
class _SendTestNotificationError:
    def map(self, status_code: int, content: bytes) -> SendTestNotificationErrorBody:
        match status_code:
            case 400 | 403 | 404 | 429 | 500:
                return RawError(status_code, content)
            case _:
                return RawError(status_code, content)


send_test_notification_error_mapper: Final[ErrorMapper[SendTestNotificationErrorBody]] = _SendTestNotificationError()
