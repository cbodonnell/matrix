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
    network = Network(resource)
    path = network.find_path(origin_node, destination_node)
    return jsonify(path)


if __name__ == "__main__":
    # app.run()
    app.run(debug=True, use_debugger=False, use_reloader=False, passthrough_errors=True)
