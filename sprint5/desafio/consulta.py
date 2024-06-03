import boto3

# Configurando sessão padrão
boto3.setup_default_session(profile_name='default')
s3 = boto3.client('s3')

# Chamando método de parsing do S3 Select
resp = s3.select_object_content(
    Bucket='mybucket-desafio',
    Key='202301_final.csv',
    ExpressionType='SQL',
    Expression="SELECT max(cast(TARIFA as decimal)), min(cast(TARIFA as decimal)), avg(cast(TARIFA as decimal)), CASE WHEN max(cast(TARIFA as decimal)) > 3500 THEN 'Tarifa máxima maior que 3,500' END, UTCNOW() FROM s3object s WHERE ORIGEM in (upper('sbsp')) and DESTINO in (upper('sbrj'))",
    InputSerialization = {
        'CSV': {
            'FileHeaderInfo': 'Use',
        },
        'CompressionType': 'NONE'
    },
    OutputSerialization = {
        'CSV': {}
    },
)

# Cabeçalho
print('tarifa_máxima, tarifa_mínima, tarifa_média, status, current_datetime')

# Decodificação em utf-8 dos eventos do método
for event in resp['Payload']:
    if 'Records' in event:
        records = event['Records']['Payload'].decode('utf-8')
        print(records)
    elif 'Stats' in event:
        pass