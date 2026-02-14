import socket
import threading

HOST = '127.0.0.1'
PORT = 9090

connected = True

def receive_messages(client):
    """Thread care primeste mesaje de la server"""
    global connected
    while connected:
        try:
            msg = client.recv(1024)
            if msg:
                print(msg.decode('utf-8'), end='')
            else:
                break
        except Exception as e:
            print(f"\n[ERROR] Connection error: {e}")
            break
    
    connected = False

def send_answers(client):
    """Thread care trimite raspunsuri la server"""
    global connected
    while connected:
        try:
            answer = input()
            if answer:
                client.send(answer.encode('utf-8'))
        except Exception as e:
            print(f"\n[ERROR] Sending error: {e}")
            break

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conectare la server
        client.connect((HOST, PORT))
        print(f"[CONNECTED] Connected to quiz server at {HOST}:{PORT}")
        
        # Start thread pentru primirea mesajelor
        receive_thread = threading.Thread(target=receive_messages, args=(client,))
        receive_thread.daemon = True
        receive_thread.start()
        
        # Start thread pentru trimiterea raspunsurilor
        send_thread = threading.Thread(target=send_answers, args=(client,))
        send_thread.daemon = True
        send_thread.start()
        
        # Asteapta pana cand conexiunea se inchide
        receive_thread.join()
        
    except Exception as e:
        print(f"[ERROR] Could not connect to server: {e}")
    finally:
        client.close()
        print("\n[DISCONNECTED] Disconnected from server.")
