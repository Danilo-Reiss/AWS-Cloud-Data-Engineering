#! python
import csv
from urllib import request 


def read(url):
    with request.urlopen(url) as entrada: # --> Faz o request da URL
        print('Baixando o CSV...')
        dados = entrada.read().decode('latin1') # --> Lê e decodifica o conteúdo do CSV
        print('Download completo!')
        for cidade in csv.reader(dados.splitlines()): # --> Faz a divisão em lista e separa em linhas os dados
            print(f'{cidade[8]}: {cidade[3]}') # --> Pega a coluna de índice 8 e 3


if __name__ == '__main__':
    read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
