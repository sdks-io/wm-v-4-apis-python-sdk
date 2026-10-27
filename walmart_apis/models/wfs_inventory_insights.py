from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Date, Optional, OptionalNullable, SdkBaseModel


class WfsInventoryInsights(SdkBaseModel):
    """Demand intelligence and replenishment recommendations (WFS-only — no SP-API equivalent)"""

    sales_forecast_week1to4: OptionalNullable[float] = Field(default=UNSET, alias="salesForecastWeek1to4")
    """Estimated units to sell in weeks 1–4."""

    sales_forecast_week5to8: OptionalNullable[float] = Field(default=UNSET, alias="salesForecastWeek5to8")
    """Estimated units to sell in weeks 5–8."""

    sales_forecast_week9to12: OptionalNullable[float] = Field(default=UNSET, alias="salesForecastWeek9to12")
    """Estimated units to sell in weeks 9–12."""

    sell_through_rate: OptionalNullable[float] = Field(default=UNSET, alias="sellThroughRate")
    """Units shipped ÷ average stored, last 90 days."""

    days_of_supply: Optional[str] = Field(default=UNSET, alias="daysOfSupply")
    """Estimated days until stock exhaustion at current sell rate"""

    out_of_stock_date: OptionalNullable[Date] = Field(default=UNSET, alias="outOfStockDate")
    """Projected date of stock exhaustion"""

    suggested_units: Optional[int] = Field(default=UNSET, alias="suggestedUnits")
    """Walmart-recommended reorder quantity"""

    surplus_units: OptionalNullable[int] = Field(default=UNSET, alias="surplusUnits")
    """Units exceeding 180 days of supply"""

    customer_favorite: Optional[bool] = Field(default=UNSET, alias="customerFavorite")
    """Whether this item is flagged as a customer favorite"""


class WfsInventoryInsightsDict(TypedDict):
    sales_forecast_week1to4: NotRequired[float | None]
    sales_forecast_week5to8: NotRequired[float | None]
    sales_forecast_week9to12: NotRequired[float | None]
    sell_through_rate: NotRequired[float | None]
    days_of_supply: NotRequired[str]
    out_of_stock_date: NotRequired[Date | None]
    suggested_units: NotRequired[int]
    surplus_units: NotRequired[int | None]
    customer_favorite: NotRequired[bool]
