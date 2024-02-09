from src.enums import (
    TierRateCardId,
    Tier,
)
from src.constants import RATE_CARD
from src.business_logic.tier.base import BaseTier


class PlatinumTier(BaseTier):
    """
    Represents the platinum tier in the tier-based earnings calculation system.

    This class extends `BaseTier` to implement earnings calculations specific to the platinum tier,
    incorporating additional bonuses and calculations pertinent to this tier level.

    Attributes:
        Inherits all attributes from `BaseTier`.

    Methods:
        calculate_earnings: Overrides to include platinum tier-specific earnings and bonuses.
    """

    def __init__(self) -> None:
        super().__init__(TierRateCardId.PLATINUM, RATE_CARD[Tier.PLATINUM])

    def calculate_earnings(self, activity_logs_df) -> None:
        """
        Calculates total earnings for the platinum tier, including base earnings and applicable bonuses.

        Alongside the base earnings calculation, this method extends the logic to apply
        platinum tier-specific bonuses such as long route bonuses, loyalty bonuses for attempts,
        and consistency bonuses, among others that may be defined for the platinum tier.

        Parameters:
            activity_logs_df (DataFrame): A DataFrame containing activity log entries. Each entry is expected
                                          to include information necessary for calculating various components
                                          of earnings, like 'route_id', 'success', and 'attempt_date_time'.

        Returns:
            bool: A boolean value indicating that the earnings calculation process was executed. This return
                  value is primarily for demonstration and may need adjustment to reflect actual implementation
                  needs or to carry out specific actions based on the calculation outcomes.
        """
        super().calculate_earnings(activity_logs_df)
        super().calculate_long_route_bonus(activity_logs_df)
        super().calculate_loyalty_bonus_attempt(activity_logs_df)
        super().calculate_consistency_bonus(activity_logs_df)
