# server pentru jocul Bomb Party - TCP pentru input, UDP pentru broadcast

import socket
import time

HOST = "127.0.0.1"
TCP_PORT = 9090
UDP_PORT = 9091
MAX_PLAYERS = 2
INITIAL_LIVES = 3
TURN_TIMEOUT = 10


def send_line(conn, text):
    conn.sendall((text + "\n").encode("utf-8"))


def broadcast(udp_socket, text):
    udp_socket.sendto(text.encode("utf-8"), ("<broadcast>", UDP_PORT))


if __name__ == "__main__":
    players = []

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, TCP_PORT))
    server.listen()

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print(f"[SERVER] Running on {HOST}:{TCP_PORT}")
    print(f"[SERVER] Waiting for {MAX_PLAYERS} players...")

    try:
        while len(players) < MAX_PLAYERS:
            conn, addr = server.accept()
            conn.settimeout(30)

            raw_name = conn.recv(1024)
            conn.settimeout(None)

            if not raw_name:
                conn.close()
                continue

            text = raw_name.decode("utf-8").strip()
            if text.startswith("NAME|") and len(text.split("|", 1)[1].strip()) > 0:
                name = text.split("|", 1)[1].strip()
            else:
                name = f"Player{len(players) + 1}"

            players.append({
                "conn": conn,
                "addr": addr,
                "name": name,
                "lives": INITIAL_LIVES,
                "active": True,
            })

            print(f"[CONNECTED] {name} from {addr}")
            send_line(conn, f"INFO|Welcome, {name}. Wait for game start.")

        print("\n[SERVER] All players connected!")
        language = input("In which language should the game be played? ").strip()
        while not language:
            language = input("Language cannot be empty. In which language should the game be played? ").strip()
        
        print(f"[SERVER] Game will be played in: {language}")
        broadcast(udp_socket, f"Game will be played in: {language}")
        broadcast(udp_socket, "Game started!")
        broadcast(udp_socket, f"Each player has {INITIAL_LIVES} lives.")

        round_number = 1

        while True:
            active_players = [p for p in players if p["active"] and p["lives"] > 0]

            if len(active_players) <= 1:
                break

            trigger = input(f"\n[ROUND {round_number}] Enter trigger: ").strip().lower()
            while not trigger:
                trigger = input("Trigger cannot be empty. Enter trigger: ").strip().lower()

            broadcast(udp_socket, f"\n--- Round {round_number} ---")
            broadcast(udp_socket, f"Trigger is '{trigger}'.")
            broadcast(udp_socket, "All players must respond!")

            # All active players respond to the same trigger
            for idx, player in enumerate(active_players):
                valid_word = False
                reason = ""
                sent_word = ""

                # Notify other players whose turn it is
                for other_player in active_players:
                    if other_player != player:
                        try:
                            send_line(other_player["conn"], f"INFO|It is {player['name']}'s turn!")
                        except Exception:
                            pass

                try:
                    send_line(player["conn"], f"TURN|{trigger}|{TURN_TIMEOUT}")
                    time.sleep(0.1)  # Small delay to ensure client displays prompt
                    player["conn"].settimeout(TURN_TIMEOUT)
                    raw_answer = player["conn"].recv(1024)
                    player["conn"].settimeout(None)

                    if not raw_answer:
                        reason = "disconnected"
                        player["active"] = False
                    else:
                        answer = raw_answer.decode("utf-8").strip()
                        if answer.startswith("WORD|"):
                            sent_word = answer.split("|", 1)[1].strip().lower()
                        else:
                            sent_word = answer.lower()

                        if len(sent_word) > 0 and trigger in sent_word:
                            valid_word = True
                        else:
                            reason = "invalid word"

                except socket.timeout:
                    player["conn"].settimeout(None)
                    reason = "timeout"
                except Exception:
                    player["conn"].settimeout(None)
                    reason = "connection error"
                    player["active"] = False

                if valid_word:
                    # Notify the player individually via TCP
                    try:
                        send_line(player["conn"], f'INFO|"{sent_word}" is a correct possibility!')
                    except Exception:
                        pass
                else:
                    player["lives"] -= 1
                    # Notify the player individually via TCP with reason
                    try:
                        send_line(player["conn"], f"INFO|You lost a life ({reason})! Lives remaining: {player['lives']}")
                    except Exception:
                        pass

                    if player["lives"] <= 0 or not player["active"]:
                        player["active"] = False
                        # Send private elimination message to the eliminated player
                        try:
                            send_line(player["conn"], f"INFO|You got eliminated! Gonna cry?")
                        except Exception:
                            pass
                
                # If not the last player, notify them to wait
                if idx < len(active_players) - 1:
                    try:
                        send_line(player["conn"], f"INFO|Waiting for the other players to answer...")
                    except Exception:
                        pass

            # Announce lives after each round
            broadcast(udp_socket, "\n--- Lives Status ---")
            for player in players:
                if player["active"] and player["lives"] > 0:
                    broadcast(udp_socket, f"{player['name']}: {player['lives']} lives")
            
            # Send elimination notifications to OTHER players AFTER lives status broadcast
            for player in active_players:
                if player["lives"] <= 0 or not player["active"]:
                    # Send elimination notification to all OTHER players via TCP
                    for other_player in players:
                        if other_player != player and other_player["active"]:
                            try:
                                send_line(other_player["conn"], f"INFO|{player['name']} was eliminated!")
                            except Exception:
                                pass

            round_number += 1

        alive = [p for p in players if p["active"] and p["lives"] > 0]
        if len(alive) == 1:
            final_msg = f"Winner is {alive[0]['name']}!"
        else:
            final_msg = "No winner (all eliminated/disconnected)."

        broadcast(udp_socket, final_msg)

        # Send END signal to all players via TCP (without repeating the message)
        for player in players:
            try:
                send_line(player["conn"], "END|")
            except Exception:
                pass

    finally:
        for player in players:
            try:
                player["conn"].close()
            except Exception:
                pass
        udp_socket.close()
        server.close()
        print("[SERVER] Stopped.")