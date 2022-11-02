from marshmallow import ValidationError
from flask import Flask, request, Blueprint, jsonify

from utils import query_params

app = Flask(__name__)

main_bp = Blueprint('main', __name__)

@app.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        cmd = request.args.get('cmd1')
        value = request.args.get('value1')

    except ValidationError as error:
        return jsonify(error.messages), 400
    result = None

    result = query_params(
        cmd=cmd,
        value=value,
        data=result,
        )
    return jsonify(result)


app.run()
