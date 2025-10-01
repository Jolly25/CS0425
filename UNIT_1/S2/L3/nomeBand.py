# Scrivere un programma in Python che genera un nome per una band musicale utilizzando due input forniti dall'utente: la città di origine e il nome del proprio animale domestico.
citta = input("Inserisci il nome della tua città d'origine: ")
animale = input("Inscerisci ora il nome del tuo animale domestico: ")

#nomeBand = citta + animale  versione 1
nomeBand = citta + " " + animale #versione 2

print("Il nome della tua band è: ", nomeBand)