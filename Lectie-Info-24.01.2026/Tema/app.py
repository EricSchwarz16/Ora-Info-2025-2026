from flask import Flask, request, jsonify
from repository import DbRepo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def check_winner(board):
    """Check if there's a winner. Returns 'X', 'O', 'draw', or None"""
    # Winning combinations
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != '-':
            return board[combo[0]]
    
    # Check for draw
    if '-' not in board:
        return 'draw'
    
    return None

@app.route('/game', methods=['POST'])
def create_game():
    """Create a new game"""
    player_id = request.args.get('player_id', type=int)
    
    if not player_id:
        return jsonify({'error': 'Player ID required'}), 400
    
    game_id = DbRepo().create_game(player_id)
    return jsonify({'game_id': game_id}), 201

@app.route('/game/<int:game_id>', methods=['GET'])
def get_game(game_id):
    """Get game state"""
    game = DbRepo().get_game(game_id)
    
    if not game:
        return jsonify({'error': 'Game not found'}), 404
    
    return jsonify(game), 200

@app.route('/game/<int:game_id>/join', methods=['POST'])
def join_game(game_id):
    """Join a waiting game"""
    player_id = request.args.get('player_id', type=int)
    
    if not player_id:
        return jsonify({'error': 'Player ID required'}), 400
    
    DbRepo().join_game(game_id, player_id)
    return jsonify({'message': 'Joined game'}), 200

@app.route('/game/<int:game_id>/move', methods=['POST'])
def make_move(game_id):
    """Make a move in the game"""
    player_id = request.args.get('player_id', type=int)
    position = request.args.get('position', type=int)
    
    if player_id is None or position is None:
        return jsonify({'error': 'Player ID and position required'}), 400
    
    if position < 0 or position > 8:
        return jsonify({'error': 'Position must be between 0 and 8'}), 400
    
    # Make move
    success = DbRepo().make_move(game_id, player_id, position)
    
    if not success:
        return jsonify({'error': 'Invalid move'}), 400
    
    # Check for winner
    game = DbRepo().get_game(game_id)
    result = check_winner(game['board'])
    
    if result == 'draw':
        DbRepo().update_game_status(game_id, 'finished')
    elif result:
        # Winner found
        winner_id = game['player1_id'] if result == 'X' else game['player2_id']
        DbRepo().update_game_status(game_id, 'finished', winner_id)
    
    return jsonify({'message': 'Move made', 'result': result}), 200

@app.route('/games/waiting', methods=['GET'])
def get_waiting_games():
    """Get all games waiting for players"""
    games = DbRepo().get_waiting_games()
    return jsonify(games), 200

if __name__ == '__main__':
    app.run(debug=True)
