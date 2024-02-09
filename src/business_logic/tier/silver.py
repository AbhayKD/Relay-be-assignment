from src.enums import (
    TierRateCardId,
    Tier,
)
from src.constants import RATE_CARD
from src.business_logic.tier.base import BaseTier


class SilverTier(BaseTier):
    """
    Represents the silver tier in the tier-based earnings calculation system.

    Extends the `BaseTier` class to implement the earnings calculations specific to the silver tier,
    adding additional bonuses and calculations unique to this level of tier.

    Attributes:
        Inherits all attributes from `BaseTier`.

    Methods:
        calculate_earnings: Enhances the base earnings calculation with silver tier-specific bonuses.
    """

    def __init__(self) -> None:
        super().__init__(TierRateCardId.SILVER, RATE_CARD[Tier.SILVER])

    def calculate_earnings(self, activity_logs_df) -> None:
        """
        Calculates the total earnings for the silver tier, including the base earnings and additional bonuses
        applicable to this tier.

        This method calls upon the base class's calculation method to compute common earnings and further
        extends it with silver tier-specific bonuses such as loyalty bonus for attempts and quality bonus for attempts.

        Parameters:
            activity_logs_df (DataFrame): A DataFrame containing activity log entries, which include essential
                                          information for calculating various components of earnings, like 'route_id',
                                          'success', and 'attempt_date_time'.
        """
        super().calculate_earnings(activity_logs_df)
        super().calculate_loyalty_bonus_attempt(activity_logs_df)
        super().calculate_quality_bonus_attempt(activity_logs_df)
