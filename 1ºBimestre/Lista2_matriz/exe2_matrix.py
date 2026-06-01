mat = []
linha = []
mat_pos = []
linha_pos = [0,0]

qnt_c = int(input('tamanho da coluna: '))
qnt_l = int(input('tamanho da linha: '))
print(' ')

for i in range(qnt_l):
    for j in range(qnt_c):
        num = float(input('digite nums: '))
        linha.append(num)
            
    mat.append(linha)
    linha = []

maior = mat[0][0] 

for i in range(qnt_l):
    for j in range(qnt_c):
        if maior < mat[i][j]:
            maior = mat[i][j]

            x = i
            y = j
        

print(f'maior valor: {maior}, linha: {x}, coluna: {y}')