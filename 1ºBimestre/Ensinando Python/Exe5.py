# Você recebeu a seguinte mensagem de um usuário:

# "   oi, TUDO bem???   "

# Crie um programa que:

# Remova os espaços extras do início e do fim
# Converta todo o texto para minúsculo
# Substitua "???" por "?"
# Deixe a primeira letra da frase em maiúsculo

# Resultado esperado:

# "Oi, tudo bem?"

texto = "   oi, TUDO bem???   "
texto = texto.strip().lower().replace("???", "?")
texto = texto.capitalize()

print(texto)