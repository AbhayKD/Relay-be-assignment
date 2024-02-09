from flask import jsonify, json
from werkzeug.exceptions import (
    NotFound,
    Forbidden,
    MethodNotAllowed,
    NotImplemented,
    BadRequest,
)
from src.utils.exceptions import (
    APIException,
    ServerErrorException,
    NotFoundException,
    ForbiddenException,
    MethodNotAllowedException,
    NotImplementedException,
    BadRequestException,
)


def handle_exception(error: APIException):
    """
    Handle specific raised API Exception
    """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def handle_general_exception(e):
    """
    Handle general exceptions
    """
    return handle_exception(ServerErrorException(e))


def handle_werkzeug_exception(e):
    """
    Handle Werkzeug Exceptions: return JSON instead of HTML for HTTP errors.
    """
    if isinstance(e, NotFound):
        return handle_exception(NotFoundException(message=e.description))
    if isinstance(e, Forbidden):
        return handle_exception(ForbiddenException(message=e.description))
    if isinstance(e, MethodNotAllowed):
        return handle_exception(MethodNotAllowedException(message=e.description))
    if isinstance(e, NotImplemented):
        return handle_exception(NotImplementedException(message=e.description))
    if isinstance(e, BadRequest):
        return handle_exception(BadRequestException(message=e.description))

    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps(
        {
            "code": e.code,
            "name": e.name,
            "description": e.description,
        }
    )
    response.content_type = "application/json"
    return response
