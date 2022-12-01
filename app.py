from marshmallow import ValidationError
from flask import Flask, request, Blueprint, jsonify

from db import db
from utils import query_params

DB_USER = 'db_user'
DB_PASSWORD ='db_password'
DB_NAME = 'db_name'
DB_PORT = 5434
DB_HOST = '127.0.0.1'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
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

@app.route("/test_db")
def db_test():
    result = db.session.execute('SELECT 1').scalar_one()
    return jsonify({'result': result,},)

app.run(host='127.0.0.1', port=25000)
