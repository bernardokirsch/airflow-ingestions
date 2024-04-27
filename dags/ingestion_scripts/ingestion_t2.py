import requests
import json
import os

resultado_path = os.environ.get('RESULTADO_PATH')

# Retorna informações das moedas disponíveis
def get_moedas_infos():

    with open(resultado_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    url = 'https://economia.awesomeapi.com.br/last/'

    combinations = list(data.keys())
    
    for combination in combinations:
        url += combination + ','

    url = url[:-1]

    response = requests.get(url)

    data = response.json()

    with open('/tmp/resultado_2.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)

get_moedas_infos()