import os
import boto3
from datetime import datetime

# Configurando client e credenciais
s3 = boto3.client('s3',
                aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                aws_session_token=os.getenv('AWS_SESSION_TOKEN'))

# Carregando arquivo no S3
def upload_aws(arquivo_local, bucket, arquivo_s3):
    s3.upload_file(arquivo_local, bucket, arquivo_s3)
    print(f"Carregado com sucesso: {arquivo_local} para {arquivo_s3}")
    return True

# Captura de elementos de data (ano/mês/dia)
agora = datetime.now()
ano = agora.strftime("%Y")
mes = agora.strftime("%m")
dia = agora.strftime("%d")

# Lista de arquivos a serem carregados
arquivos_upload = [
    {'arquivo_local': '/data/movies.csv', 'arquivo_s3': f'/Raw/Local/CSV/Movies/{ano}/{mes}/{dia}/movies.csv'},
    {'arquivo_local': '/data/series.csv', 'arquivo_s3': f'/Raw/Local/CSV/Series/{ano}/{mes}/{dia}/series.csv'}
]
bucket = 'data-lake-danilo'

# Carregar todos os arquivos
for arquivo in arquivos_upload:
    upload_aws(arquivo['arquivo_local'], bucket, arquivo['arquivo_s3'])