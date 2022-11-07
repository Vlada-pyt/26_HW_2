from marshmallow import ValidationError
from flask import Flask, request, Blueprint, jsonify

from utils import query_params

app = Flask(__name__)

main_bp = Blueprint('main', __name__)

@app.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        cmd1 = request.args.get('cmd1')
        value1 = request.args.get('value1')
        cmd2 = request.args.get('cmd2')
        value2 = request.args.get('value2')

    except ValidationError as error:
        return jsonify(error.messages), 400
    result = None

    result = query_params(
        cmd1=cmd1,
        value1=value1,
        cmd2=cmd2,
        value2=value2,
        data=result,
        )
    return jsonify(result)


app.run()
