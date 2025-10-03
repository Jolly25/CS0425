import datetime

def assistente_virtuale(comando):
    if comando == "Qual è la data di oggi?":
        oggi = datetime.date.today()
        return "La data di oggi è " + oggi.strftime("%d/%m/%Y")

    elif comando == "Che ore sono?":
        ora_attuale = datetime.datetime.now().time()
        return "L'ora attuale è " + ora_attuale.strftime("%H:%M:%S")

    elif comando == "Come ti chiami?":
        return "Mi chiamo Assistente Virtuale"

    else:
        return "Non ho capito la tua domanda."


while True:
    comando_utente = input("Cosa vuoi sapere? ")
    if comando_utente.lower() == "esci":
        print("Arrivederci!")
        break
    print(assistente_virtuale(comando_utente))
