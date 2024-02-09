from src.enums import LineItemType, Tier
from src.model import LineItem, RateCard

# Mapping of line item types to their descriptive names.
LINE_ITEM_TYPE_NAME = {
    LineItemType.PerSuccessfulAttempt: "Per successful attempt",
    LineItemType.PerUnsuccessfulAttempt: "Per unsuccessful attempt",
    LineItemType.LongRouteBonus: "Long route bonus",
    LineItemType.LoyaltyBonusAttempts: "Loyalty Bonus (attempts)",
    LineItemType.LoyaltyBonusRoutes: "Loyalty Bonus (routes)",
    LineItemType.ConsistencyBonus: "Consistency Bonus",
    LineItemType.QualityBonus: "Quality Bonus",
}


"""
Defines the RATE_CARD dictionary to map each Tier to its corresponding RateCard instance.

Each RateCard instance specifies:
- hourly_minimum_earnings: The minimum hourly earnings for the tier.
- line_items: A dictionary mapping LineItemType to LineItem instances, which define the rate for each type of earning or deduction applicable to the tier.

This structure allows for flexible configuration of earnings calculations based on tier and line item type.
"""
RATE_CARD = {
    Tier.BRONZE: RateCard(
        hourly_minimum_earnings=14.50,
        line_items={
            LineItemType.PerSuccessfulAttempt: LineItem(rate=0.459),
            LineItemType.PerUnsuccessfulAttempt: LineItem(rate=0.229),
            LineItemType.LongRouteBonus: LineItem(
                rate=10.00,
            ),
            LineItemType.LoyaltyBonusRoutes: LineItem(
                rate=20.00,
            ),
        },
    ),
    Tier.SILVER: RateCard(
        hourly_minimum_earnings=13.50,
        line_items={
            LineItemType.PerSuccessfulAttempt: LineItem(rate=0.65),
            LineItemType.PerUnsuccessfulAttempt: LineItem(rate=0.00),
            LineItemType.LoyaltyBonusAttempts: LineItem(
                rate=19.00,
            ),
            LineItemType.QualityBonus: LineItem(
                rate=25.00,
            ),
        },
    ),
    Tier.GOLD: RateCard(
        hourly_minimum_earnings=15.00,
        line_items={
            LineItemType.PerSuccessfulAttempt: LineItem(rate=0.511),
            LineItemType.PerUnsuccessfulAttempt: LineItem(rate=0.126),
            LineItemType.ConsistencyBonus: LineItem(
                rate=32.00,
            ),
        },
    ),
    Tier.PLATINUM: RateCard(
        hourly_minimum_earnings=15.25,
        line_items={
            LineItemType.PerSuccessfulAttempt: LineItem(rate=0.667),
            LineItemType.PerUnsuccessfulAttempt: LineItem(rate=0.155),
            LineItemType.LongRouteBonus: LineItem(
                rate=12.00,
            ),
            LineItemType.LoyaltyBonusAttempts: LineItem(
                rate=19.00,
            ),
            LineItemType.ConsistencyBonus: LineItem(
                rate=32.00,
            ),
        },
    ),
}
