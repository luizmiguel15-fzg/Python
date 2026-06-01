import math
cat_oposto = float(input("Digite o comprimento do cateto oposto: "))
cat_adjacente = float(input("Digite o comprimento do cateto adjacente: "))
soma_hipo = (cat_oposto**2 + cat_adjacente**2)
hipopotenusa = math.sqrt(soma_hipo)
print(f'A hipotenusa vai medir {hipopotenusa:.2f}')