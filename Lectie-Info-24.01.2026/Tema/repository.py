import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DbRepo:   
    def __init__(self, db_config: dict = None):
        if db_config is None:
            self.db_config = {
                'host': os.getenv('DB_HOST', 'localhost'),
                'database': os.getenv('DB_NAME', 'tictactoe'),
                'user': os.getenv('DB_USER', 'postgres'),
                'password': os.getenv('DB_PASSWORD', 'postgres'),
                'port': int(os.getenv('DB_PORT', 5432))
            }
        else:
            self.db_config = db_config
    
    def get_connection(self):
        return psycopg2.connect(**self.db_config)
    
    def create_game(self, player1_id, player2_id=None):
        """Create a new game with empty board"""
        conn = self.get_connection()
        cursor = conn.cursor()
        board = '---------'  # 9 empty cells represented by '-'
        cursor.execute(
            "INSERT INTO games (player1_id, player2_id, board, current_player, status) VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (player1_id, player2_id, board, player1_id, 'waiting')
        )
        game_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return game_id
    
    def get_game(self, game_id):
        """Get game state by ID"""
        conn = self.get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM games WHERE id = %s", (game_id,))
        game = cursor.fetchone()
        conn.close()
        return dict(game) if game else None
    
    def join_game(self, game_id, player_id):
        """Join a waiting game as player 2"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE games SET player2_id = %s, status = %s WHERE id = %s AND status = %s",
            (player_id, 'active', game_id, 'waiting')
        )
        conn.commit()
        conn.close()
    
    def make_move(self, game_id, player_id, position):
        """Make a move on the board (position 1-9)"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Get current game state
        cursor.execute("SELECT board, current_player, player1_id, player2_id FROM games WHERE id = %s", (game_id,))
        result = cursor.fetchone()
        
        if not result:
            conn.close()
            return False
        
        board, current_player, player1_id, player2_id = result
        
        # Validate move
        if current_player != player_id:
            conn.close()
            return False
        
        if board[position] != '-':
            conn.close()
            return False
        
        # Determine player symbol
        symbol = 'X' if player_id == player1_id else 'O'
        
        # Update board
        board_list = list(board)
        board_list[position] = symbol
        new_board = ''.join(board_list)
        
        # Switch player
        next_player = player2_id if current_player == player1_id else player1_id
        
        # Update game
        cursor.execute(
            "UPDATE games SET board = %s, current_player = %s WHERE id = %s",
            (new_board, next_player, game_id)
        )
        conn.commit()
        conn.close()
        return True
    
    def update_game_status(self, game_id, status, winner_id=None):
        """Update game status (active, finished, draw)"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE games SET status = %s, winner_id = %s WHERE id = %s",
            (status, winner_id, game_id)
        )
        conn.commit()
        conn.close()
    
    def get_waiting_games(self):
        """Get all games waiting for a second player"""
        conn = self.get_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("SELECT * FROM games WHERE status = %s", ('waiting',))
        games = cursor.fetchall()
        conn.close()
        return [dict(game) for game in games]
