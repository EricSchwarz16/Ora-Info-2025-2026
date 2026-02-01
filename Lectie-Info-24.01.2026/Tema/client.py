import requests
import random
import threading
import time

user_id = random.randint(1, 100)
game_id = None
stop_worker = False
my_turn = False

def display_board(board):
    """Display the TicTacToe board"""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")
    print("Position numbers:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\n")

def game_worker():
    """Worker thread to check for game updates"""
    global game_id, stop_worker, my_turn
    last_board = None
    last_status = None
    last_current_player = None
    
    while not stop_worker:
        time.sleep(1.5)
        
        response = requests.get(f"http://127.0.0.1:5000/game/{game_id}")
        
        if response.status_code == 200:
            game = response.json()
            
            # Display board if it changed
            if game['board'] != last_board:
                last_board = game['board']
                print("\n" + "="*30)
                display_board(game['board'])
                print("="*30)
            
            # Check if turn changed
            if game['current_player'] != last_current_player and game['status'] == 'active':
                last_current_player = game['current_player']
                my_turn = (game['current_player'] == user_id)
                if my_turn:
                    print(f"\n>>> YOUR TURN! (You are {'X' if game['player1_id'] == user_id else 'O'})")
                else:
                    print("\n>>> Opponent's turn, waiting...")
                
            # Check game status
            if game['status'] == 'finished' and last_status != 'finished':
                last_status = 'finished'
                if game['winner_id']:
                    if game['winner_id'] == user_id:
                        print("\n🎉 YOU WON! 🎉")
                    else:
                        print("\n😢 You lost!")
                else:
                    print("\n🤝 It's a draw!")
                stop_worker = True

print(f"Your Player ID: {user_id}")
print("\n=== TicTacToe Game ===\n")

while True:
    print("1. Create new game")
    print("2. Join existing game")
    print("3. List waiting games")
    print("0. Exit")
    
    option = input("Enter your option: ")
    
    if option == "0":
        break
    
    elif option == "1":
        # Create new game
        try:
            response = requests.post(f"http://127.0.0.1:5000/game?player_id={user_id}")
            if response.status_code == 201:
                game_id = response.json()['game_id']
                print(f"Game created! Game ID: {game_id}")
                print("Waiting for another player to join...")
                
                # Start worker thread
                stop_worker = False
                my_turn = False
                worker = threading.Thread(target=game_worker, daemon=True)
                worker.start()
                
                # Wait for player to join
                while True:
                    game = requests.get(f"http://127.0.0.1:5000/game/{game_id}").json()
                    if game['status'] != 'waiting':
                        print("Player 2 joined! Game starting...")
                        time.sleep(1)
                        break
                    time.sleep(1)
                
                # Game loop - only handle input
                while not stop_worker:
                    game = requests.get(f"http://127.0.0.1:5000/game/{game_id}").json()
                    
                    if game['status'] == 'finished':
                        break
                    
                    if game['current_player'] == user_id:
                        try:
                            position = input("Enter position (1-9): ")
                            position = int(position) - 1  # Convert to 0-8 for backend
                            if position < 0 or position > 8:
                                print("❌ Please enter a number between 1 and 9")
                                continue
                            response = requests.post(
                                f"http://127.0.0.1:5000/game/{game_id}/move?player_id={user_id}&position={position}"
                            )
                            
                            if response.status_code != 200:
                                print(f"❌ Invalid move: {response.json().get('error', 'Unknown error')}")
                            else:
                                print("✓ Move made!")
                                time.sleep(0.3)  # Brief pause before re-checking state
                        except ValueError:
                            print("❌ Please enter a valid number (1-9)")
                        except KeyboardInterrupt:
                            print("\nExiting game...")
                            stop_worker = True
                            break
                    else:
                        time.sleep(0.5)  # Short sleep when not our turn
                
                stop_worker = True
                time.sleep(2)  # Wait for worker to finish
                
        except Exception as e:
            print(f"Error creating game: {e}")
    
    elif option == "2":
        # Join existing game
        try:
            game_id = int(input("Enter game ID to join: "))
            response = requests.post(f"http://127.0.0.1:5000/game/{game_id}/join?player_id={user_id}")
            
            if response.status_code == 200:
                print(f"Joined game {game_id}!")
                
                # Start worker thread
                stop_worker = False
                my_turn = False
                worker = threading.Thread(target=game_worker, daemon=True)
                worker.start()
                
                time.sleep(1)  # Give worker time to display initial board
                
                # Game loop - only handle input
                while not stop_worker:
                    game = requests.get(f"http://127.0.0.1:5000/game/{game_id}").json()
                    
                    if game['status'] == 'finished':
                        break
                    
                    if game['current_player'] == user_id:
                        try:
                            position = input("Enter position (1-9): ")
                            position = int(position) - 1  # Convert to 0-8 for backend
                            if position < 0 or position > 8:
                                print("❌ Please enter a number between 1 and 9")
                                continue
                            response = requests.post(
                                f"http://127.0.0.1:5000/game/{game_id}/move?player_id={user_id}&position={position}"
                            )
                            
                            if response.status_code != 200:
                                print(f"❌ Invalid move: {response.json().get('error', 'Unknown error')}")
                            else:
                                print("✓ Move made!")
                                time.sleep(0.3)  # Brief pause before re-checking state
                        except ValueError:
                            print("❌ Please enter a valid number (1-9)")
                        except KeyboardInterrupt:
                            print("\nExiting game...")
                            stop_worker = True
                            break
                    else:
                        time.sleep(0.5)  # Short sleep when not our turn
                
                stop_worker = True
                time.sleep(2)  # Wait for worker to finish
            else:
                print("Failed to join game")
                
        except Exception as e:
            print(f"Error joining game: {e}")
    
    elif option == "3":
        # List waiting games
        try:
            response = requests.get("http://127.0.0.1:5000/games/waiting")
            if response.status_code == 200:
                games = response.json()
                if games:
                    print("\nWaiting Games:")
                    for game in games:
                        print(f"  Game ID: {game['id']}, Created by Player: {game['player1_id']}")
                else:
                    print("No waiting games found.")
        except Exception as e:
            print(f"Error fetching games: {e}")
