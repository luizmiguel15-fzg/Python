import requests


def obter_previsao(cidade: str):
    cidade = cidade.lower().strip()

    #Busca latitude e longitude (geocodificaçao)
    url_gro = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1&language=pt&format=json"

    respose_geo = requests.get(url_gro)
    dados_geo = respose_geo.json()

    if not dados_geo.get("results"):
        return f"NAO"

    local = dados_geo.get("results")
    lat = local[0]["latitude"]
    log = local[0]["longitude"]

    pais = local[0].get("country")
    regiao = local[0].get("admin1")

    nome = f"{cidade}, {regiao} - {pais}"

    # Buscando o clima
    url_clima = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={log}&current_weather=true"

    dados_clima = requests.get(url_clima).json()

    temp = str(dados_clima["current_weather"]["temperature"]) + " °C"
    vel_vento = str(dados_clima["current_weather"]["windspeed"]) + " km/h"

    resp = (
        f"------------------- Previsao para: {nome} --------------------------"
        f"\nTemperatura: {temp}\n"
        f"Velocidade do Vento: {vel_vento}"
    )

    return resp


print(obter_previsao("itatiba"))
