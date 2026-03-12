"""

readers and writers

avem o resursa care poate fi citita de oricati cititori, dar care 
uneori este schimbata de un scriitor. Putem avea mai multi cititori si mai multi
scriitori. Vrem sa simulam operatiile facute pe aceasta resursa(citire scriere)

id 1 citeste resursa -> count = 1
id 2 citeste resursa -> count = 2
id 3 citeste resursa -> cout = 3
id 1 a terminat de citit -> count = 2
id 3 a terminat de citir -> count = 1
id 2 a terminat de citit -> count = 0
id 4 a modificat resursa
id 5 a modificat resursa
id 9 citeste resursa
id 9 termina decitit
id 7 a modificat resursa

random de cititori, numar random de scriitori
citirea dureaza random intre 0.5 - 2s   


is_writing
reader_count
condition

cititor
-----------
while is_writing
    condition.wait()

reader_count += 1
condition.notify_all()

time.sleep(random) #simulez citirea

with conditon:
    reader_count -= 1
    
    if reader_count == 0
        condition.notify_all()
-----------


scriitor
-----------
while is_writing or reader_count > 0
    condition.wait()

print("modific resursa")
    
condition.notify_all() #daca cineva e in asteptare poate sa vina
-----------



with condition: #blochez lockul din conditie
    while afara nu ploua:
        condition.wait() -> deblochez lockul si threadul meu doarme pana cand primeste un semnal -> examplu 2 threaduri care stau aici si asteapta sa fie semnalate
        -> daca le dau notify_all se trezesc toate

meteo_checker:
    while true:
        daca ploua:
            condition.notify_all() -> trezeste toate threadurile care asteapta
            condition.notify_one()  -> trezeste un singur thread care asteapta
"""