from marshmallow import ValidationError
from flask import Flask, request, Blueprint, jsonify
from models import RequestParams
from utils import query_params

app = Flask(__name__)

main_bp = Blueprint('main', __name__)

@app.route('/perform_query', methods=['POST'])
def perform_query():
    try:
        params = RequestParams().load(data=request.json)
    except ValidationError as error:
        return jsonify(error.messages), 400
    result = None
    for q in params['queries']:
        result = query_params(
            cmd=q['cmd'],
            value=q['value'],
            data=result,
        )
    return jsonify(result)


app.run()
