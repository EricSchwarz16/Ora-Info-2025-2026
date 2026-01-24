import requests
import random
import threading
import datetime
import time
user_id = random.randint(1, 100)
global chatId 
global chatMessages 

def message_worker():
    global chatId 
    global chatMessages 
    
    while(True):
        time.sleep(1)
        messages = requests.get(f"http://127.0.0.1:5000/chat?id={chatId}").json()
        newMessages = []
        
        for message in messages:
            ok = False
            
            for prevMessages in chatMessages:
                if prevMessages[3] == message[3] and prevMessages[4] == message[4] and message[2] == message[2]:
                    ok = True
                    break
            
            if not ok:
                newMessages.append(message)
                
        chatMessages = messages
        
        for message in newMessages:
            print(f"UserId: {message[3]}, timestamp: {message[2]}\nMessage: {message[4]}\n")



while(True):
    
    chatId = int(input("Choose a chatId: "))
    
    #ne connectam la chat
    
    chatMessages = requests.get(f"http://127.0.0.1:5000/chat?id={chatId}")
    
    #worker care verifica mesaje noi
    worker = threading.Thread(target=message_worker)
    worker.start()
    
    while(True):
        print("1. add message")
        print("0. exit")
        option = input("Enter your option: ")
        
        if option == "0":
            worker.join() #inchidem subprogramul care da fetch la mesajele noi
            break
        elif option == "1":
            content = input("Enter your message: ")
            print(user_id)
            #add message to array
            chatMessages.append(["", "", "", user_id, content])
            timestamp = datetime.datetime.now()
            requests.post(f"http://127.0.0.1:5000/chat?content={content}&sender_id={user_id}&chat_id={chatId}&timestamp={timestamp}")
        else:
            pass
        