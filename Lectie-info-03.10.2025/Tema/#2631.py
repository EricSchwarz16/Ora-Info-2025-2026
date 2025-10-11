line = ""
dict = {}

while True: 
    line = input()
    
    if line == '':
        break
    
    cuvinte = line.split(' ')

    for cuvant in cuvinte:
        if cuvant != '':
            cuvant_sortat = ''.join(sorted(cuvant))
            
            if cuvant_sortat in dict.keys():
                dict[cuvant_sortat] += 1
            else:
                dict[cuvant_sortat] = 1
    
max_apr:int = 0
    
for key in dict:
    if dict[key] > max_apr:
        max_apr = dict[key]
        
print(max_apr)
        
        
