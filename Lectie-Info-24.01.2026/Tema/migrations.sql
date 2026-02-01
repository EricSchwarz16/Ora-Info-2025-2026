-- PostgreSQL database setup for TicTacToe game

-- Create database (run this separately first)
-- CREATE DATABASE tictactoe;

-- Connect to tictactoe database and run the following:

CREATE TABLE IF NOT EXISTS games (
    id SERIAL PRIMARY KEY,
    player1_id INTEGER NOT NULL,
    player2_id INTEGER,
    board VARCHAR(9) NOT NULL DEFAULT '---------',
    current_player INTEGER NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'waiting',  -- 'waiting', 'active', 'finished'
    winner_id INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create index for faster lookups
CREATE INDEX idx_games_status ON games(status);
CREATE INDEX idx_games_player1 ON games(player1_id);
CREATE INDEX idx_games_player2 ON games(player2_id);

-- Optional: Create trigger to update updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_games_updated_at BEFORE UPDATE ON games
FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
