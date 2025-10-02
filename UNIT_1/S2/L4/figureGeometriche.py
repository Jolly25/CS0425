import math

def perimetro_quadrato():
    lato = float(input("Inserisci la lunghezza del lato del quadrato: "))
    return lato * 4

def circonferenza_cerchio():
    raggio = float(input("Inserisci il raggio del cerchio: "))
    return 2 * math.pi * raggio

def perimetro_rettangolo():
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    return 2 * base + 2 * altezza

print("Calcolo perimetro figure geometriche")
print("Quadrato")
print("Cerchio")
print("Rettangolo")

scelta = input("Scegli una figura: ").lower()

while scelta not in ['quadrato', 'cerchio', 'rettangolo']:
    print("Per favore inserisci una forma geometrica tra quelle proposte: ")
    scelta = input("Scegli una figura: ").lower()

if scelta == "quadrato":
    risultato = perimetro_quadrato()
    print(f"Il perimetro del quadrato è: {risultato}")
elif scelta == "cerchio":
    risultato = circonferenza_cerchio()
    print(f"La circonferenza del cerchio è: {risultato}")
elif scelta == "rettangolo":
    risultato = perimetro_rettangolo()
    print(f"Il perimetro del rettangolo è: {risultato}")
