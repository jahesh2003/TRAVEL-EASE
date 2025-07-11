from flask import Flask, request, jsonify

app = Flask(__name__)
bookings = []

@app.route('/book', methods=['POST'])
def book_flight():
    data = request.json
    bookings.append(data)
    return jsonify({"message": "Flight booked successfully!", "data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

