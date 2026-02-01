# TicTacToe Game with Flask and PostgreSQL

A multiplayer TicTacToe game using Flask backend and PostgreSQL database, based on the chat app architecture.

## Setup

### 1. Install PostgreSQL
- Install PostgreSQL on your system
- Create a database named `tictactoe`

### 2. Run Database Migrations
```bash
psql -U postgres -d tictactoe -f migrations.sql
```

Or connect to PostgreSQL and run the SQL commands manually:
```sql
CREATE DATABASE tictactoe;
\c tictactoe
-- Then run the contents of migrations.sql
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database Connection
Create a `.env` file in the project root with your PostgreSQL credentials:
```env
DB_HOST=localhost
DB_NAME=tictactoe
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_PORT=5432
```

**Note:** Never commit the `.env` file to version control! It contains sensitive credentials.

## Running the Game

### Start the Server
```bash
python app.py
```

### Start Clients (in separate terminals)
```bash
python client.py
```

## How to Play

1. **Player 1**: Run client and select "Create new game"
2. **Player 2**: Run another client and select "Join existing game" or "List waiting games" to find the game ID
3. Players take turns entering positions (1-9) to place their marks
4. First player is X, second player is O
5. Game ends when someone wins or it's a draw

## API Endpoints

- `POST /game?player_id=X` - Create new game
- `GET /game/<game_id>` - Get game state
- `POST /game/<game_id>/join?player_id=X` - Join waiting game
- `POST /game/<game_id>/move?player_id=X&position=Y` - Make a move
- `GET /games/waiting` - List all waiting games

## Board Positions
```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```
