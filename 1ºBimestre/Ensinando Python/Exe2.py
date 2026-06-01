# Peça ao usuário para digitar o nome completo.

# Depois:

# Mostre o nome todo em letras maiúsculas
# Mostre o nome todo em letras minúsculas
# Mostre quantos caracteres o nome tem (sem contar espaços)

nome = str(input("digite seu nome completo: "))

qtd_carac_nome = len(nome) - nome.count(' ')

print(f"seu nome todo em maisculo: {nome.upper()}")
print(f"seu nome todo em minusculo: {nome.lower()}")
print(f'a quandidade de caracters que seu nome tem (sem espaços) e: {qtd_carac_nome}')