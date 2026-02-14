import socket
from datetime import datetime
import threading
import time

HOST = '127.0.0.1'
PORT = 9090
MAX_CLIENTS = 2

# Lista de intrebari si raspunsuri corecte
QUESTIONS = [
    {"question": "Care este capitala Frantei?", "answer": "Paris"},
    {"question": "Cat fac 5 + 7?", "answer": "12"},
    {"question": "Care este cel mai mare ocean?", "answer": "Pacific"},
    {"question": "Cati ani are un deceniu?", "answer": "10"},
    {"question": "Care este culoarea preferata a lui Eric?", "answer": "Verde"}
]

class QuizServer:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen()
        
        self.clients = []
        self.client_scores = {}
        self.client_lock = threading.Lock()
        self.quiz_started = False
        self.client_answers = {}
        
    def handle_client(self, conn, addr):
        """Gestioneaza comunicarea cu un client individual"""
        print(f"[NEW CONNECTION] {addr} connected.")
        
        # Trimite mesaj de asteptare
        conn.send("Asteptam sa se conecteze 10 jucatori...\n".encode('utf-8'))
        
        connected = True
        while connected:
            try:
                msg = conn.recv(1024)
                if not msg:
                    break
                    
                # Procesam raspunsul doar daca jocul a inceput
                if self.quiz_started:
                    answer = msg.decode('utf-8').strip()
                    with self.client_lock:
                        self.client_answers[addr] = answer
                        
            except Exception as e:
                print(f"[ERROR] {addr}: {e}")
                break
        
        # Deconectare client
        with self.client_lock:
            if conn in self.clients:
                self.clients.remove(conn)
            if addr in self.client_scores:
                del self.client_scores[addr]
        conn.close()
        print(f"[DISCONNECTED] {addr} disconnected.")
    
    def broadcast_message(self, message):
        """Trimite un mesaj la toti clientii conectati"""
        with self.client_lock:
            for client in self.clients:
                try:
                    client.send(message.encode('utf-8'))
                except:
                    pass
    
    def wait_for_clients(self):
        """Asteapta pana cand se conecteaza MAX_CLIENTS clienti"""
        print(f"[WAITING] Waiting for {MAX_CLIENTS} clients to connect...")
        
        while len(self.clients) < MAX_CLIENTS:
            conn, addr = self.server.accept()
            
            with self.client_lock:
                self.clients.append(conn)
                self.client_scores[addr] = 0
            
            # Start thread pentru fiecare client
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.daemon = True
            thread.start()
            
            print(f"[STATUS] {len(self.clients)}/{MAX_CLIENTS} clients connected.")
            
            # Anunta toti clientii cati jucatori sunt conectati
            self.broadcast_message(f"Jucatori conectati: {len(self.clients)}/{MAX_CLIENTS}\n")
        
        print(f"[READY] {MAX_CLIENTS} clients connected. Starting quiz...")
        self.broadcast_message("\n=== JOCUL INCEPE! ===\n")
        time.sleep(1)
    
    def run_quiz(self):
        """Ruleaza quiz-ul cu toate intrebarile"""
        self.quiz_started = True
        
        for i, q in enumerate(QUESTIONS, 1):
            # Reseteaza raspunsurile
            with self.client_lock:
                self.client_answers = {}
            
            # Trimite intrebarea la toti clientii
            question_msg = f"\n--- Intrebarea {i}/{len(QUESTIONS)} ---\n{q['question']}\nRaspunsul tau: "
            self.broadcast_message(question_msg)
            print(f"[QUESTION {i}] {q['question']}")
            
            # Asteapta 60 secunde pentru raspunsuri sau continuam cand le primit pe toate
            # Verifica mereu cate raspunsuri avem
            
            starttime = datetime.now().second #14:20:02
            
            while True:
                currentTime = datetime.now().second # 14:20:03 -> 100 de ori
                
                if len(self.client_answers) == MAX_CLIENTS:
                   #unlock lock_run_quiz
                   break
                
                if currentTime - starttime > 20:
                    break
            
            """
                lock_run_quiz();
                
                -> thread nou care verifica
            """
                
            # Verifica raspunsurile si acorda puncte
            with self.client_lock:
                for addr, answer in self.client_answers.items():
                    if answer.lower() == q['answer'].lower():
                        self.client_scores[addr] += 1
                        print(f"[CORRECT] {addr} answered correctly!")
            
            # Afiseaza scorurile curente
            self.show_scores()
            time.sleep(10)
        
        # Anunta castigatorul
        self.announce_winner()
    
    def show_scores(self):
        """Afiseaza scorurile curente tuturor clientilor"""
        scores_msg = "\n=== SCORURI CURENTE ===\n"
        with self.client_lock:
            for addr, score in self.client_scores.items():
                scores_msg += f"{addr[0]}:{addr[1]} - {score} puncte\n"
        scores_msg += "======================\n"
        
        self.broadcast_message(scores_msg)
        print(scores_msg)
    
    def announce_winner(self):
        """Anunta castigatorul"""
        with self.client_lock:
            max_score = max(self.client_scores.values())
            winners = [addr for addr, score in self.client_scores.items() if score == max_score]
        
        winner_msg = "\n\n=== JOC TERMINAT ===\n"
        winner_msg += f"SCOR FINAL MAXIM: {max_score} puncte\n"
        
        if len(winners) == 1:
            winner_msg += f"CASTIGATOR: {winners[0][0]}:{winners[0][1]}\n"
        else:
            winner_msg += "CASTIGATORI (EGALITATE):\n"
            for addr in winners:
                winner_msg += f"  - {addr[0]}:{addr[1]}\n"
        
        winner_msg += "===================\n"
        
        self.broadcast_message(winner_msg)
        print(winner_msg)
    
    def start(self):
        """Porneste serverul"""
        print(f"[STARTING] Quiz server is starting on {HOST}:{PORT}")
        
        # Asteapta clientii
        self.wait_for_clients()
        
        # Ruleaza quiz-ul
        self.run_quiz()
        
        print("[DONE] Quiz completed!")
        
        # Inchide toate conexiunile
        with self.client_lock:
            for client in self.clients:
                client.close()
        self.server.close()

if __name__ == "__main__":
    server = QuizServer()
    server.start()
