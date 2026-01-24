from flask import Flask, request, jsonify
from repository import DbRepo
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

#get all messages from chat
@app.route('/chat', methods=['GET'])
def get_messages():
    id = request.args.get('id', type=int)
    
    messages = DbRepo().get_chat_messages(id)
    return jsonify(messages), 200

@app.route('/chat', methods=['POST'])
def add_message():
    content = request.args.get('content', type=str)
    sender_id = request.args.get('sender_id', type=int)
    chat_id = request.args.get('chat_id', type=int)
    timestamp = request.args.get('timestamp', type=str)
    print(timestamp)
    DbRepo().add_chat_message(content, sender_id, chat_id, timestamp)
    return "Succes", 201

if __name__ == '__main__':
    app.run(debug=True)

