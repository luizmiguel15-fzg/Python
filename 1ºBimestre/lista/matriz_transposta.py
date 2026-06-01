matriz = [[0,0,0],[0,0,0],[0,0,0]]
transposta = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(3):
    for j in range(3):
        dado = input('digite: ')
        matriz[i][j] = dado

        transposta[j][i] = dado

for i in range(len(transposta)):
    print(transposta[i])



    