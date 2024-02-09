from flask import Blueprint
from flask_restful import Api


earning_blueprint = Blueprint("earning", __name__)
earning_blueprint_api = Api(earning_blueprint)


from src.resource.earning import EarningAPI

earning_blueprint_api.add_resource(EarningAPI, "/earning/<string:rate_card_id>")
