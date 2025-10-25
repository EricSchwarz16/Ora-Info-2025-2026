with open ("librarie.in", "r")as fin:
    nr_carti = int(fin.readline())
    preturi = list(map(int, fin.readline().split()))
    Q = int(fin.readline())