from enum import Enum


class BasicStringEnum(Enum):
    def __str__(self):
        return self.value

    @classmethod
    def get_enum_by_value(cls, value):
        for member in cls:
            if member.value == value:
                return member
        return None

    @classmethod
    def get_value(cls, tier):
        return cls.values.get(tier)


class Tier(BasicStringEnum):
    """
    Enum representing different tiers.
    """

    BRONZE = "BRONZE"
    SILVER = "SILVER"
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"


class TierRateCardId(BasicStringEnum):
    """
    Enum representing identifiers for rate cards associated with each tier.
    """

    BRONZE = "bronze_tier"
    SILVER = "silver_tier"
    GOLD = "gold_tier"
    PLATINUM = "platinum_tier"


class LineItemType(BasicStringEnum):
    """
    Enum representing types of line items that can contribute to earnings calculations.
    """

    PerSuccessfulAttempt = "perSuccessfulAttempt"
    PerUnsuccessfulAttempt = "perUnsuccessfulAttempt"
    LongRouteBonus = "longRouteBonus"
    LoyaltyBonusRoutes = "loyaltyBonusRoutes"
    LoyaltyBonusAttempts = "loyaltyBonusAttempts"
    QualityBonus = "qualityBonus"
    ConsistencyBonus = "consistencyBonus"
