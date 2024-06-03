import pandas as pd

# Carrega o arquivo CSV para um DataFrame
df = pd.read_csv('202301.CSV', delimiter=';')

# Substitui todas as ocorrências de vírgula por ponto na coluna 'TARIFA'
df['TARIFA'] = df['TARIFA'].str.replace(',', '.')

# Salva o DataFrame modificado em outro arquivo
df.to_csv('202301_final.csv', index=False)
