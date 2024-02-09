from flask import Flask
from src import config


def create_app():
    server = Flask(__name__)
    server.debug = config.DEBUG
    return server


server = create_app()

from src.route.health_check import health_check_blueprint
from src.route.earning import earning_blueprint


server.register_blueprint(health_check_blueprint)
server.register_blueprint(earning_blueprint)

from werkzeug.exceptions import HTTPException
from src.utils import exceptions, error_handlers

server.register_error_handler(
    exceptions.InvalidPayloadException, error_handlers.handle_exception
)
server.register_error_handler(
    exceptions.BadRequestException, error_handlers.handle_exception
)
server.register_error_handler(
    exceptions.ForbiddenException, error_handlers.handle_exception
)
server.register_error_handler(
    exceptions.NotFoundException, error_handlers.handle_exception
)
server.register_error_handler(
    exceptions.ServerErrorException, error_handlers.handle_exception
)
server.register_error_handler(Exception, error_handlers.handle_general_exception)
server.register_error_handler(HTTPException, error_handlers.handle_werkzeug_exception)

if __name__ == "__main__":
    server.run(host=config.HOST, port=config.PORT, debug=True)
