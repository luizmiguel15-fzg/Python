def ver_positivo(numeros):
    positivos = []
    for i in numeros:
        if i >= 0:
            positivos.append(i)
    
    return positivos

lista = []
while True:
    num = input('digite numeros inteiros, [p] para: ')

    if num == 'p':
        break

    lista.append(int(num))

print(f'lista possitivos: {ver_positivo(lista)}')