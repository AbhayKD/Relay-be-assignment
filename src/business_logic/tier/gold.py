from src.enums import (
    TierRateCardId,
    Tier,
)
from src.constants import RATE_CARD
from src.business_logic.tier.base import BaseTier


class GoldTier(BaseTier):
    """
    Represents the gold tier in the tier-based earnings calculation system.

    This class extends BaseTier to implement earnings calculations specific to the gold tier,
    focusing on additional bonuses and calculations that are relevant for gold tier participants.

    Attributes:
        Inherits all attributes from BaseTier.

    Methods:
        calculate_earnings: Overrides to include gold tier-specific earnings and bonuses.
    """

    def __init__(self) -> None:
        super().__init__(TierRateCardId.GOLD, RATE_CARD[Tier.GOLD])

    def calculate_earnings(self, activity_logs_df) -> None:
        """
        Calculates total earnings for the gold tier, including base earnings and applicable bonuses.

        In addition to the base earnings calculation, this method applies gold tier-specific logic
        to calculate the consistency bonus among other potential gold tier bonuses.

        Parameters:
            activity_logs_df (DataFrame): A DataFrame containing activity log entries. Each entry should include
                                          information necessary for calculating various components of earnings such as
                                          'route_id', 'success', and 'attempt_date_time'.

        Returns:
            bool: A boolean value indicating that the earnings calculation was performed. This is primarily for
                  demonstration purposes and may be replaced with more meaningful return values or actions
                  as needed in the actual implementation.
        """
        super().calculate_earnings(activity_logs_df)
        super().calculate_consistency_bonus(activity_logs_df)
