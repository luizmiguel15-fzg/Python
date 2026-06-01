info_cidades = {}
soma = 0
qtd = 0

cidade_mais_quente = None
temp_mais_quente = float('-inf')

cidade_mais_fria = None
temp_mais_fria = float('inf')

with open('temperaturas.txt', 'r') as arq:
    for linha in arq:
        info_cidades['cidade'], info_cidades['temperatura'] = linha.strip().split(',')

        info_cidades['temperatura'] = float(info_cidades['temperatura'])

        if info_cidades['temperatura'] > temp_mais_quente:
            cidade_mais_quente = info_cidades['cidade']
            temp_mais_quente = info_cidades['temperatura']
        
        elif info_cidades['temperatura'] < temp_mais_fria:
            cidade_mais_fria = info_cidades['cidade']
            temp_mais_fria = info_cidades['temperatura']

        soma += info_cidades['temperatura']
        qtd += 1

print(f'A cidade mais quente é {cidade_mais_quente} com {temp_mais_quente}°C.')
print(f'A cidade mais fria é {cidade_mais_fria} com {temp_mais_fria}°C.')

meida = soma / qtd

print(f'A média das temperaturas é {meida:.01f}ºC.')