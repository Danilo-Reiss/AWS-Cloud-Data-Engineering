from tmdbv3api import TMDb, Discover
import json
import os
import boto3
from datetime import datetime

# Configuração da API TMDb
tmdb = TMDb()
tmdb.api_key = "b264a841f0419dd0a6c3f408778df9ba"
tmdb.language = 'en'

discover = Discover()

# Parâmetros
genres = "14,878"
include_adult = True
sort_by = "popularity.desc"

# Diretório local para armazenar temporariamente os arquivos JSON e estado
local_dir = "/tmp/tmdb_data"  # Diretório temporário no Lambda
os.makedirs(local_dir, exist_ok=True)

# Configuração do cliente S3
s3 = boto3.client('s3')
bucket = 'data-lake-danilo'

# Arquivo para armazenar o estado da última página processada
state_file = os.path.join(local_dir, "state.json")

# Função para carregar o estado atual
def load_state():
    if os.path.exists(state_file):
        with open(state_file, "r") as file:
            return json.load(file)
    return {"last_page": 0, "file_index": 1}

# Função para salvar o estado atual
def save_state(state):
    with open(state_file, "w") as file:
        json.dump(state, file)
    upload_to_s3(state_file, f'/Raw/TMDB/JSON/{datetime.now().strftime("%Y/%m/%d")}/state.json')

# Função para descobrir filmes
def discover_movies(page):
    result_list = []
    resultados = discover.discover_movies({
        "page": page,
        "sort_by": sort_by,
        "with_genres": genres,
        "include_adult": include_adult
    })

    for resultado in resultados:
        result_list.append(resultado._json)

    return result_list

# Função para salvar resultados em arquivo JSON
def save_to_json(result_list, file_index):
    output_file = os.path.join(local_dir, f"data_{file_index}.json")
    with open(output_file, "w", encoding="utf-8") as json_file:
        json.dump(result_list, json_file, ensure_ascii=False, indent=4)
    print(f"Dados dos filmes salvos em {output_file}")
    upload_to_s3(output_file, f'/Raw/TMDB/JSON/{datetime.now().strftime("%Y/%m/%d")}/data_{file_index}.json')

# Função para fazer upload dos arquivos para o S3
def upload_to_s3(local_file, s3_file):
    s3.upload_file(local_file, bucket, s3_file)
    print(f"Carregado com sucesso: {local_file} para s3://{bucket}/{s3_file}")

# Função principal para automatizar o processo
def main(event, context):
    state = load_state()
    current_page = state["last_page"] + 1
    file_index = state["file_index"]

    if current_page > 100:
        print("Todas as páginas foram processadas.")
        return

    result_list = []
    for page in range(current_page, current_page + 5):
        if page > 100:  # Evitar exceder a última página
            break
        resultados = discover_movies(page)
        result_list.extend(resultados)

    if result_list:
        save_to_json(result_list, file_index)
        state["last_page"] = page
        state["file_index"] += 1
        save_state(state)

# Handler do AWS Lambda
def lambda_handler(event, context):
    main(event, context)
    return {
        'statusCode': 200,
        'body': json.dumps('Execução concluída com sucesso!')
    }
