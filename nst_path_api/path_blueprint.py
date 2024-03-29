from flask import Blueprint
from flask import request, jsonify
from nst_path_api.models import Network


path_blueprint = Blueprint('example_blueprint', __name__)


@path_blueprint.route('/api/hello', methods=['GET'])
def hello():
    return 'Hello world! This was updated on 06/12/2021.'


@path_blueprint.route('/api/path', methods=['POST'])
def find_path():
    resource = request.get_json()
    origin_node = int(request.args.get('origin', None))
    destination_node = int(request.args.get('destination', None))
    network = Network(resource)
    path = network.find_path(origin_node, destination_node)
    return jsonify(path)

