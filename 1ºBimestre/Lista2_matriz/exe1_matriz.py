mat = []
linha = []
soma = 0

tamanho = int(input('tamanho mat: '))
print(' ')

for i in range(tamanho):
    for j in range(tamanho):
        num = float(input('digite nums: '))
        linha.append(num)

        if i == j:
            soma += linha[j]
    
    print(' ')
    mat.append(linha)
    linha = []

print(soma)