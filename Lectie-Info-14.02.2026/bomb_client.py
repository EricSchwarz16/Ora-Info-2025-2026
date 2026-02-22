# client pentru jocul Bomb Party - TCP pentru input, UDP pentru broadcast

import socket
import threading

HOST = "127.0.0.1"
TCP_PORT = 9090
UDP_PORT = 9091
is_running = True


def send_line(conn, text):
    conn.sendall((text + "\n").encode("utf-8"))


def listen_udp(udp_socket):
    global is_running
    while is_running:
        try:
            msg = udp_socket.recvfrom(1024)
            print(msg[0].decode("utf-8"))
        except Exception:
            break


if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        udp_socket.bind(("", UDP_PORT))

        client.connect((HOST, TCP_PORT))
        print(f"[CONNECTED] Connected to server {HOST}:{TCP_PORT}")

        name = input("Enter your name: ").strip()
        if not name:
            name = "Anonymous"

        send_line(client, f"NAME|{name}")

        udp_thread = threading.Thread(target=listen_udp, args=(udp_socket,))
        udp_thread.daemon = True
        udp_thread.start()

        buffer = ""
        running_tcp = True

        while running_tcp:
            data = client.recv(1024)
            if not data:
                break

            buffer += data.decode("utf-8")
            lines = buffer.split("\n")
            buffer = lines[-1]

            for line in lines[:-1]:
                line = line.strip()
                if not line:
                    continue

                if line.startswith("INFO|"):
                    print(line.split("|", 1)[1])
                elif line.startswith("TURN|"):
                    parts = line.split("|")
                    if len(parts) >= 3:
                        trigger = parts[1]
                        timeout_seconds = parts[2]
                        print()  # Add blank line before prompt for visibility
                        word = input(
                            f"[YOUR TURN] Enter a word containing '{trigger}' (max {timeout_seconds}s): "
                        ).strip()
                        send_line(client, f"WORD|{word}")
                elif line.startswith("END|"):
                    # Server signals game end; final message comes via UDP
                    running_tcp = False
                    break
                else:
                    print(line)

    except Exception as e:
        print(f"[ERROR] Connection failed: {e}")
    finally:
        is_running = False
        try:
            udp_socket.close()
        except Exception:
            pass
        client.close()
        print("[DISCONNECTED] Disconnected.")
