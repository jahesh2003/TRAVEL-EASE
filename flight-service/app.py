from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/flights', methods=['GET'])
def get_flights():
    flights = [
        {"id": 1, "from": "Delhi", "to": "Mumbai", "airline": "IndiGo", "price": 4500},
        {"id": 2, "from": "Delhi", "to": "Mumbai", "airline": "Air India", "price": 4900},
        {"id": 3, "from": "Delhi", "to": "Mumbai", "airline": "SpiceJet", "price": 4100}
    ]
    return jsonify(flights)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

