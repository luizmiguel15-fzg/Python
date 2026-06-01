import math
angu = float(input("Digite o ângulo que você deseja: "))
seno = math.sin(math.radians(angu))
cosseno = math.cos(math.radians(angu))
tangente = math.tan(math.radians(angu))
print(f'O ângulo de {angu} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angu} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angu} tem a TANGENTE de {tangente:.2f}')