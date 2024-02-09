from dataclasses import dataclass, asdict, field
from marshmallow import Schema, fields
import datetime


@dataclass
class GenericDataClass:
    def to_dict(self):
        return asdict(self)


@dataclass
class ActivityLog(GenericDataClass):
    route_id: str
    attempt_date_time: datetime
    success: bool


@dataclass
class LineItemResponse(GenericDataClass):
    name: str
    quantity: int = 0
    rate: float = 0.0
    total: float = 0.0


@dataclass
class EarningStatementResponse(GenericDataClass):
    line_items: list[LineItemResponse] = field(default_factory=list)
    line_item_subtotal: float = 0.0
    hours_worked: float = 0.0
    minimum_earnings: float = 0.0
    final_earnings: float = 0.0


# schema for deserialization
class ActivityLogSchema(Schema):
    route_id = fields.Str(required=True)
    attempt_date_time = fields.DateTime(required=True)
    success = fields.Boolean(required=True)


class LineItem:
    __slots__ = ["rate"]

    def __init__(self, rate):
        self.rate = rate


class RateCard:
    __slots__ = ["hourly_minimum_earnings", "line_items"]

    def __init__(self, hourly_minimum_earnings, line_items):
        self.hourly_minimum_earnings = hourly_minimum_earnings
        self.line_items = line_items
