# MANIPULAÇÃO DE STRINGS
print('<','='*10,"teste de manilulação de string", '='*10,'>')
endline = ''*50
print(endline)

frase = "Curso em Video Python"
print(frase[9:])
len(frase) # tamanho da string
print(len(frase))

print(frase.count('o')) # conta quantas vezes a letra 'o' aparece 
print(frase.count('o',0,13)) # conta quantas vezes a letra 'o' aparece do caractere 0 ao 12

print(frase.find('Curso')) # mostra a posição onde começa a palavra 'Curso'
print(frase.find('Android')) # se não encontrar a palavra, retorna -1

print('Curso' in frase) # verifica se a palavra 'Curso' está na frase

print(frase.replace('Python', 'Android')) # substitui a palavra 'Python' por 'Android'

print(frase.upper()) # transforma a frase toda em maiúsculo
print(frase.lower()) # transforma a frase toda em minúsculo

print(frase.capitalize()) # transforma a primeira letra em maiúsculo

print(frase.title()) # transforma a primeira letra de cada palavra em maiúsculo

print(frase.split()) # divide a frase em várias partes, criando uma lista
print(frase.split()[2]) # mostra a terceira palavra da frase dividida

frase = frase.split() # divide a frase em várias partes, criando uma lista
print('-'.join(frase)) # une os caracteres da frase com o caractere '-'


frase2 = "            Aprenda Python                      "
print(frase2.strip()) # remove os espaços inúteis no começo e no final da frase

# MENU GRANTE EM UM SO print
print('-' * 30)
print('     MENU GRANTE     ')
print('-' * 30)
print("""[1] - Iniciar novo jogo
[2] - Carregar jogo
[3] - Opções
[4] - Sair do jogo
[5] - Créditos""")
print('-' * 30)

# INICIO DO PROGRAMA PRINCIPAL
nome = str(input("Digite seu nome: "))

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()

N_nome = len(nome) - nome.count(' ')
N_nome_1 = len(nome.split()[0])

print(f'nome em maiúsculo: {nome_maiusculo}')
print(f'nome em minúsculo: {nome_minusculo}')
print(f'número de letras sem espaços: {N_nome}')
print(f'número de letras do primeiro nome: {N_nome_1}')