import os
estoque = [
    ["Camiseta", 15, 49.90],
    ["Calça", 10, 89.90],
    ["Tenis", 8, 199.99],
    ["Bone", 20, 29.90],
    ["Jaqueta", 5, 149.90],
    ["Meias", 30, 9.99],
    ["Bermuda", 12, 59.90],
    ["Moletom", 7, 129.90],
    ["Cinto", 14, 39.90],
    ["Relogio", 6, 249.90],
]
num = 1
carrinho: list[list[str, int, float]] = []
lista_remocoes: list[list[str, int]] = []

# funçao para remover ou adicionar produtos do estoque, dependendo se o produto esta no carrinho ou nao
def remov_adi_estoque(estoque: list[list[str, int, float]], nome: str, qtd: int, esta_carrinho: bool,) -> None:
    nome = nome.capitalize()

    indx_estoque = -1
    indx_remocoes = -1

    for i in range(len(estoque)):
        if estoque[i][0] == nome:
            indx_estoque = i
            
    for i in range(len(lista_remocoes)):
        if lista_remocoes[i][0] == nome:
            indx_remocoes = i

    if indx_estoque == -1:
        return

    if esta_carrinho:
        estoque[indx_estoque][1] += qtd

        if indx_remocoes != -1:
            if qtd >= lista_remocoes[indx_remocoes][1]:
                lista_remocoes.pop(indx_remocoes)
                return
            else:
                lista_remocoes[indx_remocoes][1] -= qtd
                return
    else:
        lista_remocoes.append([estoque[indx_estoque][0], estoque[indx_estoque][1]])
        estoque[indx_estoque][1] -= qtd
        return

# funcao para limpar o estoque de produtos com quantidade menor ou igual a 0
def limpar_estoque_zerado(estoque: list[list[str, int, float]]) -> None:
    for i in estoque[:]:
        if i[1] <= 0:
            estoque.remove(i)


# funcao para exibir o carrinho de compras, finalizar a compra ou remover itens do carrinho
def carrinho_compras(carrinho: list[list[str, int, float]]) -> bool | None:
    valor_total = 0

    print("=" * 20, "Carrinho de Compras", "=" * 20)
    print("_" * 72)
    print(f'| {"Produto":^30} | {"Quantidade":^15} | {"Valor Total":^12} |')
    print("-" * 72)

    for i in carrinho:
        print(f"| {i[0]:<30} | {i[1]:^15} | R${i[2]:>10.2f} |")
        valor_total += i[2]

    print("-" * 72)
    print(f"valor total da compra: R${valor_total:.2f}")
    print(" ")

    intera = int(
        input(
            "[0] - Finalizar Compra\n[1] - Voltar para o Menu de Vendas\n[2] - Remover Item do Carrinho\n\nDigite o numero da interaçao: "
        )
    )

    if intera == 0:
        limpar_estoque_zerado(estoque)
        carrinho.clear()
        print("Compra finalizada!")
        input("Enter...")
        return True
    elif intera == 1:
        return True
    elif intera == 2:
        nome = str(input("Digite o nome do produto para remover do carrinho: "))
        qtd = int(input("Digite a quantidade a ser removida: "))

        remov_adi_estoque(estoque, nome, qtd, True)
        remover_produtos(nome, qtd, carrinho)

        for i in range(len(estoque)):
            if estoque[i][0] == nome:
                indice: int = i
        for j in carrinho:
            if j[0] == nome:
                j[2] = j[1] * estoque[indice][2]

# funcao para realizar a venda, adicionando o produto ao carrinho e removendo a quantidade do estoque
def realizar_venda(
    estoque: list[list[str, int, float]], nome: str, quantidade: int) -> None:
    nome = nome.capitalize()
    valor = 0

    for i in estoque:
        if i[0] == nome:
            if i[1] >= quantidade:
                valor = i[2] * quantidade
                carrinho.append([nome, quantidade, valor])
                
                remov_adi_estoque(estoque, nome, quantidade, False)

                print("Produto adicionado ao carrinho!")
                return
            else:
                print("quantidade de venta acima do limite")
                return

    print("Produdo nao encontrado!")


# funcao para adicionar produtos ao estoque, caso o produto ja exista, a quantidade sera adicionada a quantidade ja existente
def adicionar_produtos(nome: str, quantidade: int, preco: float) -> list[str, int, float] | None:
    nome = nome.capitalize()

    for i in estoque:
        if i[0] == nome:
            i[1] += quantidade
            return None

    return [nome, quantidade, preco]

# funcao para remover produtos do estoque, caso a quantidade do produto seja menor ou igual a 0, o produto sera removido do estoque
def remover_produtos(
    nome: str, quantidade: int, estoque: list[list[str, int, float]]) -> None:
    nome = nome.capitalize()
    for i in estoque:
        if i[0] == nome:
            i[1] -= quantidade
            if i[1] <= 0:
                estoque.remove(i)
                print("Produto removido!")
                input("Enter...")
                return
            else:
                print("quantidade do produto atualizada!")
                input("Enter...")
                return

    print("Produdo nao encontrado!")

# funcao para editar a quantidade e o preco do produto, caso o produto nao exista, sera exibida uma mensagem de erro
def editar_produtos(nome: str) -> None:
    indice = -1
    nome = nome.capitalize()

    for i in range(len(estoque)):
        if estoque[i][0] == nome:
            indice = i

    if indice == -1:
        print("Produdo nao encontrado!")
        return

    print(
        """[1] - Editar quantidade do produto
[2] - Editar preco do produto
[3] - Editar os dois"""
    )

    intr = int(input("Digite o numero da interaçao: "))

    if intr == 1:
        print(" ")
        nova_qtd = int(input("Digite a nova quantidade do produto: "))
        estoque[indice][1] = nova_qtd
        print("Quantidade do produto editada!")
        input("Enter...")

    elif intr == 2:
        print(" ")
        novo_preco = float(input("Digite o novo preco do produto: "))
        estoque[indice][2] = novo_preco
        print("Preco do produto editado!")
        input("Enter...")

    elif intr == 3:
        print(" ")
        nova_qtd = int(input("Digite a nova quantidade do produto: "))
        novo_preco = float(input("Digite o novo preco do produto: "))
        estoque[indice][1] = nova_qtd
        estoque[indice][2] = novo_preco
        print("Quantidade e preco do produto editados!")
        input("Enter...")


# funcao para exibir o estoque, exibindo o numero do produto, nome, quantidade e valor
def exibir_estoque(estoque: list[list[str, int, float]]) -> None:
    num = 1
    print("-=" * 20, "Estoque", "-=" * 20)
    print("_" * 72)
    print(f'| {"Nº":^3} | {"Produto":^30} | {"Quantidade":^15} | {"Valor":^12} |')
    print("-" * 72)

    for i in estoque:
        print(f"| {num:<3} | {i[0]:<30} | {i[1]:^15} | R${i[2]:>10.2f} |")
        num += 1

    print("-" * 72)
    input("Enter...")


# INICIO DO PROGRAMA
while True:
    os.system("cls")
    print("<", "=" * 15, "Estoque do Tio Betinha", "=" * 15, ">")
    print(
        """[1] - Menu Modificar Estoque
[2] -Menu de Vendas
[3] - Olhar Estoque
[4] - Parar Execuçao
        """
    )

    try:
        intr = int(input("Digite o numero da interaçao: "))
    except:
        continue

    if intr == 1:
        os.system("cls")
        while True:
            os.system("cls")
            print("-" * 20, "Adcionar Produdos", "-" * 20)
            print(
                """[1] - Adicionar Produdo
[2] - Editar Produdo
[3] - Remover Produdo
[4] - Voltar"""
            )
            intr = int(input("Digite o numero da interaçao: "))

            if intr == 1:
                os.system("cls")
                nome = str(input("digite o nome do produdo: "))
                qtd = int(input("Digite a quandidade do protudo: "))
                preco = float(input("Digite o preco do produdo: "))

                novo = adicionar_produtos(nome, qtd, preco)
                if novo:
                    estoque.append(novo)
                    print("Produdo adicionado!")
                input("Enter...")

            elif intr == 2:
                os.system("cls")
                exibir_estoque(estoque)
                nome = str(input("digite o nome do produdo: "))
                editar_produtos(nome)

            elif intr == 3:
                os.system("cls")
                exibir_estoque(estoque)
                print(" ")
                nome = str(input("digite o nome do produdo: "))
                qtd = int(input("Digite a quandidade para remover: "))
                remover_produtos(nome, qtd, estoque)

            elif intr == 4:
                break

            else:
                print("Digite um numero valido!")

    elif intr == 2:
        while True:
            os.system("cls")
            exibir_estoque(estoque)

            print("-" * 20, "Menu de Vendas", "-" * 20)
            print(
                """[1] - solicitar Produto
[2] - Olhar Carrinho
[3] - Voltar"""
            )
            intr = int(input("Digite o numero da interaçao: "))

            if intr == 1:
                realizar_venda(
                    estoque,
                    str(input("Digite o nome do produto: ")),
                    int(input("Digite a quantidade do protudo: ")),
                )
                input("Enter...")

            elif intr == 2:
                while True:
                    os.system("cls")
                    if carrinho_compras(carrinho):
                        break

            elif intr == 3:
                break

    elif intr == 3:
        exibir_estoque(estoque)

    elif intr == 4:
        break
    else:
        os.system("cls")
        continue