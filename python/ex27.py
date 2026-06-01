nome = str(input('Digite seu nome completo: '))
nomes = nome.split()
print(f'Primeiro nome: {nomes[0]}')
print(f'Último nome: {nomes[len(nomes) - 1]}')