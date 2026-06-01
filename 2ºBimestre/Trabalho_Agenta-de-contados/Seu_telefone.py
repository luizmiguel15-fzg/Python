import os

def inserir_condado(nome: str, numero: str, insta: str):
    insta = ''.join(['@',insta,'\n'])

    dado = ','.join([nome, numero, insta])

    with open('agenda.txt', 'a') as arq:
        arq.write(dado)

def todos_contdos():
    with open('agenda.txt', 'r') as arq:
        contatos = arq.readlines()
        for contato in contatos:
            nome, numero, insta = contato.split(',')
            print(f'Nome: {nome}')
            print(f'Numero: {numero}')
            print(f'Instagram: {insta}')
            print('-'*30)

def contactsin():
    print("""
    [1] Procurar pelo nome
    [2] Procurar pelo numero
    [3] Procurar pelo instagram
    """)
    esc = int(input('Escolha uma opção: '))
    os.system('cls')

    if esc == 1:
        procura = input('Digite o nome: ')
    elif esc == 2:
        procura = input('Digite o numero: ')
    elif esc == 3:
        procura = input('Digite o @ do instagram: ')
        procura = ''.join(['@', procura])
    os.system('cls')

    with open('agenda.txt', 'r') as arq:
        contatos = arq.readlines()
        for contato in contatos:
            nome, numero, insta = contato.split(',')

            nome = nome.lower()

            if esc == 1:
                if procura.lower() in nome:
                    print(f'Nome: {nome.capitalize()}')
                    print(f'Numero: {numero}')
                    print(f'Instagram: {insta}')
                    print('-'*30)
            elif esc == 2:
                if procura in numero:
                    print(f'Nome: {nome.capitalize()}')
                    print(f'Numero: {numero}')
                    print(f'Instagram: {insta}')
                    print('-'*30)
            elif esc == 3:
                if procura in insta:
                    print(f'Nome: {nome.capitalize()}')
                    print(f'Numero: {numero}')
                    print(f'Instagram: {insta}')
                    print('-'*30)

if not os.path.exists('agenda.txt'):
    with open('agenda.txt', 'w'):
        pass

while True:
    os.system('cls')

    print('=*'*20, 'MENU DE INTERAÇOES', '*='*20)
    print("""
        [1] Adicionar novo contato
        [2] Olhar os contatos
        [3] Parar Programa""")

    indr = int(input('Digite o NUMERO da interaçao que deseja executar: '))

    if indr == 1:
        os.system('cls')

        print('<', '='*15, 'INSERINDO NOVO CONDADO', '='*15, '>')
        nome = input('Digite o nome do contato: ').title()
        numero = input('Digite o numero de telefone do contato: ')
        insta = input('Digite o @ do instagram do seu contato, nao coloque o [@] na frente: ')

        inserir_condado(nome, numero, insta)

        input('Aperte Enter para continuar')
    
    elif indr == 2:
         os.system('cls')
         print("""
         [1] Mostrar todos os contatos
         [2] Procurar contato
         """)
         esc = int(input('Escolha uma opção: '))
         os.system('cls')
         if esc == 1:
            todos_contdos()
         elif esc == 2:
            contactsin()
         input("Digite Enter para continuar")

    else:
       os.system('cls')

       print('Programa Encerrado')
       break