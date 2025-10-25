# Programare Modulară în Python

În Python putem să separăm un program în mai multe fișiere și să importăm diferite clase/funcții etc. din acele fișiere. Acest mod de lucru se numește **programare modulară**.

## Avantajele programării modulare:
- Cod mai organizat și mai ușor de întreținut
- Reutilizarea codului în mai multe proiecte
- Colaborarea mai ușoară în echipă
- Debugging mai simplu (erori izolate în module specifice)

---

## Tipuri de importuri

### 1. `import modul`

**Explicație:** Importă întregul modul și trebuie să folosim prefixul `modul.` pentru a accesa funcțiile/clasele din el.

**Exemple:**

```python
# fisier: matematica.py
def adunare(a, b):
    return a + b

def inmultire(a, b):
    return a * b

PI = 3.14159
```

```python
# fisier: main.py
import matematica

rezultat1 = matematica.adunare(5, 3)        # 8
rezultat2 = matematica.inmultire(4, 7)      # 28
cerc = 2 * matematica.PI * 10               # 62.8318

print(f"5 + 3 = {rezultat1}")
print(f"4 × 7 = {rezultat2}")
print(f"Circumferința cercului: {cerc}")
```

**Avantaje:**
- Spațiu de nume curat (nu există confuzii despre originea funcțiilor)
- Se vede clar din ce modul vine fiecare funcție

---

### 2. `from modul import x`

**Explicație:** Importă doar anumite funcții/clase specifice din modul. Putem folosi direct numele lor fără prefix.

**Exemple:**

```python
# fisier: geometrie.py
def aria_dreptunghi(lungime, latime):
    return lungime * latime

def aria_cerc(raza):
    return 3.14159 * raza ** 2

def perimetru_patrat(latura):
    return 4 * latura

class Punct:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

```python
# fisier: main.py
from geometrie import aria_dreptunghi, aria_cerc, Punct

# Folosim funcțiile direct, fără prefix
suprafata1 = aria_dreptunghi(10, 5)    # 50
suprafata2 = aria_cerc(7)              # 153.93

punct1 = Punct(3, 4)
print(f"Aria dreptunghi: {suprafata1} cm²")
print(f"Aria cerc: {suprafata2} cm²")
print(f"Punct: ({punct1.x}, {punct1.y})")
```

**Avantaje:**
- Cod mai concis (nu trebuie să scriem prefixul)
- Importăm doar ce avem nevoie (economie de memorie)

---

### 3. `from modul import *`

**Explicație:** Importă TOATE funcțiile, clasele și variabilele din modul. **NU este recomandat!**

**Exemple:**

```python
# fisier: operatii.py
def adunare(a, b):
    return a + b

def scadere(a, b):
    return a - b

def inmultire(a, b):
    return a * b

def impartire(a, b):
    return a / b if b != 0 else "Eroare: împărțire la 0"
```

```python
# fisier: main.py
from operatii import *

# Putem folosi toate funcțiile direct
print(adunare(10, 5))      # 15
print(scadere(10, 5))      # 5
print(inmultire(10, 5))    # 50
print(impartire(10, 5))    # 2.0
```

**Dezavantaje (DE ACEEA NU SE RECOMANDĂ):**
- Nu știm ce funcții am importat exact
- Risc de conflict de nume (dacă avem o funcție `adunare()` și în alt modul)
- Cod greu de debugat
- Considerată practică proastă în Python

---

## Exemplu Complet: Aplicație de Gestionare Elevi

```python
# fisier: elev.py
class Elev:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta
        self.note = []

    def adauga_nota(self, nota):
        if 1 <= nota <= 10:
            self.note.append(nota)

    def medie(self):
        if len(self.note) == 0:
            return 0
        return sum(self.note) / len(self.note)
```

```python
# fisier: statistici.py
def media_clasei(elevi):
    if len(elevi) == 0:
        return 0
    total = sum(elev.medie() for elev in elevi)
    return total / len(elevi)

def cel_mai_bun_elev(elevi):
    if len(elevi) == 0:
        return None
    return max(elevi, key=lambda e: e.medie())
```

```python
# fisier: main.py
from elev import Elev
from statistici import media_clasei, cel_mai_bun_elev

# Cream elevi
ion = Elev("Ion Popescu", 15)
ion.adauga_nota(9)
ion.adauga_nota(8)
ion.adauga_nota(10)

maria = Elev("Maria Ionescu", 16)
maria.adauga_nota(10)
maria.adauga_nota(10)
maria.adauga_nota(9)

andrei = Elev("Andrei Dumitru", 15)
andrei.adauga_nota(7)
andrei.adauga_nota(8)
andrei.adauga_nota(8)

clasa = [ion, maria, andrei]

# Statistici
print(f"Media clasei: {media_clasei(clasa):.2f}")
cel_mai_bun = cel_mai_bun_elev(clasa)
print(f"Cel mai bun elev: {cel_mai_bun.nume} cu media {cel_mai_bun.medie():.2f}")
```

---

## Recomandări

1. **Folosește `import modul`** când lucrezi cu multe funcții din același modul
2. **Folosește `from modul import x, y`** când ai nevoie doar de câteva funcții specifice
3. **Evită `from modul import *`** - este considerat anti-pattern în Python!
