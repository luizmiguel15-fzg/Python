def cal_desconto(val, per_descont):
    return val*(per_descont/100)

def gerar_fatura(numeros, porcen):
    soma = 0

    for i in numeros:
        soma += i
    
    decont = cal_desconto(soma, porcen)

    return soma - decont

lista = []
while True:
    num = input('digite numeros inteiros, [p] para: ')

    if num == 'p':
        break

    lista.append(int(num))

descon = int(input('val desconto: '))

print(f'valor finar a pagar e: {gerar_fatura(lista,descon)}')