""" Leia o arquivo person.json, faça o parsing e imprima seu conteúdo. """

import json

with open('person.json', 'r') as arquivo:
    dados_person = json.load(arquivo)

print(dados_person)
