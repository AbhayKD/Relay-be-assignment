from flask import Blueprint, make_response, jsonify
from flask_restful import Api

health_check_blueprint = Blueprint('health_check', __name__)
health_check_blueprint_api = Api(health_check_blueprint)


@health_check_blueprint.route('/health_check')
def check():
    return make_response(jsonify({"message": "All AOK!"}), 200)
