import datetime

def assistente_virtuale(comando):
    if comando == "Qual è la data di oggi?":
        oggi = datetime.date.today()
        risposta = "La data di oggi è " + oggi.strftime("%d/%m/%Y")

    elif comando == "Che ore sono?":
        ora_attuale = datetime.datetime.now().time()
        risposta =  "L'ora attuale è " + ora_attuale.strftime("%H:%M:%S")

    elif comando == "Come ti chiami?":
        risposta = "Mi chiamo Assistente Virtuale"

    else:
        risposta = "Non ho capito la tua domanda."
    return risposta 


while True:
    menu = print("- Qual è la data di oggi?\n - Che ore sono?\n -Come ti chiami?\n Digita esci se vuoi uscire")
    comando_utente = input("Cosa vuoi sapere? ")
    if comando_utente.lower() == "esci":
        print("Arrivederci!")
        break
    print(assistente_virtuale(comando_utente))

# Cosa fa questo programma? Questo programma non è altro che una sorta di asistente virtuale che chiede all'utente di inserire una scelta, scelta che l'utente dovrà fare consultando un menù
# Una volta che l'utente ha eseguito la sua scelta, stamperà l'output contenuto nella funzione assistente_virtuale (Che ore sono? Qual è la data di oggi?)

