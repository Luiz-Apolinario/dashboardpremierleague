import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_token = os.getenv("API_TOKEN")

url = "https://api.football-data.org/v4/competitions/PL/standings"

headers = {
    "X-Auth-Token": api_token
}

resposta = requests.get(url, headers=headers)

print(resposta.status_code)
print(resposta.json())