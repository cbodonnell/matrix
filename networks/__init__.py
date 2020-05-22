from flask import Flask, request, jsonify


app = Flask(__name__)
app.config.from_object('config')


@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(['data'])


@app.route('/api/data', methods=['POST'])
def set_data():
    body = request.get_json()
    origin = int(request.args.get('origin', None))
    destination = int(request.args.get('destination', None))
    response = {
        'origin': origin,
        'destination': destination,
        'body': body
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run()
