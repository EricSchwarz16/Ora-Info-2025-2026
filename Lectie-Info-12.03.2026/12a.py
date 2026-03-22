"""
Scrieti un program C care citeste o matrice de intregi dintr-un fisier. Programul creeaza un numar de thread-uri egal cu numarul 
de randuri in matrice, iar fiecare thread calculeaza suma numerelor de pe un rand. Procesul principal asteapta ca thread-urile sa 
isi incheie executia si apoi afiseaza sumele.
"""

import threading


def suma_rand(index, rand, rezultate):
	rezultate[index] = sum(rand)


def citeste_matrice_din_fisier(cale_fisier):
	matrice = []
	with open(cale_fisier, "r", encoding="utf-8") as fisier:
		for linie in fisier:
			linie = linie.strip()
			if linie:
				matrice.append([int(x) for x in linie.split()])
	return matrice


def main():
	cale_fisier = input().strip()

	try:
		matrice = citeste_matrice_din_fisier(cale_fisier)
	except FileNotFoundError:
		print("Fisier inexistent")
		return
	except ValueError:
		print("Fisier invalid")
		return

	if not matrice:
		print("Matrice vida")
		return

	coloane = len(matrice[0])
	for rand in matrice:
		if len(rand) != coloane:
			print("Matrice invalida")
			return

	rezultate = [0] * len(matrice)
	threaduri = []

	for i, rand in enumerate(matrice):
		thread = threading.Thread(target=suma_rand, args=(i, rand, rezultate))
		threaduri.append(thread)
		thread.start()

	for thread in threaduri:
		thread.join()

	for suma in rezultate:
		print(suma)


main()