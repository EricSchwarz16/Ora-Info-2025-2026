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

if __name__ == '__main__':
    app.run(debug=True)