def procesare_preturi():
    with open("librarie.in", "r") as f:
        n = int(f.readline()) 
        preturi = list(map(int, f.readline().split()))
        Q = int(f.readline()) 

        undo_stack = []
        redo_stack = []

        for zi in range(Q):
            t = int(f.readline()) 
            operatii = []

            for op in range(t):
                operatii.append(f.readline().strip().split())

            for operatie in operatii:
                if operatie[0] == "+" or operatie[0] == "-":
                    tip = operatie[0] 
                    index1 = int(operatie[1]) - 1  
                    index2 = int(operatie[2]) - 1
                    valoare = int(operatie[3])

                    
                    undo_stack.append(("modificare", index1, index2, tip, valoare))
                    redo_stack.clear()  # Anulăm redo-ul dacă există operații noi

                    for i in range(index1, index2 + 1):
                        if tip == "+":
                            preturi[i] += valoare
                        elif tip == "-":
                            preturi[i] -= valoare

                elif operatie[0] == "u":
                    if undo_stack:
                        last_op = undo_stack.pop()
                        index1, index2, tip, valoare = last_op

                        redo_stack.append(last_op)
                        for i in range(index1, index2 + 1):
                            if tip == "+":
                                preturi[i] -= valoare 

                            elif tip == "-":
                                preturi[i] += valoare  

                elif operatie[0] == "r":
                    if redo_stack:
                        last_op = redo_stack.pop()
                        index1, index2, tip, valoare = last_op

                        undo_stack.append(last_op)
                        for i in range(index1, index2 + 1):
                            if tip == "+":
                                preturi[i] += valoare 

                            elif tip == "-":
                                preturi[i] -= valoare  

            with open("librarie.out", "a") as fout:
                fout.write(" ".join(map(str, preturi)) + "\n")

procesare_preturi()
