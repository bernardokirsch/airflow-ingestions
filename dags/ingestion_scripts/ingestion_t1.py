import requests
import json
import xml.etree.ElementTree as ET
import boto3
from datetime import datetime

def save_to_s3(file_path, bucket_name, object_name):
    s3 = boto3.client('s3')

    try:
        s3.upload_file(file_path, bucket_name, object_name)
        print(f'Arquivo {file_path} enviado com sucesso para o bucket {bucket_name} com o nome {object_name}')
    except Exception as e:
        print(f'Erro ao enviar o arquivo para o S3: {e}')

def xml_to_json(xml_string):
    root = ET.fromstring(xml_string)
    
    def element_to_dict(element):
        attributes = element.attrib
        element_dict = {'attributes': attributes} if attributes else {}

        for child in element:
            child_dict = element_to_dict(child)
            element_dict[child.tag] = child_dict.get('text', '')
        
        return element_dict
    
    root_dict = element_to_dict(root)

    return json.dumps(root_dict, ensure_ascii=False)

# Retorna as combinações disponíveis da API
def get_moedas():
    url = 'https://economia.awesomeapi.com.br/xml/available'

    response = requests.get(url)

    if response.status_code == 200:
        json_data = xml_to_json(response.content)

        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f'/tmp/resultado_{timestamp}.json'

        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(json_data)

        object_name = f'currency_quote_ingestion_{timestamp}.json'
        save_to_s3(file_name, 'bernardokirsch-currency-quote-ingestion', object_name)
    else:
        print('Erro ao fazer a solicitação:', response.status_code)

get_moedas()