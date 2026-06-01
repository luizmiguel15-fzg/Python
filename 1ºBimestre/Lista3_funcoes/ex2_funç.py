def analisar_notas(nota1,nota2, nota3):
    media= (nota1+nota2+nota3)/3
    print(f'ola, sua media é {media}')
      
    if media>=7:
       return 'A'
    elif media<7:
        return 'R'
    
n1 = float(input('digite a nota 1: '))
n2 = float(input('digite a nota 2: '))
n3 = float(input('digite a nota 3: '))

retorno= analisar_notas(n1,n2,n3) #chamada da função

if retorno == 'A':
    print('voce esta aprovado')
elif retorno == 'R':
    print('voce esta reprovado')

