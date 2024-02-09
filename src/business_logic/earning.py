from pandas import DataFrame
from src.model import ActivityLog, EarningStatementResponse
from src.enums import TierRateCardId
from src.business_logic.tier import BronzeTier, SilverTier, GoldTier, PlatinumTier


class Earning:
    """
    A class responsible for calculating and generating an earnings statement for a given set of activity logs
    and a specified tier rate card.

    Attributes:
        rate_card_id (TierRateCardId): The tier rate card ID indicating the earnings tier.
        activity_logs (list[ActivityLog]): A list of activity logs to be considered for earnings calculation.

    Methods:
        get_tier: Determines the tier object based on the rate card ID.
        generate_statement: Generates an earnings statement based on activity logs and the specified tier.
    """

    def __init__(
        self, rate_card_id: TierRateCardId, activity_logs: list[ActivityLog]
    ) -> None:
        self.rate_card_id = rate_card_id
        self.activity_logs = activity_logs

    def get_tier(self):
        """
        Determines and returns the tier object based on the rate card ID.

        Returns:
            An instance of the tier class (BronzeTier, SilverTier, GoldTier, PlatinumTier) corresponding
            to the rate card ID.
        """
        match self.rate_card_id.value:
            case TierRateCardId.BRONZE.value:
                return BronzeTier()
            case TierRateCardId.SILVER.value:
                return SilverTier()
            case TierRateCardId.GOLD.value:
                return GoldTier()
            case TierRateCardId.PLATINUM.value:
                return PlatinumTier()

    def generate_statement(self) -> EarningStatementResponse:
        """
        Calculates earnings based on the tier and activity logs, and generates an earnings statement.

        Converts the activity logs into a DataFrame, calculates the earnings using the appropriate tier object,
        and compiles the results into an EarningStatementResponse.

        Returns:
            EarningStatementResponse: An object containing detailed earnings information, including line items,
                                      subtotal, minimum earnings, hours worked, and final earnings.
        """
        tier = self.get_tier()
        activity_logs_df = DataFrame.from_records([log for log in self.activity_logs])
        tier.calculate_earnings(activity_logs_df)
        return EarningStatementResponse(
            line_items=tier.line_items,
            line_item_subtotal=tier.line_items_subtotal,
            minimum_earnings=tier.minimum_earnings,
            hours_worked=tier.hours_worked,
            final_earnings=tier.final_earnings,
        )
