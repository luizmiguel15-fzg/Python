def somar_2_numeros(a, b):
    soma = a + b
    return soma

def ola_pessoa(nome):
    print(f'ola, {nome}')

def meida(a, b):
    meida = somar_2_numeros(a, b)/2
    return meida

def dobra_lista(lista):
    lista_dobrada = []
    for i in lista:
        lista_dobrada.append(i * 2)
    
    return lista_dobrada


nome2 = str(input('dite nome: '))

num1 = 5
num2 = 5

lista1 = [1,2,3,4,5]

print(f'a media e: {meida(num1, num2):.2}')
print(f'lista dobrada {dobra_lista(lista1)}')

ola_pessoa(nome2)
print(somar_2_numeros(num1, num2))