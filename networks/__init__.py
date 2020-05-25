from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object('config')
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:4200"}})


@app.route('/api/path', methods=['POST'])
def find_path():
    body = request.get_json()
    print(body)
    origin = int(request.args.get('origin', None))
    destination = int(request.args.get('destination', None))
    #  Find path
    response = [100, 200, 300]
    return jsonify(response)


if __name__ == "__main__":
    app.run()
