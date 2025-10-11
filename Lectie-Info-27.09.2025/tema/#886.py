def isVowel(litera) -> bool:
    return litera in 'aeiou'

sir = input()

curr_length = 0
curr_start = 0  # începutul secvenței curente

max_length = 0
max_start = 0  # începutul celei mai lungi secvențe

for i in range(len(sir)):
    if not isVowel(sir[i]):
        if curr_length == 0:
            curr_start = i  # începe o nouă secvență de consoane
        curr_length += 1
        # actualizăm dacă:
        # 1. e o secvență mai lungă
        # 2. e la fel de lungă dar mai din dreapta
        if curr_length > max_length or (curr_length == max_length and curr_start > max_start):
            max_length = curr_length
            max_start = curr_start
    else:
        curr_length = 0  # secvența s-a încheiat

# extragem subșirul
rezultat = sir[max_start:max_start + max_length]
print(rezultat)
