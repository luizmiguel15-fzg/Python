def encontrar_maximo(lista):
    maior=lista[0]
    for numero in lista:
        if numero > maior:
            maior = numero
    return maior
    
entrada = str(input('digite os numeros com espaços: '))
entrada = entrada.split() # reparte uma string conforme os espaços e cria uma lista

lista = []
for valor in entrada:
    lista.append(int(valor))

print('o maior numero é: ', encontrar_maximo(lista))
