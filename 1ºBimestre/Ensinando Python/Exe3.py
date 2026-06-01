# Peça ao usuário para digitar uma frase.

# Depois:

# Separe a frase em palavras
# Mostre quantas palavras existem na frase
# Exiba a primeira e a última palavra digitada

frase = str(input('digite uma frase: '))

frase = frase.split()

print(f'a frase contem {len(frase)} de palavras')
print(f'a primeira palavra e: {frase[0]}. E a ultima e: {frase[len(frase) - 1]}')