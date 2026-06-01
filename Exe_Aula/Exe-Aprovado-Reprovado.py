with open('DS/Exe-Manipulando_Dados/alunos_Notas.txt', 'w') as arq:
    for i in range(4):
        dados = input('digite: [nome nota1 nota2] do aluno: ')
        arq.write(f'{dados}\n')

with open('DS/Exe-Manipulando_Dados/alunos_Notas.txt', 'r') as arq:
    num = 0
    for i in arq:
        dados = i.strip().split()
        
        nome = dados[0]

        n1 = float(dados[1])
        n2 = float(dados[2])

        media = (n1 + n2) / 2
        num += 1

        if media >= 6:
            print(f'Aluno {num}: {nome} Aprovado - Media: {media}')
        else:
            print(f'Aluno {num}: {nome} Reprovado - Media: {media}')