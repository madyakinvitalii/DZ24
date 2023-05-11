from flask import Blueprint, jsonify, request, Response
from classes.request import UserRequest


request_bp = Blueprint('request_bp', __name__)


@request_bp.route("/perform_query", methods=['POST'])
def perform_query() -> Response:
    data = request.json
    user_request = UserRequest(data)
    return jsonify(user_request.create_procedure())
