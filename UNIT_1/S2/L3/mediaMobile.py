def media_mobile(numeri, n):
    medie = []
    for i in range(len(numeri)):
        # ultimi n elementi fino all'indice i
        w = numeri[max(0, i-n+1) : i+1]
        media = sum(w) / len(w)
        medie.append(media)
    return medie

numeri = [10, 20, 30, 40, 50, 1, 2, 3, 4, 5]
n = 3

risultato = media_mobile(numeri, n)
print(risultato)
