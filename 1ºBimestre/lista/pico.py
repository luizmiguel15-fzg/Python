lista = []
picos = []

while True:
    num = int(input("digite, -1 para: "))
    if num == -1:
        break

    lista.append(num)

for i in range(len(lista)):
    if i > 0 and i < len(lista) - 1:
        if lista[i - 1] < lista[i] and lista[i + 1] < lista[i]:
            picos.append(lista[i])
    else:
        if i == 0:
            if lista[i + 1] < lista[i]:
                picos.append(lista[i])

        elif i == len(lista) - 1:
            if lista[i - 1] < lista[i]:
                picos.append(lista[i])

print(picos)




