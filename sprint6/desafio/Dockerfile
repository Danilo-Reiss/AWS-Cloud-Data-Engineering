# Usando a imagem base oficial do Python
FROM python:3.9-slim

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar o script para o diretório de trabalho do container
COPY script-s3.py .

# Instalar boto3
RUN pip install boto3

# Comando para rodar o script
CMD ["python", "script-s3.py"]
