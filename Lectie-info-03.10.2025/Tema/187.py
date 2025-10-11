dict = { '2': 0, '3':0, '5':0, '7':0}

with open(r"C:\Users\Bob\Documents\Erik-meditatii\Ora-Info-2025-2026\Lectie-info-03.10.2025\Tema\ciffrecv.in", "r") as file:
     for line in file:
         for number in line.split(' '):
            if number in dict.keys():
                dict[number] += 1
            
max_apr = 0
max_nr = -1

for key in dict:
    if dict[key] >= max_apr:
        max_apr = dict[key]
        max_nr = key
        
print(f"{max_nr} {max_apr}")
