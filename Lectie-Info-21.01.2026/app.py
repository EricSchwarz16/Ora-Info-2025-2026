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

# PUT -> schimbam tot
@app.route('/fee', methods=['PUT'])
def update_fee():
    fee_id = request.args.get('id', type=int)
    value = request.args.get('value', type=int)
    date = request.args.get('date', type=str)
    
    for fee in fees:
        if fee['id'] == fee_id:
            fees.remove(fee)
            fees.append({"id": fee_id, "value": value, "date": date})
            return jsonify({"message": "Fee updated"}), 200
    return jsonify({"error": "Fee not updated"}), 404

# PATCH -> schimbam doar anumite campuri

@app.route('/fee', methods=['PATCH'])
def update_partial_fee():
    fee_id = request.args.get('id', type=int)
    value = request.args.get('value', type=int)
    
    for fee in fees:
        if fee['id'] == fee_id:
            fee['value'] = value
            return jsonify({"message": "Fee updated"}), 200
    return jsonify({"error": "Fee not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

