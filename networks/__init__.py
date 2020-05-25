from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from networks.models import Network


app = Flask(__name__)
app.config.from_object('config')
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})


@app.route('/api/path', methods=['POST'])
def find_path():
    resource = request.get_json()
    origin_node = int(request.args.get('origin', None))
    destination_node = int(request.args.get('destination', None))
    # TODO: Refactor to network constructor method
    inbound = {int(k): v['inbound'] for k, v in resource['nodes'].items()}
    outbound = {int(k): v['outbound'] for k, v in resource['nodes'].items()}
    links = {int(k): i for i, k in enumerate(resource['links'])}
    num_links = len(resource['links'])
    turn_matrix = np.full((num_links, num_links), False)
    for origin in resource['links']:
        for destination in resource['links'][origin]['destinations']:
            turn_matrix[links[int(origin)]][links[destination]] = True
    network = Network(links, inbound, outbound, turn_matrix)
    path = network.find_path(origin_node, destination_node)
    return jsonify(path)


if __name__ == "__main__":
    # app.run()
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
