import random
a1 = input('digite o nome do aluno: ')
a2 = input('digite o nome do segundo aluno: ')
a3 = input('digite o nome do terceiro aluno: ')
a4 = input('digite o nome do quarto aluno: ')

lista = [a1, a2, a3, a4]

escolhido = random.choice(lista)  # Escolhe um aluno aleatoriamente da lista
print('o aluno escolhido foi {}'.format(escolhido))
