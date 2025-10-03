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
    comando_utente = input("Cosa vuoi sapere? ")
    if comando_utente.lower() == "esci":
        print("Arrivederci!")
        break
    print(assistente_virtuale(comando_utente))

