with open('exemplo.txt', 'w') as arq:
    arq.write('Ola Mundo\n')
    arq.write('Segunda linha!!!\n')

with open('exemplo.txt', 'a') as info:
    info.write('New Line\n')

with open('exemplo.txt', 'r') as ler:
    conteudo = ler.readlines()
    print(conteudo)

with open('exemplo.txt', 'r') as ler:
    for linha in ler:
        print(linha.strip())


#Segunda parte
with open('alunos.txt', 'w') as arq:
    arq.write('Betinha 1 1\n')
    arq.write('Carlos 7 6\n')
    arq.write('Ana 10 9\n')
    arq.write('Pedro 6 5\n')
    arq.write('Mariana 9 8\n')

dados = []
i = 0
with open('alunos.txt', 'r') as ler:
    for linha in ler:
        dados = linha.strip().split()
        nome = dados[0]

        n1 = float(dados[1])
        n2 = float(dados[2])

        media = (n1 + n2)/2
        i += 1

        print(f'Aluno {i}: {nome} - Nota 1: {n1}, Nota 2: {n2} - Media: {media:.2f}')