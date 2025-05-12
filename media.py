def calcular_media(lista_notas):
    total = 0

    for nota in lista_notas:
        total += nota
    
    media = total / len(lista_notas)

    return media

notas = [9, 1, 8]

print(calcular_media(notas))