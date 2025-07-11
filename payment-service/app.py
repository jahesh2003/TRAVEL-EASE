from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/pay', methods=['POST'])
def pay():
    data = request.json
    return jsonify({
        "message": "Payment processed successfully!",
        "amount": data.get("amount", 0),
        "status": "success"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

