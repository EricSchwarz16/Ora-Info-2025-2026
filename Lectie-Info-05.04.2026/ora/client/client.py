import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from constants.constants import K, tcp_ports_news, timeframes
import socket

def get_message(option: int):
    PORT = tcp_ports_news[option]
            
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #ne conectam la server
    print("Am deschis clientul")
    client.connect((HOST, PORT))
    print("Sunt conectat la server")
    msg = client.recv(1024)
    
    client.close()
    
    return msg

if __name__ == "__main__":
    HOST = '127.0.0.1'
    
    while True:
        option = input("Choose a timeframe\n1d -> press 1\n7d -> press 2\n1m -> press 3\nexit -> press 0\n")
        
        #mimam api gatewayu
        if option == "1":
            #deschidem conexiune cu news_service ce se ocupa de timeframeu; de o zi
            print(get_message(0))
        elif option == "2":
            print(get_message(1))
        elif option == "3":
            print(get_message(2))
        else:
            break