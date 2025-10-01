import re

def conta_parole(testo):
    testo = testo.lower()

    testo = re.sub(r"[^a-zàèéìòù\s]", "", testo)  
    
    parole = testo.split()

    occorrenze = {}
    for parola in parole:
        if parola in occorrenze:
            occorrenze[parola] += 1
        else:
            occorrenze[parola] = 1
    
    return occorrenze

frase = input("Inserisci una frase: ")
print(conta_parole(frase))
