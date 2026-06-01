# Peça ao usuário para digitar uma palavra ou frase.

# Depois:

# Inverta o texto usando fatiamento
# Verifique se o texto é um palíndromo (ignorar maiúsculas/minúsculas)

# Exemplo:
# "arara" → é palíndromo
# "Ame a ema" → também deve ser considerado

frase = str(input("Digite uma palavra ou frase: "))

frase_invertida = frase[::-1].lower()

if frase_invertida == frase.lower():
    print("É um palíndromo")
else:
    print("Não é um palíndromo")