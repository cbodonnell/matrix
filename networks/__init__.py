from flask import Flask, request, jsonify
from flask_cors import CORS
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
    nodes = {int(k): v for k, v in resource['nodes'].items()}
    links = {int(k): v for k, v in resource['links'].items()}
    for link in links:
        links[link]['costs'] = {
            int(links[link]['start']): (links[link]['attributes']['length']
                                        / links[link]['attributes']['speeds'][str(links[link]['start'])])
        }
        if not links[link]['attributes']['isOneWay']:
            links[link]['costs'][int(links[link]['end'])] = links[link]['attributes']['length'] \
                                                            / links[link]['attributes']['speeds'][str(links[link]['end'])]
        links[link]['opposite'] = {
            links[link]['start']: links[link]['end'],
            links[link]['end']: links[link]['start']
        }
    network = Network(nodes, links)
    path = network.find_path(origin_node, destination_node)
    return jsonify(path)


if __name__ == "__main__":
    # app.run()
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
