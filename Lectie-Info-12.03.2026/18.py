"""
Scrieti un program C care converteste toate literele mici din argumentele primite la linia de comanda in litere mari 
si afiseaza rezultatul. Folositi un thread pentru fiecare argument.

"""

import threading


def transforma(index, text, rezultate):
	rezultate[index] = text.upper()


def main():
	argumente = []

	while True:
		text = input().strip()
		if text == "0":
			break
		argumente.append(text)

	rezultate = [""] * len(argumente)
	threaduri = []

	for i, text in enumerate(argumente):
		thread = threading.Thread(target=transforma, args=(i, text, rezultate))
		threaduri.append(thread)
		thread.start()

	for thread in threaduri:
		thread.join()

	for rezultat in rezultate:
		print(rezultat)


main()