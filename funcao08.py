def calcular_medias(notas):
    total = sum(notas)
    media = total /len(notas)
    return media

notas = [8.5, 8.0, 6.5, 9.0]
media = calcular_medias(notas)
print("A média é: ", media)