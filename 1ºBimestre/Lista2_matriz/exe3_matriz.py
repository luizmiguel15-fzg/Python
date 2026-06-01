import numpy as np

mat = []
mat_trans = []
mat_trans2 = []
lista = []
lin = []

linha = int(input("tamanho linha: "))
coluna = int(input("tam colun: "))

for i in range(linha):
    for j in range(coluna):
        num = int(input("numeros: "))
        lista.append(num)
    mat.append(lista)
    lista = []

for i in range(coluna):
    for j in range(linha):
        lin.append(mat[j][i])
    mat_trans.append(lin)
    lin = []

#mat_trans2 = np.transpose(mat)

for i in range(len(mat_trans)):
    print(mat_trans[i])