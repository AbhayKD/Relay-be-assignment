from flask import request
from flask_restful import Resource
from marshmallow import ValidationError
from src.enums import TierRateCardId
from src.utils.exceptions import ValidationException, InvalidPayloadException
from src.model import ActivityLogSchema
from src.business_logic.earning import Earning


class EarningAPI(Resource):
    def post(self, rate_card_id):
        try:
            rate_card_id_enum = TierRateCardId.get_enum_by_value(rate_card_id)
            if not rate_card_id_enum:
                raise ValidationException("Invalid rate card id provided")
            body = request.get_json()
            activity_logs = ActivityLogSchema(many=True)
            logs = activity_logs.load(body)
            if not len(logs):
                raise InvalidPayloadException("No activity logs found")
            
            earning_logic = Earning(rate_card_id=rate_card_id_enum, activity_logs=logs)
            earnings = earning_logic.generate_statement().to_dict()
            return earnings, 200
        except ValidationError as e:
            raise ValidationException(e)
