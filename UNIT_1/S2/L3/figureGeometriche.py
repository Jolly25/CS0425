import math

def perimetro_quadrato():
    lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
    return lato*4

def circonferenza_cerchio():
    raggio = float(input("Inserisci il raggio del cerchio: "))
    return 2 * math.pi * raggio

def perimetro_rettangolo():
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    return 2 * base + 2 * altezza

print("Calcolo perimetro figure geometriche")
print("1 - Quadrato")
print("2 - Cerchio")
print("3 - Rettangolo")

scelta = input("Scegli una figura (1/2/3): ")

if scelta == "1":
    risultato = perimetro_quadrato()
    print(f"Il perimetro del quadrato è: {risultato}")
elif scelta == "2":
    risultato = circonferenza_cerchio()
    print(f"La circonferenza del cerchio è: {risultato}")
elif scelta == "3":
    risultato = perimetro_rettangolo()
    print(f"Il perimetro del rettangolo è: {risultato}")
else:
    print("Scelta non valida.")