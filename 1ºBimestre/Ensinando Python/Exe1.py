# **EXERCICIO 1**
# Crie um programa que receba uma frase do usuário e mostre:
# Quantos caracteres a frase possui (incluindo espaços)
# Quantas letras "a" aparecem na frase (não diferenciar maiúsculas de minúsculas)

frase = str(input("Digite uma frase: "))

frase = frase.lower()
qtd_carc_frase = len(frase)
n_A_frase = frase.count('a')

print(f'a frase contem {qtd_carc_frase} de caracter e possui {n_A_frase} de [a]')