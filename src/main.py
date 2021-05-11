"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Current
# from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object


@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints


@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/current', methods=['GET'])
def get_all_current():
    all_current = Current.query.all()
    currents_serialized = []
    for current in all_current:
        print(current.serialize)
        currents_serialized.append = ("current.serialize")
    return jsonify(currents_serialized), 200


@app.route('/parent', methods=['GET'])
def get_all_current():
    all_parent = Parent.query.all()
    parents_serialized = []
    for parent in all_parent:
        print(parent.serialize)
        parents_serialized.append = ("parent.serialize")
    return jsonify(currents_serialized), 200


@app.route('/grandParent', methods=['GET'])
 def get_all_current():
    all_grandParent = GrandParent.query.all()
    GrandParents = []
    for Parent in all_GrandParent:
         print(GrandParents.serialize())
        GrandParents.append(GrandParent.serialize)

    return jsonify(GrandParents), 200   



if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
