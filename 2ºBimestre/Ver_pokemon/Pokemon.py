import requests
import os

type_colors = {
    "normal": "#A8A77A",
    "fire": "#EE8130",
    "water": "#6390F0",
    "electric": "#F7D02C",
    "grass": "#7AC74C",
    "ice": "#96D9D6",
    "fighting": "#C22E28",
    "poison": "#A33EA1",
    "ground": "#E2BF65",
    "flying": "#A98FF3",
    "psychic": "#F95587",
    "bug": "#A6B91A",
    "rock": "#B6A136",
    "ghost": "#735797",
    "dragon": "#6F35FC",
    "dark": "#705746",
    "steel": "#B7B7CE",
    "fairy": "#D685AD",
}
cores_info = {
    "hp": "#78C850",
    "xp": "#FFD700",
    "peso": "#607D8B",
    "altura": "#2196F3",
    "tipo": "#FFFFFF",
}
pokemons = []

def achar_pokemon(pokemons: list[str, str | None, str | None], qtd_poke: int):
    nome = []
    peso_KG = []
    altura_M = []
    HPs = []
    Ataques = []
    Defesa = []
    Xp = []
    url_imagens = []
    tipos = []
    cores = []
    respostas = []
    dados = []

    if qtd_poke == 1:
        urls = [f"https://pokeapi.co/api/v2/pokemon/{pokemons[0]}"]

        msg = f"Pokemon ['{pokemons[0]}'] encontrado, abra o arquivo Pokemons.html para ver o card do pokemon"
    elif qtd_poke == 2:
        urls = [
            f"https://pokeapi.co/api/v2/pokemon/{pokemons[0]}",
            f"https://pokeapi.co/api/v2/pokemon/{pokemons[1]}",
        ]

        msg = f"Pokemon ['{pokemons[0]}'] e Pokemon ['{pokemons[1]}'] encontrados, abra o arquivo Pokemons.html para ver o card dos pokemons"
    else:
        urls = [
            f"https://pokeapi.co/api/v2/pokemon/{pokemons[0]}",
            f"https://pokeapi.co/api/v2/pokemon/{pokemons[1]}",
            f"https://pokeapi.co/api/v2/pokemon/{pokemons[2]}",
        ]

        msg = f"Pokemon ['{pokemons[0]}'] , Pokemon ['{pokemons[1]}'] e Pokemon ['{pokemons[2]}'] encontrados, abra o arquivo Pokemons.html para ver o card dos pokemons"

    for i in range(len(urls)):
        if requests.get(urls[i]).status_code != 200:
            os.system("cls")
            return f"Pokemon ['{pokemons[i]}'] nao escontrado"

        respostas.append(requests.get(urls[i]))

        dados.append(respostas[i].json())

    for i in range(len(dados)):
        nome.append(dados[i]["name"].capitalize())

        peso_KG.append(dados[i]["weight"] / 10)
        altura_M.append(dados[i]["height"] / 10)

        HPs.append(dados[i]["stats"][0]["base_stat"])
        Ataques.append(dados[i]["stats"][1]["base_stat"])
        Defesa.append(dados[i]["stats"][2]["base_stat"])
        Xp.append(dados[i]["base_experience"])

        tipos.append(
            ", ".join(
                elementos["type"]["name"].capitalize()
                for elementos in dados[i]["types"]
            )
        )
        cores.append(type_colors[dados[i]["types"][0]["type"]["name"]])

        url_imagens.append(
            dados[i]["sprites"]["other"]["official-artwork"]["front_default"]
        )

        if not url_imagens[i]:
            url_imagens[i] = dados[i]["sprites"]["front_default"]

    cards = ""

    for i in range(qtd_poke):
        cards += f"""
        <div class="card" style="border-color:{cores[i]};">
            <img class="pokemon-img" src="{url_imagens[i]}" alt="{nome[i]}">
            <h1>{nome[i]}</h1>
            <span class="badge" style="background-color:{cores[i]};">
                {tipos[i]}
            </span>

            <table class="info-table">
                <tr>
                    <td class="label" style="color: {cores_info['altura']}">Altura</td>
                    <td class="value" style="color: {cores_info['altura']}">{altura_M[i]} m</td>
                </tr>
                <tr>
                    <td class="label" style="color: {cores_info['peso']}">Peso</td>
                    <td class="value" style="color: {cores_info['peso']}">{peso_KG[i]} kg</td>
                </tr>
                <tr>
                    <td class="label" style="color: {cores_info['hp']}">HP</td>
                    <td class="value" style="color: {cores_info['hp']}">{HPs[i]}</td>
                </tr>
                <tr>
                    <td class="label" style="color: {cores_info['xp']}">XP</td>
                    <td class="value" style="color: {cores_info['xp']}">{Xp[i]}</td>
                </tr>
                <tr>
                    <td class="label">Ataque</td>
                    <td class="value">{Ataques[i]}</td>
                </tr>
                <tr>
                    <td class="label">Defesa</td>
                    <td class="value">{Defesa[i]}</td>
                </tr>
            </table>
        </div>
        """

    html_final = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Card - Pokedex </title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            gap: 1.5vh;
        }}
        .card {{
            background-color: white;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            padding: 30px;
            text-align: center;
            width: 300px;
            border-top: 8px solid #000000;
        }}
        .pokemon-img {{
            width: 200px;
            height: 200px;
            object-fit: contain;
        }}
        h1 {{
            color: #333;
            margin: 10px 0;
            font-size: 24px;
        }}
        .badge {{
            background-color: #000000;
            color: white;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 14px;
            display: inline-block;
            margin-bottom: 20px;
        }}
        .info-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }}
        .info-table td {{
            padding: 8px;
            border-bottom: 1px solid #eee;
            font-size: 15px;
        }}
        .info-table td.label {{
            font-weight: bold;
            color: #666;
            text-align: left;
        }}
        .info-table td.value {{
            text-align: right;
            color: #333;
        }}
    </style>
</head>
<body>
    {cards}
</body>
</html>
"""

    with open("Pokemons.html", "w", encoding="utf-8") as arq:
        arq.write(html_final)

    return msg


while True:
    os.system("cls")

    print("=" * 50, f"\n {'Escolhendo Pokemons':^55} \n", "=" * 50)
    print("""    [1] 1 Pokemon
    [2] 2 Pokemons
    [3] 3 Pokemons
    [4] Sair""")
    indx = input(
        "Digite o numero correspondente a quantidade de pokemons que deseja achar: "
    )

    if indx == "1":
        os.system("cls")
        pokemons.append(str(input("Digite o nome do 1 Pokemon: ")))

        print(achar_pokemon(pokemons, 1))
        input("Enter...")

    elif indx == "2":
        os.system("cls")
        pokemons.append(str(input("Digite o nome do 1 Pokemon: ")))
        pokemons.append(str(input("Digite o nome do 2 Pokemon: ")))

        print(achar_pokemon(pokemons, 2))
        input("Enter...")

    elif indx == "3":
        os.system("cls")
        pokemons.append(str(input("Digite o nome do 1 Pokemon: ")))
        pokemons.append(str(input("Digite o nome do 2 Pokemon: ")))
        pokemons.append(str(input("Digite o nome do 3 Pokemon: ")))

        print(achar_pokemon(pokemons, 3))
        input("Enter...")

    elif indx == "4":
        os.system("cls")
        print("Saindo...")
        break

    else:
        os.system("cls")
        print("Numero invalido, Digite um numero valido")
        input("Enter...")