from src.enums import (
    TierRateCardId,
    LineItemType,
)
from src.constants import LINE_ITEM_TYPE_NAME
from src.model import LineItemResponse, RateCard


class BaseTier:
    """
    Base class for calculating tier-based earnings.

    Attributes:
        name (TierRateCardId): Identifier for the tier.
        rate_card (RateCard): RateCard object containing pricing information.
        line_items (list[LineItemResponse]): Calculated earnings and deductions.
        hours_worked (float): Total hours worked across all routes.
        minimum_earnings (float): Guaranteed minimum earnings based on tier and hours worked.
    """

    def __init__(self, name: TierRateCardId, rate_card: RateCard) -> None:
        """
        Initializes a new BaseTier instance.

        Parameters:
            name (TierRateCardId): The tier's identifier.
            rate_card (RateCard): A RateCard object with pricing details.
        """
        self.name = name
        self.rate_card = rate_card
        self.line_items = []
        self.hours_worked = 0.0
        self.minimum_earnings = 0.0

    @property
    def line_items_subtotal(self) -> float:
        """Calculates the subtotal of all earnings from line items."""
        return sum([line_item.total for line_item in self.line_items])

    @property
    def final_earnings(self) -> float:
        """Calculates final earnings, considering the higher of line items subtotal or minimum earnings."""
        return (
            self.line_items_subtotal
            if self.line_items_subtotal > self.minimum_earnings
            else self.minimum_earnings
        )

    def calculate_earnings(self, activity_logs_df) -> None:
        """
        Orchestrates the calculation of total earnings based on activity logs.

        Parameters:
            activity_logs_df (DataFrame): Data frame containing activity log entries.
        """
        self.calculate_successful_attempt(activity_logs_df)
        self.calculate_unsuccessful_attempt(activity_logs_df)
        self.calculate_hourly_minimum_earnings(activity_logs_df)

    def calculate_successful_attempt(self, activity_logs_df) -> None:
        """
        Calculates earnings from successful attempts.

        Parameters:
            activity_logs_df (DataFrame): Data frame containing activity log entries.
        """
        count_df = activity_logs_df[activity_logs_df["success"] == True][
            "success"
        ].value_counts()
        quantity = float(count_df.iloc[0] if len(count_df) > 0 else 0)
        rate = self.rate_card.line_items[LineItemType.PerSuccessfulAttempt].rate
        self.line_items.append(
            LineItemResponse(
                name=LINE_ITEM_TYPE_NAME[LineItemType.PerSuccessfulAttempt],
                quantity=quantity,
                rate=rate,
                total=quantity * rate,
            )
        )

    def calculate_unsuccessful_attempt(self, activity_logs_df) -> None:
        """
        Calculates deductions or zero-earnings from unsuccessful attempts.

        Parameters:
            activity_logs_df (DataFrame): Data frame containing activity log entries.
        """
        count_df = activity_logs_df[activity_logs_df["success"] == False][
            "success"
        ].value_counts()
        quantity = float(count_df.iloc[0] if len(count_df) > 0 else 0)
        rate = self.rate_card.line_items[LineItemType.PerUnsuccessfulAttempt].rate
        self.line_items.append(
            LineItemResponse(
                name=LINE_ITEM_TYPE_NAME[LineItemType.PerUnsuccessfulAttempt],
                quantity=quantity,
                rate=rate,
                total=quantity * rate,
            )
        )

    def calculate_hourly_minimum_earnings(self, activity_logs_df) -> None:
        """
        Ensures earnings meet a minimum hourly rate.

        Parameters:
            activity_logs_df (DataFrame): Data frame containing activity log entries.
        """
        activity_logs_df_grouped_by_route = activity_logs_df.groupby("route_id")
        route_durations = activity_logs_df_grouped_by_route["attempt_date_time"].apply(
            lambda x: (x.max() - x.min()).total_seconds() / 3600
        )
        self.hours_worked = sum(route_durations) if len(route_durations) else 0.0
        self.minimum_earnings = (
            self.hours_worked * self.rate_card.hourly_minimum_earnings
        )

    def calculate_long_route_bonus(self, activity_logs_df) -> None:
        """
        Calculates and applies a long route bonus based on the number of successful attempts per route.

        A long route bonus is applied if a route has more than 30 successful attempts.

        Parameters:
            activity_logs_df (DataFrame): A DataFrame containing activity logs, including route IDs and success flags.
        """
        activity_logs_df_grouped_by_route = activity_logs_df.groupby("route_id")
        route_successful_drops = route_successful_drops = (
            activity_logs_df_grouped_by_route["success"].size()
        )
        routes_over_30_successful_drops = route_successful_drops[
            route_successful_drops > 30
        ]

        rate = self.rate_card.line_items[LineItemType.LongRouteBonus].rate
        quantity = 1 if len(routes_over_30_successful_drops) else 0
        self.line_items.append(
            LineItemResponse(
                name=LINE_ITEM_TYPE_NAME[LineItemType.LongRouteBonus],
                quantity=quantity,
                rate=rate,
                total=rate * quantity,
            )
        )

    def calculate_loyalty_bonus_route(self, activity_logs_df) -> None:
        """
        Calculates and applies a loyalty bonus based on the number of unique routes completed.

        A loyalty bonus for routes is applied if more than 10 unique routes have been completed.

        Parameters:
            activity_logs_df (DataFrame): A DataFrame containing activity logs, including route IDs.
        """
        unique_route_count = activity_logs_df["route_id"].nunique()
        quantity = 1 if unique_route_count > 10 else 0
        rate = self.rate_card.line_items[LineItemType.LoyaltyBonusRoutes].rate
        self.line_items.append(
            LineItemResponse(
                name=LINE_ITEM_TYPE_NAME[LineItemType.LoyaltyBonusRoutes],
                quantity=quantity,
                rate=rate,
                total=rate * quantity,
            )
        )

    def calculate_loyalty_bonus_attempt(self, activity_logs_df) -> None:
        """
        Calculates and applies a loyalty bonus based on the total number of successful attempts.

        A loyalty bonus for attempts is applied if there are 150 or more successful attempts.

        Parameters:
            activity_logs_df (DataFrame): A DataFrame containing activity logs, including success flags.
        """
        successful_attempts = activity_logs_df[activity_logs_df["success"]].shape[0]
        quantity = 1 if successful_attempts >= 150 else 0
        rate = self.rate_card.line_items[LineItemType.LoyaltyBonusAttempts].rate
        self.line_items.append(
            LineItemResponse(
                name=LINE_ITEM_TYPE_NAME[LineItemType.LoyaltyBonusAttempts],
                quantity=quantity,
                rate=rate,
                total=rate * quantity,
            )
        )

    def calculate_quality_bonus_attempt(self, activity_logs_df) -> None:
        """
        Calculates and applies a quality bonus based on the success rate of attempts.

        A quality bonus is applied if there are at least 20 attempts with a success rate of 97% or higher.

        Parameters:
            activity_logs_df (DataFrame): A DataFrame containing activity logs, including success flags.
        """
        total_attempts = activity_logs_df.shape[0]
        successful_attempts = activity_logs_df[activity_logs_df["success"]].shape[0]
        success_rate = successful_attempts / total_attempts * 100
        quantity = 1 if total_attempts >= 20 and success_rate >= 97.0 else 0
        rate = self.rate_card.line_items[LineItemType.QualityBonus].rate
        self.line_items.append(
            LineItemResponse(
                name=LINE_ITEM_TYPE_NAME[LineItemType.QualityBonus],
                quantity=quantity,
                rate=rate,
                total=rate * quantity,
            )
        )

    def calculate_consistency_bonus(self, activity_logs_df) -> None:
        """
        Calculates and applies a consistency bonus based on the overall success rate across all routes
        and the number of unique routes completed.

        A consistency bonus is applied if the delivery person has completed deliveries on at least two
        unique routes with an overall success rate of 96.5% or higher.

        Parameters:
            activity_logs_df (DataFrame): A DataFrame containing activity logs, including 'success' flags
                                          and 'route_id' to identify unique routes.

        """
        success_rate = activity_logs_df["success"].mean() * 100
        num_routes = activity_logs_df["route_id"].nunique()
        quantity = 1 if num_routes >= 2 and success_rate >= 96.5 else 0
        rate = self.rate_card.line_items[LineItemType.ConsistencyBonus].rate
        self.line_items.append(
            LineItemResponse(
                name=LINE_ITEM_TYPE_NAME[LineItemType.ConsistencyBonus],
                quantity=quantity,
                rate=rate,
                total=rate * quantity,
            )
        )
