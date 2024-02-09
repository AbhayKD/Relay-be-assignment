from src.enums import (
    TierRateCardId,
    Tier,
)
from src.constants import RATE_CARD
from src.business_logic.tier.base import BaseTier


class BronzeTier(BaseTier):
    """
    Represents the bronze tier in the tier-based earnings calculation system.

    This class extends BaseTier to implement earnings calculations specific to the bronze tier,
    including base earnings calculations and additional bonuses relevant to the bronze tier.

    Attributes:
        Inherits all attributes from BaseTier.

    Methods:
        calculate_earnings: Overrides to include bronze tier-specific earnings and bonuses.
    """

    def __init__(self) -> None:
        super().__init__(TierRateCardId.BRONZE, RATE_CARD[Tier.BRONZE])

    def calculate_earnings(self, activity_logs_df) -> None:
        """
        Calculates total earnings for the bronze tier, including base earnings and applicable bonuses.

        This method extends the base earnings calculation with additional logic to apply bronze tier-specific
        bonuses such as long route bonuses and loyalty bonuses for routes.

        Parameters:
            activity_logs_df (DataFrame): A DataFrame containing activity log entries. Each entry should include
                                          information such as 'route_id', 'success', and 'attempt_date_time' to
                                          calculate various components of earnings.
        """
        super().calculate_earnings(activity_logs_df)
        super().calculate_long_route_bonus(activity_logs_df)
        super().calculate_loyalty_bonus_route(activity_logs_df)
