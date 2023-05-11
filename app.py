from typing import Tuple

from flask import Flask, jsonify, Response
from marshmallow import ValidationError

from views.request import request_bp

app = Flask(__name__)
app.register_blueprint(request_bp)


@app.errorhandler(ValidationError)
def validation_error(err: ValidationError) -> Tuple[Response, int]:
    """
    Функция перехвата ошибки валидации запроса пользователя
    """
    return jsonify(err.messages), 400


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
