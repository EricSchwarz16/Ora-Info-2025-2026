def suma_maxima(s, n, sir):
    max_suma = 0  
    subsir = []  # Inițializăm subsirul pentru stocarea elementelor valide
    adaugate = set()  # Set pentru a marca elementele deja adăugate în subsir
    
    
    sir.sort(reverse=True)
    
    i = 0  
    
    # Adăugăm elemente în subsir atâta timp cât suma nu depășește s
    while i < n:
        suma = sum(subsir)  
        if suma + sir[i] <= s and sir[i] not in adaugate:
            subsir.append(sir[i])  
            adaugate.add(sir[i])  
            i += 1  
        else:
            i += 1  

        
        max_suma = max(max_suma, sum(subsir))

    # După ce am parcurs tot șirul, începem să scoatem elemente din subsir în ordine inversă
    while subsir:
        suma -= subsir.pop()  
        if suma <= s:
            # Căutăm în continuare secvențe în șir
            j = 0
            while j < n:
                if sir[j] not in adaugate and suma + sir[j] <= s:
                    suma += sir[j]  
                    subsir.append(sir[j])  
                    adaugate.add(sir[j])  
                j += 1

            
            max_suma = max(max_suma, suma)

    return max_suma


# Citire date
n, s = map(int, input().split())  
sir = list(map(int, input().split()))  

# Apelăm funcția și afișăm rezultatul
print(suma_maxima(s, n, sir))
