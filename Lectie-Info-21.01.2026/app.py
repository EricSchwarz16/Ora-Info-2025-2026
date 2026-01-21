from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

fees = [
	{"id": 1, "value": 23, "date": "24-11-2014"},
{"id": 2, "value": 43, "date": "24-11-2024"},
{"id": 3, "value": 253, "date": "24-11-2020"}
]

@app.route('/fees', methods=['GET'])
def get_fees():
    return jsonify(fees), 200

@app.route('/fee', methods=['GET'])
def get_fee_by_id():
    fee_id = request.args.get('id', type=int)
    for fee in fees:
        if fee['id'] == fee_id:
            return jsonify(fee), 200
    return jsonify({"error": "Fee not found"}), 404

@app.route('/fee', methods=['POST'])
def add_fee():
    new_fee = request.get_json()
    fees.append(new_fee)
    return jsonify(new_fee), 201

@app.route('/fee', methods=['DELETE'])
def delete_fee():
    fee_id = request.args.get('id', type=int)
    for fee in fees:
        if fee['id'] == fee_id:
            fees.remove(fee)
            return jsonify({"message": "Fee deleted"}), 200
    return jsonify({"error": "Fee not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

