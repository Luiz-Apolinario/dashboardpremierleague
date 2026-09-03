import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv

def coletar_classificacao():
    #pegar o token da apu no arquivo env
    load_dotenv()
    api_token = os.getenv("API_TOKEN")

    url = "https://api.football-data.org/v4/competitions/PL/standings" #url da api

    headers = {
        "X-Auth-Token": api_token
    }

    resposta = requests.get(url, headers=headers) #coletando dados da api

    print(resposta.status_code)

    #dados formatados vao para o arquivo classificacao.json para conferir
    dados = resposta.json()
    with open("classificacao.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    #criando uma lista comtodos os times ordenados por posicao
    classificacao = []
    for time in dados["standings"][0]["table"]:
        classificacao.append({"Posição": time["position"], "Time": time["team"]["shortName"], "Jogos": time["playedGames"], "Saldo de Gols": time["goalDifference"], "Pontos": time["points"]})

    tabela = pd.DataFrame(classificacao) #criando a tabela com pandas
    return tabela